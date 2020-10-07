from sympy import *

print("변수는 x로 입력하여 주시고, 식에 x 이외의 문자를 입력해도 무관하나, x 이외의 문자는 1개만 입력하여 주십시오.")
a1 = input("좌극한을 구할 식을 x에 대하여 입력하여 주십시오. : ")
a2 = input("우극한을 구할 식을 x에 대하여 입력하여 주십시오. : ")
a3 = input("함숫값을 구할 식을 x에 대하여 입력하여 주십시오. : ")
x = Symbol('x')

def isNum(k):
    try :
        float(k)
        return 'T'
    except ValueError:
        return 'F'
    except TypeError:
        return 'F'

def pfind(fx):
    if fx.find("sqrt") > 0:
        fx = simplify(fx)
        fx = radsimp(fx)
    else :
        fx = simplify(fx)

pfind(a1)
pfind(a2)
a3 = simplify(a3)

c = input("두 함수를 어떤 수로 한없이 가까워지게 할 것인지 입력하여 주십시오. : ")
b = Limit(a2, x, c, dir='+').doit()
d = Limit(a1, x, c, dir='-').doit()
e = a3.subs(x,c)

print("-----------------------------------")

print("좌극한 : ", end='')
pprint(d)

print("우극한 : ", end='')
pprint(b)

print("함숫값 : ",end='')
pprint(e)

def equal():
    if isNum(b) == 'F' or isNum(d) == 'F':
        f = Eq(d, b)
        g = solve(f)
        print("-----------------------------------")
        print("극한값이 존재하기 위한 상수(문자)의 값은 ", end='')
        print(g, end='')
        print("입니다.")

    if isNum(e) == 'F':
        h = Eq(b, e)
        i = solve(h)
        print("-----------------------------------")
        print("연속이기 위한 상수(문자)의 값은 ", end='')
        print(i, end='')
        print("입니다.")

equal()
print("-----------------------------------")

if b == d == e:
    print("연속입니다.")
elif b == d != e:
    print("극한값은 존재하지만, 불연속입니다.")
    print("-----------------------------------")
    print("※ 좌극한, 우극한의 값은 같으나 함숫값이 문자라면, 불연속으로 출력이 됩니다. ※")
else:
    print("불연속입니다.")
    print("-----------------------------------")
    print("※ 좌극한,우극한,함숫값 중에서 하나라도 문자가 존재하여 모두 같지 않으면 불연속으로 출력이 됩니다. ※")
