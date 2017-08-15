
def mult_3_5(x):
    """ If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    # multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000. """

    mult_3 = []
    mult_5 = []

    for n in range(0, x, 3):
        #print(n)
        if not (n%5 == 0):
            mult_3.append(n)
    #print(mult_3)
    for n in range(0, x, 5):
        #print(n)
        mult_5.append(n)
    #print(mult_5)
    return sum(mult_3) + sum(mult_5)


mult_3_5(1000)


