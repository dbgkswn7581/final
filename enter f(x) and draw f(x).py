import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import re

def draw(fx):
    fig, ax = plt.subplots()

    def style():
        ax.spines['left'].set_position(('data', 0))
        ax.spines['right'].set_visible('none')
        ax.spines['top'].set_visible('none')
        ax.spines['bottom'].set_position(('data', 0))
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

        for old, new in replacements.items():
            string = string.replace(old, new)

        def func(x):
            return eval(string)

        return func

    if __name__ == '__main__':
        func = string2func(fx)
        a = float(input('enter lower limit: '))
        b = float(input('enter upper limit: '))
        c = np.linspace(a, b, 250)

        style()
        plt.plot(c, func(c))
        plt.xlim(a, b)
        plt.show()

fx = input("f(x)를 입력해 주십시오. : ")
draw(fx)
