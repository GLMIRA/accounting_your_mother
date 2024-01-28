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
    path("debt_type/input", views.debt_type_input, name="debt_type/input"),
    path("debt_type/all", views.debt_type_all, name="debt_type/all"),
    path(
        "debt_type/update/<str:debt_type_id>",
        views.debt_type_update,
        name="debt_typ/update",
    ),
    path("debt/input", views.debt_input, name="debt/input"),
    path("debt/all", views.debt_input, name="debt_all"),
]
