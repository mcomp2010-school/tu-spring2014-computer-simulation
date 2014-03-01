from eara_math import DescStat

list1 = [775, 1312, 686, 1549, 880, 1231, 1641, 74, 1020, 1220, 1381,
         1496, 76, 1296, 502, 1378, 1786, 1722, 704, 643, 995, 40, 281,
         1690, 1608, 1714, 1118, 1237, 1370, 1646, 574, 876, 1652, 1924,
         904, 1267, 1507, 1399, 1173, 354, 1425, 736, 752, 771, 51,
         997, 1589, 750, 518, 1678, 1513, 683, 1324, 1675, 101, 1171,
         471, 161, 235, 38, 828, 311, 1806, 1402, 399, 1331, 1211, 1151,
         528, 850, 1124, 1087, 533, 1656, 1439, 1785, 1910, 1024, 233,
         133, 1749, 1258, 488, 1638, 1198, 153, 401, 310, 159, 258, 568,
         475, 211, 861, 285, 1303, 57, 903, 1561, 1768]

print 'Length of List: %s' % len(list1)
print 'Mean: %s' % DescStat.mean(list1)
print 'Standard Deviation %s' % \
        DescStat.sample_standard_deviation(list1)
print 'Coefficent of Skewness %s' % \
        DescStat.coefficent_of_skewness(list1)
print 'Coefficent of Kurtosis %s' % \
        DescStat.coefficent_of_kurtosis(list1)
print 'Coefficent of Excess Kurtosis %s' % \
        DescStat.coefficent_of_excess_kurtosis(list1)

'''
Output
===============================
Length of List: 100
Mean: 976.85
Standard Deviation 557.971078773
Coefficent of Skewness 0.139879112857
Coefficent of Kurtosis 1.74541289519
Coefficent of Excess Kurtosis -1.25458710481
===============================
'''
