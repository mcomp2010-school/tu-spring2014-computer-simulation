import math
import random


class Integral(object):

    def __init__(self, lowerbound, upperbound, n, function, function_desc):
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.n = n
        self.function = function
        self.function_desc = function_desc

    def __str__(self):
        return ('[l=' + str(self.lowerbound) +
                ',u=' + str(self.upperbound) +
                ', n=' + str(self.n) + '] ' +
                str(self.function_desc))


class DescStat(object):
    """
    Computer Simulation Class
    """

    @staticmethod
    def monte_carlo(integral):
        lowerbound = float(integral.lowerbound)
        upperbound = float(integral.upperbound)
        n = float(integral.n)
        function = integral.function
        # Variables
        accept=0       # acceptances
        rx=0.0         # random number between a and b 
        ry=0.0         # random number between 0 and ymax
        ymax = 0.0
        try:
            ymax = function(0)    # maximum value of normal pdf
            stop_counter = False
            counter = 0.0
            times  = 1
            while stop_counter == False:
                counter = counter + .5
                times= times + 1
                eval_func = function(counter)
                if eval_func > ymax and times < 100:
                    ymax = eval_func
                else:
                    stop_counter = True 
        except:
            ymax = 3

        # Integration
        for i in range(int(n)):
            rx=lowerbound+(upperbound-lowerbound)*random.random()
            ry=ymax*random.random()
            # Accept/Reject
            if ry<function(rx):
                accept +=1
        return str(integral) + ' = ' + str((upperbound-lowerbound)*
                                           ymax*
                                           float(accept)/float(n))
    
    @staticmethod
    def trapeziod_rule(integral):
        lowerbound = float(integral.lowerbound)
        upperbound = float(integral.upperbound)
        n = float(integral.n)
        function = integral.function

        deltax = (upperbound - lowerbound) / n
        point_list = []
        for x in range(1, int(n) + 2, 1):
            if x is 1 or x is int(n + 1):
                factor = 1
            else:
                factor = 2

            suma = 0.0
            if not point_list:
                function_results = (function(lowerbound) * factor)
                point_list.append({'x': float(lowerbound),
                                   'fx': function_results,
                                   'factor': factor,
                                   'sum': function_results})
            else:
                last_item_x = point_list[-1].get('x')
                last_item_sum = point_list[-1].get('sum')
                point = float(last_item_x) + float(deltax)
                function_results = (function(point) * factor)
                suma = (last_item_sum + function_results)
                point_list.append({'x': float(point),
                                   'fx': function_results,
                                   'factor': factor,
                                   'sum': suma})

        fact = float(deltax) / float(2)
        area = fact * suma
        return str(integral) + ' = ' + str(area)

    @staticmethod
    def summation(list_of_number, func_item=None, func_total=None):
        if not func_item:
            func_item = lambda x: float(x)
        if not func_total:
            func_total = lambda x: float(x)

        total = 0.0
        for item in list_of_number:
            total = total + float(func_item(item))
        return func_total(total)

    @staticmethod
    def summation_func(upper=1.0, func_item=None, func_total=None):
        if not func_item:
            func_item = lambda x: float(x)
        if not func_total:
            func_total = lambda x: float(x)

        total = 0.0
        count = 1.0
        while (count <= upper):
            
            total = total + float(func_item(count))
            count = count + .2
 
        return func_total(total)
    
    @staticmethod
    def mean(list_of_number):
        return DescStat.summation(list_of_number,
                                  lambda x: x,
                                  lambda x: x / float(len(list_of_number)))

    @staticmethod
    def variance(list_of_numbers):
        current_mean = float(DescStat.mean(list_of_numbers))
        total = DescStat.summation(list_of_numbers,
                                   lambda x: math.pow(current_mean - x, 2))
        return float(total) / float(len(list_of_numbers))

    @staticmethod
    def standard_deviation(list_of_numbers):
        return math.sqrt(DescStat.variance(list_of_numbers))

    @staticmethod
    def sample_standard_deviation(list_of_numbers):
        current_mean = float(DescStat.mean(list_of_numbers))
        total = DescStat.summation(list_of_numbers,
                                   lambda x: math.pow(current_mean - x, 2))
        result = float(total) / float(len(list_of_numbers) - 1)
        return math.sqrt(result)

    @staticmethod
    def coefficent_of_skewness(list_of_numbers):
        current_mean = float(DescStat.mean(list_of_numbers))
        total = DescStat.summation(list_of_numbers,
                                   lambda x: math.pow(current_mean - x, 3))
        length_minus_one = float(len(list_of_numbers) - 1)
        sd4 = math.pow(DescStat.sample_standard_deviation(list_of_numbers), 3)
        bottom = float(length_minus_one) * float(sd4)
        return float(total) / float(bottom)

    @staticmethod
    def coefficent_of_kurtosis(list_of_numbers):
        current_mean = float(DescStat.mean(list_of_numbers))
        total = DescStat.summation(list_of_numbers,
                                   lambda x: math.pow(current_mean - x, 4))
        length_minus_one = float(len(list_of_numbers) - 1)
        sd4 = math.pow(DescStat.sample_standard_deviation(list_of_numbers), 4)
        bottom = float(length_minus_one) * float(sd4)
        return float(total) / float(bottom)

    @staticmethod
    def coefficent_of_excess_kurtosis(list_of_numbers):
        return DescStat.coefficent_of_kurtosis(list_of_numbers) - 3
