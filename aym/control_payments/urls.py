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
]
