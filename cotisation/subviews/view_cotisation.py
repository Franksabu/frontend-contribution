from django.http import JsonResponse
from django.shortcuts import render, redirect
from cotisation.models import Cotisation
from django.shortcuts import get_object_or_404
from cotisation.forms import CotisationForm
from django.template.loader import render_to_string
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def cotisation_list(request):
    context = {
        "cotisations": Cotisation.objects.all()
    }
    return render(request, "cotisation_list.html", context)


def cotisation_create(request):
    form = CotisationForm(request.POST) if request.method == "POST" else CotisationForm()
    return save_cotisation_form(request, form, "cotisation_create.html", "create")


def save_cotisation_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(
                request, action, form
            )
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string("cotisation_list.html")
                data["url_redirect"] = reverse("cotisation_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(
            template_name, context, request=request
        )  # Rendre le formulaire en cas de requête GET
    return JsonResponse(data)


def cotisation_detail(request, pk):
    cotisation = get_object_or_404(Cotisation, pk=pk)
    return render(request, "cotisation_details.html", {"cotisation": cotisation})
