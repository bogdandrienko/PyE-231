from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_app import utils, models, serializers


@utils.Decorators.constr_dec_logger(is_class=False)
def index_http(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


@utils.Decorators.constr_dec_logger(is_class=False)
@utils.Decorators.dec_error_handle
def index_json(request):
    print(1 / 0)
    return JsonResponse(data={"response": "This is a Index Page"}, safe=False)


class Home(View):  # Mixins
    @utils.Decorators.constr_dec_logger(is_class=True)
    def get(self, request, *args, **kwargs):
        _contacts = models.Contact.objects.filter(is_completed=True)
        context = {"contacts": _contacts}
        return render(request, "home.html", context=context)

    def post(self, request, *args, **kwargs):
        models.Contact.objects.create(
            username=request.POST["username"],
            position=None,
            number=request.POST["number"],
            description=request.POST.get("description", ""),
        )
        return redirect(reverse("home"))


def contact_delete(request, contact_id: str):
    models.Contact.objects.get(id=int(contact_id)).delete()
    return redirect(reverse("home"))


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def get_contacts(request):
    if request.method == "GET":
        _contacts = models.Contact.objects.filter(is_completed=True)
        _contacts_json = serializers.ContactAllSerializer(_contacts, many=True).data
        return Response(data={"data": _contacts_json}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print("request.data: ", request.data)
        return Response(data={"message": "успешно создано"}, status=status.HTTP_200_OK)
