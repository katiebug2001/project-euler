import unittest
import math

def factor(num):

    """returns ALL (not just prime) factors of a number"""

    limit = int(math.sqrt(num))
    factors = [1]

    if num > 1:
        factors.append(num)

    if limit > 1:
        if num/limit == limit:
            factors.append(limit)

        elif num % limit == 0:
            factors.extend([limit, num//limit])


    for d in range(2, limit):
        if num % d == 0:
                factors.extend([d, num//d])

    print("{} has {} factors".format(num, len(factors)))
    factors.sort()
    return factors


def next_triangle(triangle_tuple, num_to_skip = 1):
    """takes a triangular number and ordinally which triangular number that one is in a tuple (e.g (1, 1) or (15, 5)
    returns the next triangular number and the number of that triangular number in a tuple"""
    #print("triangle_tuple = {}".format(triangle_tuple))
    #print("num_to_skip = {}".format(num_to_skip))

    num_new_triangle = (triangle_tuple[1] + num_to_skip)
    #print("num_new_triangle = {}".format(num_new_triangle))

    triangle_to_be_added = triangle_tuple[0]

    for addend in range((triangle_tuple[1] + 1), (triangle_tuple[1] + num_to_skip + 1)):
        #print("addend = {}".format(addend))
        #print("triangle_to_be_added = {}".format(triangle_to_be_added))
        triangle_to_be_added += addend

    return (triangle_to_be_added, num_new_triangle)


def factor_test(up_to):
    triangle = (1, 1)
    this_triangle_factors = factor(triangle[0])

    while True:
        print("triangle: {}, factors: {} ".format(triangle[0], len(factor(triangle[0]))))
        triangle = next_triangle(triangle)
        # last_triangle_factors, this_triangle_factors = this_triangle_factors, factor(triangle[0])
        # if len(last_triangle_factors) > len(this_triangle_factors):
        #     print("fail :(")
        #     break
        if triangle[1] >= up_to:
            #print("done!")
            break

def find_triangle(factors):
    """takes a number of factors; returns first triangular number with more than that many factors"""
    triangle = (1,1)
    while len(factor(triangle[0])) <= factors:
        triangle = next_triangle(triangle)

    return triangle[0]

print(find_triangle(500))


class test_factor_and_next_triangle(unittest.TestCase):
    """tests factor and next_triangle"""

    def test_find_triangle(self):
        """ tests the function find_triangle """
        more_factors_than = [1, 4, 5, 10, 15]
        test_hopeful_output = [3, 28, 28, 120, 120]
        test_output = []

        for input in more_factors_than:
            test_output.append(find_triangle(input))
        self.assertEqual(test_output, test_hopeful_output)

    def test_factor(self):
        """tests the function factor"""

        test_numbers = [1, 2, 8, 5, 21, 28]
        test_factorizations = [[1],  [1, 2], [1, 2, 4, 8], [1, 5], [1, 3, 7, 21], [1, 2, 4, 7, 14, 28]]
        returned_factorizations = []

        for num in test_numbers:
            returned_factorizations.append(factor(num))

        self.assertEqual(test_factorizations, returned_factorizations)

    def test_next_triangle(self):
        """tests the function next_triangle"""

        test_input_tri_tuples = [(1,1), (15,5),]
        check_output_tri_tuples = [(3, 2), (21, 6)]
        outputs = []

        for input in test_input_tri_tuples:
            outputs.append(next_triangle(input))

        self.assertEqual(next_triangle((10, 4), 5), (45, 9))

        self.assertEqual(check_output_tri_tuples, outputs)



if __name__ == "__main__":
    unittest.main()

#35942481