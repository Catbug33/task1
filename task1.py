import numpy
array = numpy.random.random_integers(0,9,(10,10,10))
print array

biggest_sum = 0;
dimension = len(array)
for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):

            sum_current = 0
           # print 'XXX'
            for x in range(0, dimension):
                sum_current += array[i, j, x]
                #print x, 'index of x'
                #print array[i, j, x], '- number on[i, j, x] ', sum_current, ' - sum_current'
                if sum_current > biggest_sum:
                    biggest_sum = sum_current

            #print 'YYY'
            for y in range(0, dimension):
                sum_current += array[i, y, k]
                # print y, 'index of y'
                # print array[i, y, k],'number on array[i, y, k] ', sum_current, 'sum_current'
                if sum_current > biggest_sum:
                    biggest_sum = sum_current

            # print 'ZZZ'
            for z in range(0, dimension):
                # print array[z, j, k], 'number on array[z, j, k]'
                sum_current += array[z, j, k]
                # print z, 'index of z                                    '
                # print sum_current, 'sum_current',
                if sum_current > biggest_sum:
                    biggest_sum = sum_current
print 'here is it'
print biggest_sum, 'biggest_sum'
