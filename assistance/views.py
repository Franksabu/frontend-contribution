from pyexpat.errors import messages
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from .models import Assistance
from .forms import AssistanceForm
from parametrage.operations import OperationsHelpers
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def assistance_list(request):
    context = {
        "assistances": Assistance.objects.all(),
    }
    return render(request, "assistance_list.html", context)


@login_required
def assistance_create(request):
    form = (
        AssistanceForm(request.POST) if request.method == "POST" else AssistanceForm()
    )
    return save_assistance_form(request, form, "assistance_create.html", "create")


@login_required
def save_assistance_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string("assistance_list.html")
                data["url_redirect"] = reverse("assistance_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


@login_required
def assistance_update(request, id):
    assistance = get_object_or_404(Assistance, id=id)

    if request.method == "POST":
        form = AssistanceForm(request.POST, instance=assistance)
        if form.is_valid():
            assistance = form.save(commit=False)
            assistance.date_update = timezone.now()
            assistance.user_valide = request.user
            assistance.save()
            if request.user.is_authenticated:
                assistance.user_valide = request.user
            else:
                # Gérer le cas où l'utilisateur n'est pas authentifié
                return JsonResponse(
                    {
                        "form_is_valid": False,
                        "form_error": "Vous devez être connecté pour effectuer cette action.",
                    }
                )

            return JsonResponse(
                {"form_is_valid": True, "url_redirect": "/assistance/assistances/list/"}
            )
        else:
            return JsonResponse(
                {
                    "form_is_valid": False,
                    "form_error": "Le formulaire contient des erreurs.",
                }
            )

    else:
        form = AssistanceForm(instance=assistance)

    # Rendre le formulaire en HTML partiel
    html_form = render_to_string(
        "assistance_update.html",
        {"form": form, "assistance": assistance},
        request=request,
    )
    return JsonResponse({"html_form": html_form})


@login_required
def assistance_detail(request, pk):
    assistance = get_object_or_404(Assistance, pk=pk)
    return render(request, "assistance_detail.html", {"assistances": assistance})


@login_required
def assistance_delete(request, id):
    assistance = get_object_or_404(Assistance, id=id)

    if request.method == "POST":
        assistance.delete()
        return JsonResponse(
            {
                "success": True,
                "url_redirect": reverse(
                    "assistance_list"
                ),  # Redirection après suppression
            }
        )
    return JsonResponse({"success": False})
