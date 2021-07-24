#Made by Lee hyowon
#Work In Progress(WIP)

import random
from config import Config

def isin(t,a):
    t_len = int(len(t))
    if t_len == 0:
        return False
    for i in range(0, t_len):
        if t[i] == a:
            return True
    return False

test_type = Config.voca_random_test #가독성을 높이기 위해 변수로 만듦.``
show_answer = Config.show_correct_answer
voca = open("voca.txt", "r", encoding='UTF8').readlines()
amount = len(voca)
answer_count = amount
voca_list = []

if amount == 0:
    print('err:amount값이 0입니다. Voca.txt를 확인해주세요')
    exit()
for i in range(0, amount):
    num = int(voca[i].split('\n')[0].split('.')[0])
    word = voca[i].split('\n')[0].split('.')[1].split(':')[0]
    mean_list = voca[i].split('\n')[0].split('.')[1].split(':')[1].split(",")

    voca_list.append([num, word, mean_list])
    #print(voca_list)

print(test_type)
print(amount)
print(voca_list)

if test_type == True:
    #랜덤시험
    random_num_list = []#random order create(code_test-list_random_number_sequence.py)
    while len(random_num_list) < amount:
        random_num = random.randrange(1, amount + 1)
        if isin(random_num_list, random_num) == False:
            random_num_list.append(random_num)
    print(random_num_list)
    for i in range(0, len(random_num_list)):
        for o in range(0, len(voca_list)):
            if random_num_list[i] == voca_list[o][0]:
                count = 0
                print('단어뜻이 여러개인 경우, ","를 이용하여 나누어 주세요')
                answer = input(str(i + 1) + " . " + str(voca_list[o][1]) + "의 뜻을 적으시오 : ").split(",")
                #list_b = answer
                #New bug!(단어뜻이 여러개일때 가끔씩 오답처리됨.)
                for x in range(0, len(voca_list[o][2])):#answer_check(code_test-list_check.py[improve ver.])
                    word_mean = voca_list[o][2][x]
                    for y in range(0, len(answer)):
                        if type(answer) == list:
                            answer_mean = answer[y].strip()
                        else:
                            answer_mean = answer
                        if word_mean == answer_mean:
                            count += 1

                if count == len(voca_list[i][2]):
                    print('정답입니다.')
                else:
                    print('오답입니다.')
                    if show_answer:
                        print('정답: ' + str(voca_list[o][2]))
                    answer_count -= 1
                
                break


    

#New bug! 단어 뜻이 한개일 경우 오답으로 표시됨.(fixed 2021/06/08 18:03)
elif test_type == False: #complete(Now Cleaning code...)
    #순서대로
    for i in range(0, amount):
        count = 0
        print('단어뜻이 여러개인 경우, ","를 이용하여 나누어 주세요')
        answer = input(str(voca_list[i][0]) + " . " + str(voca_list[i][1]) + "의 뜻을 적으시오 : ").split(",")
        #list_b = answer
        for x in range(0, len(voca_list[i][2])):#answer_check(code_test-list_check.py[improve ver.])
            word_mean = voca_list[i][2][x]
            for y in range(0, len(answer)):
                if type(answer) == list:
                    answer_mean = answer[y].strip()
                else:
                    answer_mean = answer
                if word_mean == answer_mean:
                    count += 1

        if count == len(voca_list[i][2]):
            print('정답입니다.')
        else:
            if show_answer:
                print('정답: ' + str(voca_list[i][2]))
            print('오답입니다.')
            answer_count -= 1

else:
    print("'config'폴더안 'Config.py'파일을 확인해 주세요")
print('점수 : ' + str(answer_count) + '/' + str(amount))