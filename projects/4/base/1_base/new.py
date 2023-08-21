from datetime import datetime, timedelta
import sys

var1 = "1692627385"                 # str  == 59 bytes
var2 = "2023-08-21T14:15:41+00:00"  # str  == 74 bytes
var3 = 1692627385                   # int  == 32 bytes
# 1629533741

print(sys.getsizeof(var1))
print(sys.getsizeof(var2))
print(sys.getsizeof(var3))

print(datetime.now() + timedelta(minutes=10, hours=2))

# форматирование даты и времени
now2 = datetime.now().strftime("%A %B %m-%d-%y, %H:%M:%S.%f")  # Tuesday December 12-06-22, 19:39:24.135024 <class 'str'>
now3 = datetime.now().strftime("%H:%M")  # 20:31 <class 'str'>
print(now2, type(now2))
print(now3, type(now3))
