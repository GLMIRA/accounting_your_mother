from django.urls import path

from . import views

app_name = "control_payments"
urlpatterns = [
    path("", views.index, name="index"),
    ## USER PROFILE
    path("user_profile/all", views.user_profile_all, name="user_profile/all"),
    path("user_profile/input", views.user_profile_input, name="user_profile/input"),
    path(
        "user_profile/update/<int:user_id>",
        views.user_profile_update,
        name="user_profile/update",
    ),
]
