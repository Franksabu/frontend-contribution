from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from .models import Type_cotisation
from .forms import Type_cotisationForm
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def type_cotisation_list(request):
    context = {
        "type_cotisations": Type_cotisation.objects.all,
    }
    return render(request, "type_cotisation_list.html", context)


def type_cotisation_create(request):
    form = (
        Type_cotisationForm(request.POST)
        if request.method == "POST"
        else Type_cotisationForm()
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


def type_cotisation_detail(request, pk):
    type_cotisation = get_object_or_404(Type_cotisation, pk=pk)
    return render(
        request, "type_cotisation_details.html", {"type_cotisation": type_cotisation}
    )
