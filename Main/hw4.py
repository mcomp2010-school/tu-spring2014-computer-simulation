
obvers = [18,13,3,40,9,29,10,3,8,10,
          1,17,29,2,22,1,22,1,4,32,
          20,5,8,6,10,3,1,11,13,2,
            15,8,1,23,29,9,34,17,10,4,
            15,2,1,1,40,8,6,6,8,1,
            3,24,14,24,8,14,28,12,18,7,
            1,5,6,10,54,12,13,1,22,45,
            5,12,2,14,12,1,33,23,7,5,
            12,5,46,18,2,2,6,2,39,7,
            4,4,2,19,1,5,12,3,5,1]

obvers.sort()
#print obvers

freq = {}

for obv in obvers:
    if freq.get(obv):
        freq[obv] = freq.get(obv) + 1
    else: 
        freq[obv] = 1

print freq

interval = 5
start = 0
end = 50

bins_dict = 0
print int(end) / int(interval)



# for k,v in freq.iteritems():
#     print '%s\t%s'%(k,v)


import math

past=0 
for m in range(5, 60, 5):
    p = float(m)
    x = float(20) / float(225)
    d= -1.0 * p * x

    pre = 1 - math.pow(math.e, d )
    fut = past - pre
    past = 1 - math.pow(math.e, d )
    
    #print '%s\t%s'%(m, -fut)

'''
#############################################
'''
import numpy

a = numpy.random.exponential(float(20)/float(225),1000)


'''
#############################################
'''


import scipy.stats as st

class my_pdf(st.rv_continuous):
    def _pdf(self,x):
        xa = float(20) / float(225)
        d= -1.0 * p * x

        pre = 1 - math.pow(math.e, d )
    
        return pre

my_cv = my_pdf(a=0.0,b=30.0,name='my_pdf')
print my_cv.rvs(size=5) 
# Chi Square from Normal

#sum(x-m/v)

class ChiSquareFromNormal(st.rv_continuous):
    def _pdf(self,x):
        return x-40/20

my_cv = ChiSquareFromNormal(a=0.0,b=100.0,name='my_pdf')
print my_cv.rvs(size=5) 

"""
OUTPUT:
[ 4.25731918  4.20151548  4.10128827  4.09638405  4.34611102]
"""

# Laplace from Exponential

class LaplaceFromExponential(st.rv_continuous):
    def _pdf(self,x):
        return 1 - math.pow(math.e, -x )

my_cv = LaplaceFromExponential(a=0.0,b=100.0,name='my_pdf')
print my_cv.rvs(size=5) 

"""
OUTPUT:
[ 0.12679166  1.03864539  0.61428448  0.38842799  0.23260088]
"""

# cauchy from normal
class CauchyFromNormal(st.rv_continuous):
    def _pdf(self,x):
        return (x-40/20) - (x-300/20) 

my_cv = CauchyFromNormal(a=0.0,b=100.0,name='my_pdf')
print my_cv.rvs(size=5) 

"""
OUTPUT:
[ 0.03843663  0.03411253  0.06767783  0.03259841  0.011621  ]
"""

# TRiangle from uniform
class TriangleFromUniform(st.rv_continuous):
    def _pdf(self,x):
        return math.log(1+(2-1)*x) 

my_cv = TriangleFromUniform(a=0.0,b=100.0,name='my_pdf')
print my_cv.rvs(size=5) 

"""
OUTPUT:
[ 1.44969574  1.49228347  1.68398838  1.29081857  1.11232111]
"""
