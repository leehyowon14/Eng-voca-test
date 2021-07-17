list_a = [3, 2, 5, 1, 4]
list_b = [1, 2, 3, 4, 5]

for i in range(0, len(list_a)):
    print(list_a[i])
    for o in range(0, len(list_b)):
        if list_a[i] == list_b[o]:
            print(list_b[o])