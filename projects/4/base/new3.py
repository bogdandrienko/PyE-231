import time
start = time.perf_counter()
time.sleep(3.0)  # блокирующий код
print(f"elapsed time: ", round(time.perf_counter() - start, 7))
