list1 = ["admin@gmail.com", "admin1@gmail.com"]
list2 = ["admin2@gmail.com", "admin1@gmail.com"]
list3 = ["admin@gmail.com", "admin3@gmail.com"]

list4 = []
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)
print(list4)
print(set(list4))
