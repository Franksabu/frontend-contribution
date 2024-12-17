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
from django.contrib.auth.decorators import login_required


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


# def membre_update(request, id):
#     membre = get_object_or_404(Membre, id=id)

#     if request.method == "POST":
#         form = MembreForm(request.POST, instance=membre)
#         if form.is_valid():
#             membre = form.save(commit=False)
#             membre.date_update = timezone.now()
#             membre.user_valide = request.user
#             membre.save()
#             messages.success(request, "Membre mis à jour avec succès.")
#             return redirect("membre_list")
#     else:
#         form = MembreForm(instance=membre)
#     print(form)

#     return render(request, "membre_update.html", {"html_form": form, "membre": membre})

@login_required
def membre_update(request, id):
    membre = get_object_or_404(Membre, id=id)

    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            membre = form.save(commit=False)
            membre.date_update = timezone.now()
            membre.user_valide = request.user
            membre.save()
            if request.user.is_authenticated:
                membre.user_valide = request.user
            else:
                # Gérer le cas où l'utilisateur n'est pas authentifié
                return JsonResponse(
                    {
                        "form_is_valid": False,
                        "form_error": "Vous devez être connecté pour effectuer cette action.",
                    }
                )

            return JsonResponse({"form_is_valid": True, "url_redirect": "/membre/list/"})
        else:
            return JsonResponse(
                {
                    "form_is_valid": False,
                    "form_error": "Le formulaire contient des erreurs.",
                }
            )

    else:
        form = MembreForm(instance=membre)

    # Rendre le formulaire en HTML partiel
    html_form = render_to_string(
        "membre_update.html",
        {"form": form, "membre": membre},
        request=request,
    )
    return JsonResponse({"html_form": html_form})


# @login_required
def membre_detail(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    return render(request, "membre_detail.html", {"membre": membre})


# @login_required
def membre_delete(request, id):
    membre = get_object_or_404(Membre, id=id)

    if request.method == "POST":
        membre.delete()
        return JsonResponse(
            {
                "success": True,
                "url_redirect": reverse("membre_list"),  # Redirection après suppression
            }
        )
    return JsonResponse({"success": False})


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
