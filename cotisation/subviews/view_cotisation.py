from django.http import JsonResponse
from django.shortcuts import render, redirect
from cotisation.models import Cotisation
from django.shortcuts import get_object_or_404
from cotisation.forms import CotisationForm
from django.template.loader import render_to_string
from parametrage.operations import OperationsHelpers
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def cotisation_list(request):
    context = {"cotisations": Cotisation.objects.all()}
    return render(request, "cotisation_list.html", context)


def cotisation_create(request):
    form = (
        CotisationForm(request.POST) if request.method == "POST" else CotisationForm()
    )
    return save_cotisation_form(request, form, "cotisation_create.html", "create")


def save_cotisation_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string("cotisation_list.html")
                data["url_redirect"] = reverse("cotisation_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = form.errors
                # data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(
            template_name, context, request=request
        )  # Rendre le formulaire en cas de requête GET
    return JsonResponse(data)


# def cotisation_update(request, id):
#     cotisation = get_object_or_404(Cotisation, id=id)

#     if request.method == 'POST':
#         form = CotisationForm(request.POST, instance=cotisation)
#         if form.is_valid():
#             form.save()
#             return redirect('cotisation_list')
#         else:
#             return render(request, 'cotisation_update.html', {'form': form, 'cotisation': cotisation})
#     else:
#         form = CotisationForm(instance=cotisation)

#     return render(request, 'cotisation_update.html', {'form': form, 'cotisation': cotisation})


@login_required
def cotisation_update(request, id):
    cotisation = get_object_or_404(Cotisation, id=id)

    if request.method == "POST":
        print(request.POST)
        form = CotisationForm(request.POST, instance=cotisation)
        if form.is_valid():
            cotisation = form.save(commit=False)  # Ne sauvegardez pas encore
            cotisation.user_valide = request.user  # Assignez l'utilisateur
            cotisation.save()
            if request.user.is_authenticated:
                cotisation.user_valide = request.user
            else:
                # Gérer le cas où l'utilisateur n'est pas authentifié
                return JsonResponse(
                    {
                        "form_is_valid": False,
                        "form_error": "Vous devez être connecté pour effectuer cette action.",
                    }
                )

            return JsonResponse({"form_is_valid": True, "url_redirect": "/cotisation/list/"})
        else:
            return JsonResponse(
                {
                    "form_is_valid": False,
                    "form_error": "Le formulaire contient des erreurs.",
                }
            )

    else:
        form = CotisationForm(instance=cotisation)

    # Rendre le formulaire en HTML partiel
    html_form = render_to_string(
        "cotisation_update.html",
        {"form": form, "cotisation": cotisation},
        request=request,
    )
    return JsonResponse({"html_form": html_form})


# @login_required
def cotisation_delete(request, id):
    cotisation = get_object_or_404(Cotisation, id=id)

    if request.method == "POST":
        cotisation.delete()
        return JsonResponse(
            {
                "success": True,
                "url_redirect": reverse(
                    "cotisation_list"
                ),  # Redirection après suppression
            }
        )
    return JsonResponse({"success": False})


def cotisation_detail(request, pk):
    cotisation = get_object_or_404(Cotisation, pk=pk)
    return render(request, "cotisation_details.html", {"cotisation": cotisation})
