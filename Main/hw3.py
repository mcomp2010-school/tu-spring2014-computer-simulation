import math
from eara_math import DescStat
from eara_math import Integral


def print_monte_carlo(integral, list_n):
    for n in list_n:
        integral.n = n
        print DescStat.monte_carlo(integral)

'''
Integeral 1
'''
integral1 = Integral(0, math.pi, 10, lambda x: float(math.sin(x)), 'sin(x) dx')
print_monte_carlo(integral1, [10, 100, 500, 1000])


'''
Integeral 2
'''
function2 = lambda x: float(math.sqrt(15 * x))
integral2 = Integral(1, 6, 10, function2, 'sqrt(15x) dx')
print_monte_carlo(integral2, [10, 100, 500, 1000])

'''
Integeral 3
'''
function3 = lambda x: float((2 * (math.pow(math.e, (x * (-1)) / 2))) /
                            (math.sqrt(2 * math.pi)))
integral3 = Integral(0, 5, 10, function3, '(2*e^(-x/2))/(sqrt(2PI)) dx')
print_monte_carlo(integral3, [10, 100, 500, 1000])

'''
Integeral 4
'''
function4 = lambda x: float(1.0 / float(x))
integral4 = Integral(1, 3, 10, function4, 'dx 1/x')
print_monte_carlo(integral4, [10, 100, 500, 1000])

'''
Integeral 5
'''
function5 = lambda x: float(1.0 / float(1.0 + math.pow(x, 2)))
integral5 = Integral(2, 4, 10, function5, 'dx 1/(1+x^2)')
print_monte_carlo(integral5, [10, 100, 500, 1000])

'''
OUTPUT:
[l=0,u=3.14159265359, n=10] sin(x) dx = 1.88023375314
[l=0,u=3.14159265359, n=100] sin(x) dx = 1.9742454408
[l=0,u=3.14159265359, n=500] sin(x) dx = 1.89903609068
[l=0,u=3.14159265359, n=1000] sin(x) dx = 2.02438500755
[l=1,u=6, n=10] sqrt(15x) dx = 27.1108834235
[l=1,u=6, n=100] sqrt(15x) dx = 32.5330601081
[l=1,u=6, n=500] sqrt(15x) dx = 36.5996926217
[l=1,u=6, n=1000] sqrt(15x) dx = 36.1930293703
[l=0,u=5, n=10] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.1968268412
[l=0,u=5, n=100] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.39629798141
[l=0,u=5, n=500] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.45214990066
[l=0,u=5, n=1000] (2*e^(-x/2))/(sqrt(2PI)) dx = 1.50800181992
[l=1,u=3, n=10] dx 1/x = 0.6
[l=1,u=3, n=100] dx 1/x = 1.08
[l=1,u=3, n=500] dx 1/x = 1.152
[l=1,u=3, n=1000] dx 1/x = 1.266
[l=2,u=4, n=10] dx 1/(1+x^2) = 0.6
[l=2,u=4, n=100] dx 1/(1+x^2) = 0.2
[l=2,u=4, n=500] dx 1/(1+x^2) = 0.208
[l=2,u=4, n=1000] dx 1/(1+x^2) = 0.222
'''
