def divisible(number):
    for x in range(number, 1, -1):  
        print 'x = %d' % x 
        i = 1
        while True:
            if (i * number) % (x - 1) != 0:
                i += 1
            else:
                number = (i * number)
                print 'increment num: %d' % number
                break
    return number

# print divisible(20)

assert (divisible(20) == 232792560), "Got a wrong answer"

assert (divisible(10) == 2520), "Got a wrong answer"

