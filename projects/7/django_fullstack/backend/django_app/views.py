import time
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import requests


@api_view(http_method_names=["GET"])
def api_users(request: Request):
    print("api_users", request.query_params)

    return Response(data={"success": "ok"}, status=200)


@api_view(http_method_names=["POST"])
def api_user_credit_check(request):
    print("api_user_credit_check", request.data)

    summ = int(request.data["summ"])
    date_planning = int(request.data["date_planning"])

    time.sleep(1.5)

    # kgd/egov
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        result = True
    else:
        result = False

    _data = {"total_summ": summ + (summ * 20 / 100 * date_planning / 12), "result": result}

    return Response(data={"success": _data}, status=200)
