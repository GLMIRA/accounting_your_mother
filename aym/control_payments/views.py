from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import (
  UserProfile,
  DebtType,
  Debts,
)
from .forms import (
    UserProfileFormUpdate,
    UserProfileFormInput,
)
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "control_payments/index.html")


### USER PROFILE
@login_required(login_url="/accounts/login/")
def user_profile_all(request):
    user_profile_list = UserProfile.objects.all().order_by("user__username")
    template = loader.get_template(
        "control_payments/user_profile/user_profile_all.html"
    )
    context = {
        "user_profile_list": user_profile_list,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/accounts/login/")
def user_profile_input(request: HttpRequest):
    if request.method == "POST":
        form = UserProfileFormInput(request.POST)
        if form.is_valid():
            user_profile = UserProfile()
            user_profile.user = form.cleaned_data["user"]
            user_profile.cpf = form.cleaned_data["cpf"]
            user_profile.birth_date = form.cleaned_data["birth_date"]
            user_profile.discord_nickname = form.cleaned_data["discord_nickname"]
            user_profile.save()
            return HttpResponse("User profile save!")
    else:
        form = UserProfileFormInput()
    return render(
        request=request,
        template_name="control_payments/user_profile/user_profile_input.html",
        context={"form": form},
    )


@login_required(login_url="/accounts/login/")
def user_profile_update(request: HttpRequest, user_id: int):
    user_profile = UserProfile.objects.get(pk=user_id)
    if request.method == "POST":
        form = UserProfileFormUpdate(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile.cpf = form.cleaned_data["cpf"]
            user_profile.birth_date = form.cleaned_data["birth_date"]
            user_profile.discord_nickname = form.cleaned_data["discord_nickname"]
            user_profile.save()
            return HttpResponse("User profile updated!")
    else:
        form = UserProfileFormUpdate(instance=user_profile)
    return render(
        request=request,
        template_name="control_payments/user_profile/user_profile_update.html",
        context={"user": user_profile.user, "form": form},
    )

  
def debt_type_input(request: HttpRequest):
    if request.method == "GET":
        return render(request, "control_payments/debt_type/debt_type_input.html")
    debt_type = DebtType(
        name=request.POST["name"], description=request.POST["description_debt_typ"]
    )
    debt_type.save()
    return HttpResponse("new type of debt successfully saved")


def debt_type_all(request: HttpResponse):
    debt_type_list = DebtType.objects.all().order_by("name")
    template = loader.get_template("control_payments/debt_type/debt_type_all.html")
    context = {"debt_type_list": debt_type_list}
    return HttpResponse(template.render(context, request))


def debt_type_update(request: HttpRequest, debt_type_id: DebtType):
    debt_type = DebtType.objects.get(pk=debt_type_id)
    if request.method == "GET":
        context = {
            "debt_type": debt_type,
        }
        return render(
            request=request,
            context=context,
            template_name="control_payments/debt_type/debt_type_update.html",
        )
    debt_type.name = request.POST["name"]
    debt_type.description = request.POST["debt_type_description"]
    debt_type.save()
    return HttpResponse("debt_type updated!!!")


def debt_input(request: HttpRequest):
    if request.method == "GET":
        return render(request, "control_payments/debt/debt_input.html")
    debt = Debts(
        debt_type=DebtType.objects.get(name=request.POST["debt_type"]),
        due_date=request.POST["due_date"],
        debt_value=request.POST["value"],
    )
    debt.save()
    return HttpResponse("new debt save")
