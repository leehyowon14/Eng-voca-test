voca = open("..\\voca.txt", "wt", encoding='UTF8')
print("vaca.txt(단어장) 파일 설정\n")
amount = int(input('단어의 갯수를 적어주세요. : '))

print("주의!! 단어뜻이 여러개인경우','로 나누어주세요")
print("주의!! 단어뜻이 여러개인경우','로 나누어주세요")
print("주의!! 단어뜻이 여러개인경우','로 나누어주세요")

for i in range(1, amount+1):
    voca.write('{}.\n'.format(i))
voca.close()
print('voca.txt 세팅 완료')