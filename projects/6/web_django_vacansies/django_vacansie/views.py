from django.shortcuts import render, redirect
from django.urls import reverse

from django_vacansie import models
from django_app import utils


def vacansie_list(request):
    _data = lambda: utils.native_paginate(request, models.Vacansie.objects.all().filter(is_active=True), 9)  # orm + pagination
    vacs = utils.get_cache(f"vacansie_list {request.GET.get('page', 1)}", lambda: _data(), timeout=2)  # cache
    return render(request, "vacansie/vacansie_list.html", context={"page_obj": vacs})


def vacansie_detail(request, vac_id: str):
    _data = lambda: models.Vacansie.objects.get(id=int(vac_id))  # orm
    vac = utils.get_cache(f"vacansie_detail {vac_id}", lambda: _data(), timeout=2)  # cache
    return render(request, "vacansie/vacansie_detail.html", context={"i": vac})


def vacansie_create(request):
    if request.method == "GET":
        return render(request, "vacansie/vacansie_create.html")
    elif request.method == "POST":
        title = request.POST["title"]
        description = request.POST.get("description", "")
        salary = int(request.POST.get("salary", "0"))
        models.Vacansie.objects.create(title=title, description=description, salary=salary, is_active=True)
        return redirect(reverse("vacansie_list"))
