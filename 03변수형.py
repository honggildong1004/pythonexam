# -*- coding: utf-8 -*-
"""03변수형.ipynb"""

#정수형 변수 선언
a = 10
b = -15

sum = a + b       #사칙연산 덧셈

print("Sum:", sum)

#실수형 변수 선언
pi = 3.14159
지름 = 5.0

둘레 = pi * 지름  # 원의 둘레 계산

print("원의 둘레:", 둘레)
print("원의 둘레: %.2f" %둘레)

#boolean 변수선언
is_raining = True
is_sunny = False

#조건문과 함꼐 사용
if is_raining:
    print("우산을 가져가세요")
else:
    print("날씨가 좋습니다.")

#문자열형 변수 선언
greeting = "안녕하세요"
name = "홍길동"

message = greeting + ", " + name + "님" #문자열 연결
print(message)

#정수형에서 실수형으로 변환(float명렁어사용)
int_num = 10
float_num = float(int_num)

print(int_num)
print(float_num)

#실수형에서 정수형으로 변환(int명렁어사용)
float_num = 3.14
int_num = int(float_num)

print(float_num)
print(int_num)

#문자열에서 정수형으로(int명령어 사용)
str_num = "123"
int_num = int(str_num)

#정수형에서 문자열으로(str명령어 사용)
int2_num = "456"
str_num = str(int2_num)

print(int_num)
print(int2_num)
print(str_num)
