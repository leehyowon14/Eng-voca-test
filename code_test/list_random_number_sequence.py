import random

def isin(t,a):
    t_len = int(len(t))
    if t_len == 0:
        return False
    for i in range(0, t_len):
        if t[i] == a:
            return True
    return False

num = 30
list = []
while len(list) < num:
    random_num = random.randrange(1, num + 1)
    if isin(list, random_num) == False:
        list.append(random_num)

print(list)
