from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Membre
from .forms import MembreForm
from django.utils import timezone
from parametrage.enums import choix_sex, choix_identite
from parametrage.operations import OperationsHelpers
from django.urls import reverse


# @login_required
def membre_list(request):
    context = {
        "membres": Membre.objects.all(),
        "choix_sex": choix_sex,
        "choix_identite": choix_identite,
    }
    return render(request, "membre_list.html", context)


def get_choices(request):
    return JsonResponse({"choix_sex": choix_sex, "choix_identite": choix_identite})


# @login_required
def membre_create(request):

    form = MembreForm(request.POST) if request.method == "POST" else MembreForm()
    return save_membre_form(request, form, "membre_create.html", "create")


def save_membre_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string("membre_list.html")
                data["url_redirect"] = reverse("membre_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:

        context = {"form": form}
        print(form.errors)
        data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def membre_update(request, pk):
    membre = get_object_or_404(Membre, pk=pk)

    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            membre = form.save(commit=False)
            membre.date_update = timezone.now()
            membre.user_validate = request.user
            membre.save()
            messages.success(request, "Membre mis à jour avec succès.")
            return redirect("membre_list")
    else:
        form = MembreForm(instance=membre)

        # Vérifiez si la requête est AJAX
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return render(request, "membre_form.html", {"form": form})

    return render(request, "membre_update.html", {"form": form})


# @login_required
def membre_detail(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    return render(request, "membre_detail.html", {"membre": membre})


# @login_required
def membre_delete(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == "POST":
        membre.date_delete = timezone.now()
        membre.user_delete = request.user
        membre.save()
        messages.success(request, "Membre supprimé avec succès.")
        return redirect("membre_list")
    return render(request, "membres/membre_confirm_delete.html", {"membre": membre})


# @login_required
def membre_validate(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == "POST":
        membre.date_validate = timezone.now()
        membre.user_valide = request.user
        membre.save()
        messages.success(request, "Membre validé avec succès.")
        return redirect("membre_list")
    return render(request, "membres/membre_confirm_validate.html", {"membre": membre})


# vue pr index
def index_view(request):
    return render(request, "index.html")
