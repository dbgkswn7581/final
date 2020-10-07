import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import re
import os

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

def der(fx):
    i = Derivative(fx,x)
    j = i.doit()

    k = j.subs(x,c)

    return k

def der_(fx):
    i = Derivative(fx,x)
    j = i.doit()
    return j

pfind(a1)
pfind(a2)
a3 = simplify(a3)



c = input("f(x) 함수가 어떤 x 값을 기준으로 나누어져 있는지 입력하여 주십시오. : ")
b = Limit(a2, x, c, dir='+').doit()
d = Limit(a1, x, c, dir='-').doit()
e = a3.subs(x,c)
l = der(a1)
_l = der_(a1)
m = der(a2)
_m = der_(a2)

def draw(fx, gx, fk, k, f_x, g_x):
    fig, ax = plt.subplots()

    def style():
        ax.spines['left'].set_position(('data',0))
        ax.spines['right'].set_visible('none')
        ax.spines['top'].set_visible('none')
        ax.spines['bottom'].set_position(('data',0))
        ax.tick_params('both', length=0)


    replacements = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'exp': 'np.exp',
        'sqrt': 'np.sqrt',
        '^': '**',
    }

    allowed_words = [
        'x',
        'sin',
        'cos',
        'sqrt',
        'exp',
    ]

    def string2func(string):
        ''' 문자열을 평가하고 x의 함수를 반환한다. '''
        # 모든 단어를 찾아 모든 것이 허용되는지 확인한다.:
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in allowed_words:
                raise ValueError(
                    '"{}"은 수학 식에서 사용할 수 없습니다.'.format(word)
                )

        for old, new in replacements.items():
            string = string.replace(old, new)

        def func(x):
            return eval(string)


        return func

    if __name__ == '__main__':


        func = string2func(fx)
        funcc = string2func(gx)
        funccc = string2func(f_x)
        funcccc = string2func(g_x)
        a = float(input('정의역의 하한선을 입력하여 주십시오. : '))
        b = float(input('정의역의 상한선을 입력하여 주십시오. : '))
        c = np.linspace(a, k, 250)
        d = np.linspace(k, b, 250)

        x = Symbol('x')

        if f_x.find('x') >= 0:
            plt.plot(c,funccc(c), c='b', label='f`(x)')
        else:
            y = [f_x for i in c]
            plt.plot(c,y, c='b', label='f`(x)')

        if g_x.find('x') >= 0:
            plt.plot(d,funcccc(d), c='b', label='g`(x)')
        else:
            z = [g_x for i in d]
            plt.plot(d,z, c='b',label='g`(x)')



        if fx == fk != gx:
            fk = sympify(fk)
            e = fk.subs(x, k)
            gx = sympify(gx)
            f = gx.subs(x, k)
            plt.scatter(k,e,c='r',marker='o')
            plt.scatter(k,f,c='r',marker='x')
        elif fx != fk == gx:
            fk = sympify(fk)
            e = fk.subs(x, k)
            fx = sympify(fx)
            f = fx.subs(x, k)
            plt.scatter(k, e, c='r', marker='o')
            plt.scatter(k, f, c='r', marker='x')

        style()

        plt.plot(c, func(c), c = 'r',label = 'f(x)')
        plt.plot(d, funcc(d),c = 'r', label = 'g(x)')
        plt.xlim(a, b)
        plt.legend()
        plt.show()

print("-----------------------------------")

print("좌극한 : ", end='')
pprint(d)

print("우극한 : ", end='')
pprint(b)

print("함숫값 : ",end='')
pprint(e)

print("x<%s일 때 도함수 : "%c,end='')
pprint(_l)

print("x>%s일 때 도함수 : "%c,end='')
pprint(_m)

print("좌미분계수 : ",end='')
pprint(l)

print("우미분계수 : ",end='')
pprint(m)


if isNum(b) == 'F' or isNum(d) == 'F':
    f = Eq(d,b)
    g = solve(f)
    print("-----------------------------------")
    print("극한값이 존재하기 위한 상수(문자)의 값은 ",end='')
    print(g,end='')
    print("입니다.")


if isNum(e) == 'F':
    h = Eq(b,e)
    i = solve(h)
    print("-----------------------------------")
    print("연속이기 위한 상수(문자)의 값은 ",end='')
    print(i,end='')
    print("입니다.")


print("-----------------------------------")

if b == d == e:
    print("연속입니다.")
    if l == m:
        print("미분 가능한 함수입니다.")
    else :
        print("연속이지만 미분이 불가능한 함수입니다.")
        if isNum(l) == 'F' or isNum(m) =='F':
            h = Eq(l, m)
            i = solve(h)
            print("-----------------------------------")
            print("미분가능 하기 위한 상수(문자)의 값은 ", end='')
            print(i, end='')
            print("입니다.")

elif b == d != e:
    print("극한값은 존재하지만, 불연속입니다.")
    print("-----------------------------------")
    print("※ 좌극한, 우극한의 값은 같으나 함숫값이 문자라면, 불연속으로 출력이 됩니다. ※")
    print("※ 불연속이라면, 미분 가능성을 따지지 않습니다. ※")
else:
    print("불연속입니다.")
    print("-----------------------------------")
    print("※ 좌극한,우극한,함숫값 중에서 하나라도 문자가 존재하여 모두 같지 않으면 불연속으로 출력이 됩니다. ※")
    print("※ 불연속이라면, 미분 가능성을 따지지 않습니다. ※")


print("-----------------------------------")


if isNum(b) == 'F' or isNum(d) == 'F' or isNum(e) == 'F' or isNum(l) == 'F' or isNum(m) == 'F':
    print("※ 입력한 함수에 x 이외의 문자가 존재하여 그래프를 그릴 수 없습니다. ※")

else :
    print("입력한 함수를 그리기 위하여 정의역을 입력하여 주십시오.")
    draw(str(a1),str(a2),str(a3),float(c),str(_l),str(_m))

os.system('pause')
