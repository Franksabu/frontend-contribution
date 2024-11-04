from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Assistance
from .forms import AssistanceForm
from parametrage.operations import OperationsHelpers
from django.urls import reverse


def assistance_list(request):
    context = {
        "assistances": Assistance.objects.all(),
    }
    return render(request, "assistance_list.html", context)


def assistance_create(request):
    form = AssistanceForm(request.POST) if request.method == "POST" else AssistanceForm()
    return save_assistance_form(request, form, "assistance_create.html", "create")


def save_assistance_form(request, form, template_name, action):
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
                data["html_content_list"] = render_to_string("assistance_list.html")
                data["url_redirect"] = reverse("assistance_list")
            else:
                data["form_is_valid"] = False
                data["form_error"] = res

    else:
        context = {"form": form}
        data["html_form"] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def assistance_detail(request, pk):
    assistance = get_object_or_404(Assistance, pk=pk)
    return render(request, "assistance_detail.html", {"assistances": assistance})
