from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Detail_cotisation
from .forms import Detail_cotisationForm
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def detail_cotisation_list(request):
    detail_cotisations = Detail_cotisation.objects.all()
    for detail in detail_cotisations:
        cotisa = detail.cotisation_id.montant_min
        montan = detail.montant_paye if detail.montant_paye is not None else 0
        if cotisa < montan:
            detail.solde = 0
        else:
            detail.solde = cotisa - montan
    context = {"detail_cotisations": detail_cotisations}
    return render(request, "detail_cotisation_list.html", context)


def detail_cotisation_create(request):
    form = Detail_cotisationForm(request.POST) if request.method == "POST" else Detail_cotisationForm()
    return save_detail_form(request, form, "detail_cotisation_create.html", "create")


def save_detail_form(request, form, template_name, action):
    data = {}
    if request.method == "POST":
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)

            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string(
                    "detail_cotisation_list.html"
                )
                data["url_redirect"] = reverse("detail_cotisation_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def detail_cotisation_detail(request, pk):
    detail = get_object_or_404(Detail_cotisation, pk=pk)
    cotisa = detail.cotisation_id.montant_min
    montan = detail.montant_paye if detail.montant_paye is not None else 0
    if cotisa < montan:
        detail.solde = 0
    else:
        detail.solde = cotisa - montan
    return render(request, "detail_cotisation_detail.html", {"detail": detail})
