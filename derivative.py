from sympy import *

a = input("f(x) 식을 입력하여 주십시오. : ")
x = Symbol('x')
a = sympify(a)

b = Derivative(a,x)
c = b.doit()

print("--------------------------")
print("f(x) 함수를 미분한 결과입니다.")
print(c)