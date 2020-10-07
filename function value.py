from sympy import *

print("제곱의 형태는 '**'로 표현하고, 곱하기를 생략하지 말아주십시오.")
a = input("x를 변수로 하여 함수 식을 입력해 주십시오. : ")
x = Symbol('x')
b = input("대입할 x 값을 입력해 주십시오. : ")
a = simplify(a)
expr = a.subs(x,b)
print(expr)