from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import UserProfile
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
