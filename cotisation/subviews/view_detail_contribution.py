from django.http import JsonResponse
from django.shortcuts import render, redirect
from cotisation.models import DetailContribution
from django.shortcuts import get_object_or_404
from cotisation.forms import Detail_contributionForm
from django.template.loader import render_to_string
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def detail_contribution_list(request):
    context = {
        "detail_contributions": DetailContribution.objects.all(),
    }
    return render(request, "detail_contribution_list.html", context)


def detail_contribution_create(request):
    form = Detail_contributionForm(request.POST) if request.method == "POST" else Detail_contributionForm()
    return save_detail_contribution_form(request, form, "detail_contribution_create.html", "create")


def save_detail_contribution_form(request, form, template_name, action):
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
                data["html_content_list"] = render_to_string("detail_contribution_list.html")
                data["url_redirect"] = reverse("detail_contribution_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(
            template_name, context, request=request
        )  # Rendre le formulaire en cas de requête GET
    return JsonResponse(data)


def detail_contribution_detail(request, pk):
    detail_contribution = get_object_or_404(DetailContribution, pk=pk)
    return render(request, "detail_contribution_detail.html", {"detail_contribution": detail_contribution})
