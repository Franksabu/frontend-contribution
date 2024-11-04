from django.http import JsonResponse
from django.shortcuts import render, redirect
from cotisation.models import Contribution
from django.shortcuts import get_object_or_404
from cotisation.forms import ContributionForm, CotisationForm
from django.template.loader import render_to_string
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def contribution_list(request):
    context = {
        "contibutions": Contribution.objects.all(),
    }
    return render(request, "contibution_list.html", context)


def contribution_create(request):
    form = ContributionForm(request.POST) if request.method == "POST" else CotisationForm()
    return save_contribution_form(request, form, "contribution_create.html", "create")


def save_contribution_form(request, form, template_name, action):
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
                data["html_content_list"] = render_to_string("contribution_list.html")
                data["url_redirect"] = reverse("contribution_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(
            template_name, context, request=request
        )  # Rendre le formulaire en cas de requête GET
    return JsonResponse(data)


def contribution_detail(request, pk):
    cotisation = get_object_or_404(Contribution, pk=pk)
    return render(request, "contribution_details.html", {"cotisation": cotisation})
