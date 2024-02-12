import datetime
import random
import time
import requests

while True:
    try:
        messages = [{"id": 12354, "serial_id": f"970835" + f"{random.randint(0, 135135)}", "x": 86464.534, "y": 74564.534, "datetime": str(datetime.datetime.now()),
                     "speed": random.randint(0, 1)} for x in range(1, 5)]
        # host, port = "127.0.0.1", 8000
        host, port = "194.67.82.8", 80
        response = requests.post(f"http://{host}:{port}/api/communicator/", json={"messages": messages})
        print(f"{datetime.datetime.now()} success: ", response.status_code)
    except Exception as error:
        print(f"{datetime.datetime.now()} error: ", error)
    time.sleep(5)
