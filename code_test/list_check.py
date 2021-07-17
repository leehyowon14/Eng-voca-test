count = 0
list_a = [1, 2, 3, 4]
list_b = [1, 3, 2, 4]

for x in range(0, len(list_a)):
    a = list_a[x]
    for y in range(0, len(list_b)):
        b = list_b[y]
        if a == b:
            count += 1
            print(count)
            break
if count == len(list_a):
    print('right')
else:
    print('wrong')
