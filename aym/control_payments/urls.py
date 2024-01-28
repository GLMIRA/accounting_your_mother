from django.urls import path

from . import views

app_name = "control_payments"
urlpatterns = [
    path("", views.index, name="index"),
    path("resident/all", views.resident_all, name="resident/all"),
    path("resident/get/<int:resident_id>", views.resident_get, name="resident/get"),
    path("resident/input", views.resident_input, name="resident/input"),
    path(
        "resident/update/<int:resident_id>",
        views.resident_update,
        name="resident/update",
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
