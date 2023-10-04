data1 = ((1, "Bogdan"), (2, "Roman"))
data2 = {1: "Bogdan", 2: "Roman"}

dict1 = {}
for i in data1:
    dict1[i[0]] = i[1]
print(dict1)  # {1: 'Bogdan', 2: 'Roman'}




def check(s1):
    return s1 == s1[::-1]


t1 = "121"
t2 = "123"
print(check(t1))
print(check(t2))
