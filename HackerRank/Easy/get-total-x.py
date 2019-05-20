
'''
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

1) The elements of the first array are all factors of the integer being considered
2) The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

For example, given the arrays a = [2, 6] and b = [24, 36], there are two numbers between them: 6 and 12.
Explanation:
    6 % 2 = 0, 6 % 6 = 0, and 24 % 6 = 0, 36 % 6 = 0 for the first value.
    Similarly, 12 % 2 = 0, 12 % 6 = 0 and 24 % 12 = 0, 36 % 12 = 0.

Complete the get_total_x function. It should return the number of integers that are between the sets.

get_total_x has the following parameter(s):

a: an array of integers
b: an array of integers

Output: Print the number of integers that are considered to be between a and b.
'''

from functools import reduce

# HELPER FUNCTIONS FOR LCM AND GCD


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


def gcdm(*args):
    """Return gcd of args."""
    return reduce(gcd, args)


def get_total_x(a, b):
    a_lcm = lcmm(*a)
    b_gcd = gcdm(*b)

    ints = 0
    ticker = a_lcm

    while ticker <= b_gcd:
        if ticker % a_lcm == 0 and b_gcd % ticker == 0:
            ints += 1
        ticker += 1

    return ints


print(get_total_x([2, 6], [24, 36]))  # 2 (6, 12)
print(get_total_x([2, 4], [16, 32, 96]))  # 3 (4, 8, 16)
print(get_total_x([1], [100]))  # 9 (1, 2, 4, 5, 10, 20, 25, 50, 100)
