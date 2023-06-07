# Практика: вытащить из архива папку с файлами и кодом очистить
# её от “мусорных”(junk.json) файлов.

import os
path = "for_clean\\temp"

for root, dirs, files in os.walk(path, topdown=True):
    # print(root, dirs, files)
    for name in files:
        p = os.path.join(root, name)
        if name == "junk.json":
            try:
                print("к удалению: ", p)
                os.remove(p)
            except Exception as error:
                print(error)
        else:
            print("не удалять: ", p)
