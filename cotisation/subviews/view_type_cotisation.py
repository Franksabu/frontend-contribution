from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect, render, get_object_or_404
from cotisation.models import TypeCotisation
from cotisation.forms import TypecotisationForm
from parametrage.operations import OperationsHelpers
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def type_cotisation_list(request):
    context = {
        "type_cotisations": TypeCotisation.objects.all(),
    }
    return render(request, "type_cotisation_list.html", context)


def type_cotisation_create(request):
    form = (
        TypecotisationForm(request.POST)
        if request.method == "POST"
        else TypecotisationForm()
    )
    return save_type_cotisation_form(
        request, form, "type_cotisation_create.html", "create"
    )


def save_type_cotisation_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string(
                    "type_cotisation_list.html"
                )
                data["url_redirect"] = reverse("type_cotisation_list")

            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:

        context = {"form": form}
        data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# def type_cotisation_update(request, id):
#     type_cotisation = get_object_or_404(TypeCotisation, id=id)

#     if request.method == 'POST':
#         form = TypecotisationForm(request.POST, instance=type_cotisation)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({
#                 'form_is_valid': True,
#                 'url_redirect': reverse('type_cotisation_list')})
#             # return redirect('type_cotisation_list')
#         else:
#             return JsonResponse({
#                 'form_is_valid': False,
#                 'form_error': form.errors
#             })
#             # return render(request, 'cotisation_update.html', {'form': form, 'type_cotisation': type_cotisation})
#     else:
#         form = TypecotisationForm(instance=type_cotisation)

#     return render(request, 'type_cotisation_update.html', {'form': form, 'type_cotisation': type_cotisation})

@login_required
def cotisation_update(request, id):
    type_cotisation = get_object_or_404(TypeCotisation, id=id)

    if request.method == "POST":
        print(request.POST)
        form = TypecotisationForm(request.POST, instance=type_cotisation)
        if form.is_valid():
            type_cotisation = form.save(commit=False)  # Ne sauvegardez pas encore
            type_cotisation.user_valide = request.user  # Assignez l'utilisateur
            type_cotisation.save()
            if request.user.is_authenticated:
                type_cotisation.user_valide = request.user
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
        form = TypecotisationForm(instance=type_cotisation)


# @login_required
def type_cotisation_delete(request, id):
    type_cotisation = get_object_or_404(TypeCotisation, id=id)

    if request.method == "POST":
        type_cotisation.delete()
        return JsonResponse({
            "success": True,
            "url_redirect": reverse("type_cotisation_list")  # Redirection après suppression
        })
    return JsonResponse({"success": False})


def type_cotisation_detail(request, pk):
    type_cotisation = get_object_or_404(TypeCotisation, pk=pk)
    return render(
        request, "type_cotisation_details.html", {"type_cotisation": type_cotisation}
    )
