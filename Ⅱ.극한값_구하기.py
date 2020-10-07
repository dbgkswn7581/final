from sympy import *

a1 = input("좌극한을 구할 식을 x에 대하여 입력하여 주십시오. : ")
a2 = input("우극한을 구할 식을 x에 대하여 입력하여 주십시오. : ")
x = Symbol('x')
a1 = simplify(a1)
a2 = simplify(a2)
c = input("두 함수를 어떤 수로 한없이 가까워지게 할 것인지 입력하여 주십시오. : ")
b = Limit(a2, x, c, dir='+').doit()
d = Limit(a1, x, c, dir='-').doit()

print("좌극한 : ", end='')
print(d)

print("우극한 : ", end='')
print(b)

# Limit 함수를 이용하여 극한값을 구할 수 있으며, dir='+' 또는 dir='-'을 이용하여 우극한 또는 좌극한으로 나눌 수 있고, doit 함수로 극한값을 계산한다.
