import datetime
from django.http import HttpRequest, HttpResponse
from django_app import utils


class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # print(utils.Datetime.get_current_datetime_str())
        # print(datetime.datetime.now(), request.path)
        response: HttpResponse = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response
