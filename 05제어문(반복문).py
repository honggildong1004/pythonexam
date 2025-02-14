# -*- coding: utf-8 -*-
"""05제어문(반복문).ipynb"""

fruits = ["사과", "바나나", "포도"]

for i in fruits:
    print(i)



#형식 : for 변수 in range(시작,끝,간격)
#0부터 4까지 출력
for i in range(5):
    print("0부터 4까지 출력%s" %i)

#1부터 10까지 2씩 증가 출력
for i in range(1,11, 2):
    print("1부터 10까지 출력%s" %i)

#형식 while 조건

#0부터 4까지 출력
count = 0
while count <5:
    print(count)
    count +=1

#반복문제어
#break문:방복문을 즉시 종료
for i in range(10):
    if i == 5:
        break
    print(i)

#continue 현재 반복을 건너뛰고 다음 반복을 실행
for i in range(5):
    if i == 2:
        continue
    print(i)

#중첩반복문
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

#리스트 컴프리헨션
#형식 for 변수 in 시퀀스
numbers = [i for i in range(5)]             #0부터 4까지 생성
print(numbers)

numbers2 = [i for i in range(5) if i%2==0] #0부터 4까지 짝수만 생성
print(numbers2)

numbers3 = [i**2 for i in range(5)]        #0부터 4까지 제곱 생성
print(numbers3)

