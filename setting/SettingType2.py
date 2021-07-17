voca = open("..\\voca.txt", "wt", encoding='UTF8')
amount = int(input('단어의 갯수를 적어주세요. : '))

print("단어뜻이 여러개인경우','로 나누어주세요")
for i in range(1, amount+1):
    word = input('단어를 적어주세요: ')
    mean = input('뜻을 적어주세요: ')
    voca.write('{}.{}:{}\n'.format(i, word, mean))
voca.close()
print('voca.txt 세팅 완료')