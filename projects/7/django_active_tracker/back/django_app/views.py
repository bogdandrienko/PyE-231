import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def api(request):
    return JsonResponse(data={"success": "ok"}, status=200)


@csrf_exempt
def communicator(request):
    if request.method != "POST":
        return JsonResponse(data={"error": "Method not supported"}, status=500)
    # print(request.body)
    body: bytes = request.body
    data = json.loads(body)
    messages = data.get('messages', [])
    # print(type(messages), messages)
    bot_token = "6589285143:AAF_jOEz0-eFpX3MeBSc49aK9Zw3W7NQbtc"
    user_list = "1289279426,1289279426"
    text = "Внимание!\n"
    is_alarm = False
    for i in messages:
        # print(type(i), i)
        if i.get("speed", 0) <= 0:
            is_alarm = True
            text += f"{i.get('serial_id', 'неизвестное')}, "
    if is_alarm:
        for chat_id in [x.strip() for x in user_list.split(",")]:
            requests.post(url=f"https://api.telegram.org/bot{bot_token}/sendMessage", json={"chat_id": chat_id, "text": text[:-2]})
    return JsonResponse(data={"success": "ok"}, status=201)
