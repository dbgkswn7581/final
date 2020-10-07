from sympy import *

a = input("평균변화율을 구할 식을 x에 대하여 입력하여 주십시오. : ")
a = simplify(a)
x = Symbol('x')

b,c = map(int, input("x의 값이 a에서 b까지 변한다고 할 때, a와 b의 값을 공백을 두고 입력해 주십시오. : ").split())

del_x = c-b
del_y = a.subs(x,c) - a.subs(x,b)

aver = del_y / del_x

print("함수 y=f(x)에서 x의 값이 ",end='')
print(b,end='')
print("에서 ",end='')
print(c,end='')
print("까지 변할 때의 평균변화율은 ",end='')
print(aver,end='')
print("입니다.")