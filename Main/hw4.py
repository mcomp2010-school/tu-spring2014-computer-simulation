
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
    
    print '%s\t%s'%(m, -fut)


import numpy

a =numpy.random.exponential(float(20)/float(225),1000)





