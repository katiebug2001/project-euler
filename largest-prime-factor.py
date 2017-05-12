import unittest


def largest_prime_factor(num):
    """The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143.
    finds the largest prime factor of num"""

    half_num = (num//2)
    possible_factors = generator_primes(half_num)
    possible_factors.reverse()

    for factor in possible_factors:
        if (num % factor) == 0:
                return(factor)

    return num


def generator_primes(x):
    """generates all prime numbers less than or equal to x"""

    primes = []

    for maybe_prime in range(2, (x + 1)):
        #steps through every number from 2 to our number x
        print("the number we are evaluating is {}".format(maybe_prime))
        is_prime = True

        for prime in primes:
            #steps through every number already in our list of primes
            print("the number we are testing {} with is {}".format(maybe_prime, prime))

            if (maybe_prime%prime) == 0:
                print("{} is divisible by {}; {} is not prime".format(maybe_prime, prime, maybe_prime))
                is_prime = False
                break

        if is_prime == True:
            primes.append(maybe_prime)
            print("added {} to our list of primes".format(maybe_prime))
        #print("done evaluating {}".format(maybe_prime))
    return primes

print(largest_prime_factor(10))

# class test_primeGen_largePrime(unittest.TestCase):
#     """tests the functions generator_primes() and largest_prime_factor()"""
#
#     def test_generator_primes(self):
#         test_primes = []
#         check_primes = [ [], [2, 3], [2, 3, 5],[2, 3, 5, 7, 11, 13, 17, 19, 23], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] ]
#         test_list = [ 1, 3, 6, 23, 100]
#         for n in test_list:
#             test_primes.append(generator_primes(n))
#         self.assertEqual(check_primes, test_primes)
#
#     def test_largest_prime_factor(self):
#         test_factors = []
#         check_factors = [ 3, 3, 5, 5]
#         test_list = [ 3, 6, 20, 100]
#
#         for n in test_list:
#             print(n)
#             test_factors.append(largest_prime_factor(n))
#         self.assertEqual(check_factors, test_factors)
#
# if __name__ == '__main__':
#      unittest.main()