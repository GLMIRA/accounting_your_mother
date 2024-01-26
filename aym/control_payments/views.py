from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Resident, DebtType


def index(request):
    return HttpResponse("Bem vindo ao controle de pagamentos!")


def resident_all(request):
    resident_list = Resident.objects.all().order_by("name")
    template = loader.get_template("control_payments/resident/resident_all.html")
    context = {
        "resident_list": resident_list,
    }
    return HttpResponse(template.render(context, request))


def resident_get(request, resident_id):
    resident = Resident.objects.get(pk=resident_id)
    # TODO: fazer o template de mostrar resident
    # template = loader.get_template("control_payments/resident_id.html")
    # context = {
    #     "resident": resident,
    # }
    result = f"Resident: {resident.name} - {resident.email}"
    return HttpResponse(result)


def resident_input(request: HttpRequest):
    if request.method == "GET":
        return render(request, "control_payments/resident/resident_input.html")
    resident = Resident(
        cpf=request.POST["cpf"],
        name=request.POST["name"],
        email=request.POST["email"],
        age=request.POST["age"],
        discord_nickname=request.POST["discord_nickname"],
    )
    resident.save()
    return HttpResponse("Resident saved!")


def resident_update(request: HttpRequest, resident_id):
    resident = Resident.objects.get(pk=resident_id)
    if request.method == "GET":
        context = {
            "resident": resident,
        }
        return render(
            request=request,
            context=context,
            template_name="control_payments/resident/resident_update.html",
        )
    resident.name = request.POST["name"]
    resident.email = request.POST["email"]
    resident.age = request.POST["age"]
    resident.discord_nickname = request.POST["discord_nickname"]
    resident.save()
    return HttpResponse("Resident updated!")


def debt_type_input(request: HttpRequest):
    if request.method == "GET":
        return render(request, "control_payments/debt_type/debt_type_input.html")
    debt_type = DebtType(
        name=request.POST["name"], description=request.POST["description"]
    )
    debt_type.save()
    return HttpResponse("new type of debt successfully saved")


def debt_type_all(request: HttpResponse):
    debt_type_list = DebtType.objects.all().order_by("name")
    template = loader.get_template("control_payments/debt_type/debt_type_all.html")
    context = {"debt_type_list": debt_type_list}
    return HttpResponse(template.render(context, request))
