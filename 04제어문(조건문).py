# -*- coding: utf-8 -*-
"""04제어문(조건문).ipynb"""

#기본조건문 1.1 조건문은 특정 조건에 따라 코드블록을 실행
age = 18
if age >= 18:
    print("성인입니다") #age가 18세 이상이면 실행



#1.2 성적에 따른 학점계산
score = int(input("성적을 입력하세요"))

# 학점계산
if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"당신의 학점은{grade}입니다.")

#2. 중첩조건문
#조건문안에 다른 조건문을 넣을 수 있습니다.
age = 20
is_student = True

if age >= 18:
    if is_student:
        print("학생입니다.") #이 코드가 실행
    else:
        print("성인입니다.")
else:
    print("미성년입니다.")

#3. in 키워드를 사용한 조건문
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("바나나가 있습니다.")

if "orange" not in fruits:
    print("오랜지는 없습니다.")

#4. 조건연산자
#4.1 and(모든 조건이 참이어야 True)
age = 20
money = 10000

if age>=18 and money >=5000:
    print("1놀이공원 입장이 가능합니다.")

#4.2 or(조건중에 하나라도 참이면 True)
age = 15
money = 10000

if age>=18 or money >=5000:         #나이가 조건에 충족되지 않아도 pass
    print("2놀이공원 입장이 가능합니다.")

#4.3 not (조건모두 거짓이어야 True)
fruits = ["apple", "banana", "cherry"]

if not "orange" in fruits:          #True
    print("3오렌지가 없습니다.")
else:
    print("3오렌지가 있습니다.")

#5. 조건문 한 줄로 쓰기(if 표현식)
#조건이 참일때 값 if 조건 else 조건이 거짓일 때 값

score = 75
result = "합격" if score >= 60 else "불합격"
print(result)

#6. pass키워드(아무 동작도 안함)
#pass는 빈 블록 만들때
age = 20
if age < 18:
    pass #나중에 구현(만들)할 부분
else:
    print("성인입니다")
