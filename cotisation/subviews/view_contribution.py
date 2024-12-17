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
        "contributions": Contribution.objects.all(),
    }
    return render(request, "contribution_list.html", context)


def contribution_create(request):
    form = ContributionForm(request.POST) if request.method == "POST" else ContributionForm()
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
            print(form)
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


def contributions_update(request, id):
    contribution = get_object_or_404(Contribution, id=id)
    
    if request.method == 'POST':
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            form.save()
            return redirect('contribution_list')
    else:
        form = ContributionForm(instance=contribution)

    return render(request, 'contribution_update.html', {'form': form, 'contribution': contribution})


#  @login_required
def contribution_delete(request, id):
    contribution = get_object_or_404(Contribution, id=id)

    if request.method == "POST":
        contribution.delete()
        return JsonResponse({
            "success": True,
            "url_redirect": reverse("contribution_list")  # Redirection après suppression
        })
    return JsonResponse({"success": False})


def contribution_detail(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    return render(request, "contribution_detail.html", {"contribution": contribution})
