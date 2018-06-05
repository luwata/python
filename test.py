list = [4, 8, 415, 1, 25, 75, 6]

flag = true

limit = len(list)

while flag:
    for i in range(0, limit-1):
        flag = False
        if (list[i] > list[i+1]):
            flag = false
            if (list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1)
                flag = true
        limit = limit - 1
    print(list)





