import unittest
from math import sqrt


def largest_prime_factor(num):
    """The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143.
    finds the largest prime factor of num"""

    possible_factors = generator_primes(num)
    possible_factors.reverse()

    for factor in possible_factors:
        if (num % factor) == 0:
                return(factor)

    return num


def generator_primes(x):
    """generates all prime numbers up to sqrt(x) and one more"""

    primes = []
    sqrt_x = sqrt(x)
    #print(sqrt_x)
    bigger_than_sqrt = False

    for maybe_prime in range(2, x):
        # steps through every number from 2 to our number x
        # print("evaluating {}".format(maybe_prime))
        is_prime = True


        if (maybe_prime % 10000) == 0:
            print('at {}'.format(maybe_prime))

        if maybe_prime > sqrt_x:

            #print("{} is bigger than {}; finding one more prime".format(maybe_prime, sqrt_x))
            bigger_than_sqrt = True

        for prime in primes:
            #steps through every number already in our list of primes
            #print("dividing {} by {}".format(maybe_prime, prime))

            if (maybe_prime%prime) == 0:
                #print("{} is divisible by {}; {} is not prime".format(maybe_prime, prime, maybe_prime))
                is_prime = False
                break

        if is_prime:
            primes.append(maybe_prime)
            #print("added {} to primes".format(maybe_prime))

            if bigger_than_sqrt:
                #print("returning b/c bigger than sqrt")
                return primes

        #print("done evaluating {}".format(maybe_prime))




    #print('returning b/c done')
    return primes



print(largest_prime_factor(600851475143))

class test_primeGen_largePrime(unittest.TestCase):
    """tests the functions generator_primes() and largest_prime_factor()"""

    def test_generator_primes(self):
        test_primes = []
        check_primes = [ [], [2], [2, 3],[2, 3, 5], [2, 3, 5, 7, 11] ]
        test_list = [ 1, 3, 6, 23, 100]
        for n in test_list:
            test_primes.append(generator_primes(n))
        self.assertEqual(check_primes, test_primes)

    def test_largest_prime_factor(self):
        test_factors = []
        check_factors = [ 3, 3, 5, 5]
        test_list = [ 3, 6, 20, 100]

        for n in test_list:
            test_factors.append(largest_prime_factor(n))
        self.assertEqual(check_factors, test_factors)

if __name__ == '__main__':
     unittest.main()