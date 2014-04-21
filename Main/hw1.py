import math
from eara_math import DescStat
from eara_math import Integral


def print_integrals(integral, list_n):
    for n in list_n:
        integral.n = n
        print DescStat.trapeziod_rule(integral)

'''
Integral 1
'''
integral1 = Integral(0, math.pi, 10, lambda x: float(math.sin(x)), 'sin(x) dx')
print_integrals(integral1, [10, 100, 1000])

'''
Integral 2
'''
function2 = lambda x: float(math.sqrt(15 * x))
integral2 = Integral(1, 6, 10, function2, 'sqrt(15x) dx')
print_integrals(integral2, [10, 100, 1000])

'''
Integral 3
'''
function3 = lambda x: float((2 * (math.pow(math.e, (x * (-1)) / 2))) /
                            (math.sqrt(2 * math.pi)))
integral3 = Integral(0, 5, 10, function3, '(2*e^(-x/2))/(sqrt(2PI)) dx')
print_integrals(integral3, [10, 100, 1000])

'''
Integral 4
'''
function4 = lambda x: float(1.0 / float(x))
integral4 = Integral(1, 3, 10, function4, 'dx 1/x')
print_integrals(integral4, [10, 100, 1000])

'''
Integral 5
'''
function5 = lambda x: float(1.0 / float(1.0 + math.pow(x, 2)))
integral5 = Integral(2, 4, 10, function5, 'dx 1/(1+x^2)')
print_integrals(integral5, [10, 100, 1000])

'''
Output of program:
[l=0,u=3.14159265359, n=10] sin(x) dx = 1.98352353751
[l=0,u=3.14159265359, n=100] sin(x) dx = 1.99983550389
[l=0,u=3.14159265359, n=1000] sin(x) dx = 1.99999835507
[l=1,u=6, n=10] sqrt(15x) dx = 35.3415885232
[l=1,u=6, n=100] sqrt(15x) dx = 35.3651043032
[l=1,u=6, n=1000] sqrt(15x) dx = 35.3890577197
[l=0,u=5, n=10] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.47240154498
[l=0,u=5, n=100] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.46485670531
[l=0,u=5, n=1000] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.46494491424
[l=1,u=3, n=10] dx 1/x = 1.10156232656
[l=1,u=3, n=100] dx 1/x = 1.09864191698
[l=1,u=3, n=1000] dx 1/x = 1.0989459183
[l=2,u=4, n=10] dx 1/(1+x^2) = 0.219109533991
[l=2,u=4, n=100] dx 1/(1+x^2) = 0.218673356438
[l=2,u=4, n=1000] dx 1/(1+x^2) = 0.218727813509
'''
