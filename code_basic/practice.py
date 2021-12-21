#int 정수
#str (string) 문자
#flowt 둥둥둥 떠다닌다는 뜻 (소수점 실수)


'''
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

print(5>10) 
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

animal="고양이"
name="해피"
age=3
hobby="낮잠"
isAdult=age>=3

print("우리집" + animal + "의 이름은" + name + "에요~")
hobby = "공놀이"
print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요.")
print(name, "는", str(age), "살이며,", hobby, "을 아주 좋아해요.")
print(name + "는 어른일까요?" + str(isAdult))
'''

'''
이렇게 하면
여러 문장이
주석 처리가 됩니다.
'''

# '#'는 한 문장을 주석 처리 합니다.

'''
name="사당"
print(name + "행 열차가 들어오고 있습니다.")
name="신도림"
print(name + "행 열차가 들어오고 있습니다.")
name="서현"
print(name + "행 열차가 들어오고 있습니다.")

print(5+50)
print(4-52)
print(3*9)
print(8/2)

print(2**3) #2^3 (2의 3승)
print(5%3) #나눴을 때 나머지 구하기
print(10%3) #나머지 구하기
print(5//3) #(정수로) 몫 구하기
print(10/3) #(소수점까지 정확한) 몫 구하기

print(5>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3) #==는 같다는 뜻
print(4==2)
print(3+4==7)

print(1 !=3) #!=는 같지 않다는 뜻
print(not(1 !=3)) #not 때문에 같지 않지 않아요

print((3>0) and (3<5)) #and는 양쪽 모두 참이어야 참으로 나옴
print((3>0) & (3<5))
print((3>0) or (3>5)) #or는 한쪽만 참이어도 참으로 나옴
print((3>0) | (3>5))

print(5>4>3)
print(5>4>7)
'''

'''
print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number + 2 #오른쪽에서 왼쪽으로 읽힘. 그래서 number+2가 number로 바뀜
print(number)
number += 2 # += 위에걸 짧게 쓰면 이렇게 쓸 수 있음. (넘버를 2 더 많은 수로 엎어써 바꾸겠다.)
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2  # 위와 같은 방법으로 응용
print(number)
number %= 3
print(number)
number %= 5  # 5라는 수로 나눴을 때 남은 수가 넘버가 됩니다.
print(number)
'''

'''
print(abs(-5)) #절댓값
print(pow(4,2)) #승
print(max(5,12)) #큰 수 고르기
print(min(5,12)) #작은 수 고르기
print(round(3.14)) #반올림
print(round(4.99)) #반올림
'''

'''
from math import *   #math(모듈) 안에 들어가 있는 코드를 불러다 올 때 쓰는 것들 ('*' 은 모든 것이라는 뜻); import math 라고만 쓸 수도 있음
print(floor(4.99))  #버림 (소수자 뒤 숫자는 다 버려버린다)
print(ceil(3.14))   #무조건 일의 자리까지 올림 
print(sqrt(16))     #루트

#import math   #이렇게 쓸 수도 있는데, 그러면 쓸 때마다 math. 써야함
#math. 

from random import *
print(random())              # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)         # 0,0 ~ 10.0 미만의 임의의 값 생성
print((random() * 10) + 1)   # 1 ~ 10.0 이하(왜냐하면 하나씩 올라왔기 때문)의 임의의 값 생성
print(int(random() * 10)     # 0 ~ 10 이하의 임의의 값 생성 (정수, 소수점 허용 안함)

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성; random range 라는 뜻
print(randint(1,45))   # 1 ~ 45 이하의 임의의 값 생성
'''

'''
sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
# " " 안에서의 ""은 줄바꿈 문자이다.
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
'''

'''
#슬라이싱
jumin = 123456-7890123
'''

print(2+3)