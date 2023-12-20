import random
import time

from django.http import HttpResponse
from django.core.cache import caches

RamCache = caches["default"]
DatabaseCache = caches["special"]


def get_cache(key: str, query: callable = lambda: any, timeout: int = 10, cache: any = RamCache) -> any:
    data = cache.get(key)
    if data is None:
        data = query()
        cache.set(key, data, timeout)
    return data


def index(request):
    # 6x speed
    # # взять
    # iin = RamCache.get("iin")
    # print(iin)
    # # положить
    # new_iin = random.randint(1, 1000000)
    # RamCache.set("iin", new_iin, 10)

    def compute_user() -> int:
        time.sleep(2.0)
        val = random.randint(1, 1000000)
        return val

    iin = get_cache(key="index", query=compute_user, timeout=20, cache=RamCache)
    # iin = get_cache(key="index", query=compute_user, timeout=20, cache=DatabaseCache)
    return HttpResponse(f"Привет {iin}")
