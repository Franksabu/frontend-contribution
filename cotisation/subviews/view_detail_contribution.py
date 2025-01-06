from django.http import JsonResponse
from django.shortcuts import render, redirect
from cotisation.models import DetailContribution, Contribution
from django.shortcuts import get_object_or_404
from cotisation.forms import DetailContributionForm
from django.template.loader import render_to_string
from parametrage.operations import OperationsHelpers
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def detail_contribution_list(request, id):
    contribution = get_object_or_404(Contribution, id=id)
    detail_contribution = DetailContribution.objects.filter(
        contribution_id=contribution.id
    )
    context = {"contribution": contribution, "detail_contribution": detail_contribution}
    return render(request, "detail_contribution_list.html", context)


@login_required
def detail_contribution_create(request, id):
    form = (
        DetailContributionForm(request.POST)
        if request.method == "POST"
        else DetailContributionForm()
    )
    return save_detail_contribution_form(
        request, form, "detail_contribution_create.html", "create", id
    )


def save_detail_contribution_form(request, form, template_name, action, id):
    contribution = get_object_or_404(Contribution, id=id)
    detail_contribution = DetailContribution.objects.filter(contribution=contribution)
    form = DetailContributionForm(contributionId=id)
    data = {}
    if request.method == "POST":
        form = DetailContributionForm(request.POST, contributionId=id)
        if not form.is_valid():
            data["form_is_valid"] = False
        else:
            res = OperationsHelpers.execute_action(request, action, form)
            if len(res) == 0:
                data["form_is_valid"] = True
                data["html_content_list"] = render_to_string(
                    "detail_contribution_list.html", {"contribution": contribution, "detail_contribution": detail_contribution}
                )
                data["url_redirect"] = reverse("detail_contribution_list", args=[id])
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {
            "form": form,
            "detail_contribution": detail_contribution,
            "contribution": contribution,
        }
        data["html_form"] = render_to_string(
            template_name, context, request=request
        )  # Rendre le formulaire en cas de requête GET
    return JsonResponse(data)


@login_required
def detail_contribution_update(request, contri_id, id):
    contribution = get_object_or_404(Contribution, id=contri_id)
    detail_contribution = get_object_or_404(
        DetailContribution, id=id, contribution=contribution
    )

    if request.method == "POST":
        form = DetailContributionForm(request.POST, instance=detail_contribution)
        if form.is_valid():
            detail_contribution = form.save(commit=False)  # Ne sauvegardez pas encore
            detail_contribution.user_valide = request.user  # Assignez l'utilisateur
            detail_contribution.save()
            if request.user.is_authenticated:
                detail_contribution.user_valide = request.user
            else:
                # Gérer le cas où l'utilisateur n'est pas authentifié
                return JsonResponse(
                    {
                        "form_is_valid": False,
                        "form_error": "Vous devez être connecté pour effectuer cette action.",
                    }
                )
            success_url = f"/cotisation/detail_contributions/list/{contribution.id}/"
            return JsonResponse(
                {
                    "form_is_valid": True,
                    "url_redirect": success_url,
                }
            )
        else:
            return JsonResponse(
                {
                    "form_is_valid": False,
                    "form_error": "Le formulaire contient des erreurs.",
                }
            )

    else:
        form = DetailContributionForm(instance=detail_contribution)

    # Rendre le formulaire en HTML partiel
    html_form = render_to_string(
        "detail_contribution_update.html",
        {
            "form": form,
            "detail_contribution": detail_contribution,
            "contribution": contribution,
        },
        request=request,
    )
    return JsonResponse({"html_form": html_form})


@login_required
def detail_contribution_delete(request, contri_id, id):
    contribution = get_object_or_404(Contribution, id=contri_id)
    detail_contribution = get_object_or_404(
        DetailContribution, id=id, contribution=contribution
    )

    if request.method == "POST":
        detail_contribution.delete()
        return JsonResponse(
            {
                "success": True,
                "url_redirect": reverse("detail_contribution_list", args=[contri_id]),
            }
        )
    return JsonResponse({"success": False})


# def detail_contribution_detail(request, pk):
#     detail_contribution = get_object_or_404(DetailContribution, pk=pk)
#     return render(request, "detail_contribution_detail.html", {"detail_contribution": detail_contribution})
