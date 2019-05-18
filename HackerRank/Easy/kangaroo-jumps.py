import unittest

'''
You are choreographing a circus show with various animals.
For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

If it is possible for both kangaroos to be at the same location after the same amount of jumps, return "YES". Otherwise, return "NO".

Example:
Kangaroo 1 starts at x1 = 2 with a jump distance of v1 = 1.
Kangaroo 2 starts at x2 = 1 with a jump distance of v2 = 1.
After one jump, they are both at x = 3, (x1 + v1 = 2 + 1 = 3, x2 + v2 = 1 + 2 = 3), so our answer is YES.

Function Description

Complete the function kangaroo in the editor below.
It should return YES if they reach the same position at the same time, or NO if they don't.

See here: https://www.hackerrank.com/challenges/kangaroo/problem
'''


def kangaroo(x1, v1, x2, v2):
    can_collide = "NO"
    jumps1 = 0
    jumps2 = 0
    while True:
        if kangaroo_ahead_and_jumps_further(x1, v1, x2, v2):
            break
        else:
            if x1 == x2 and jumps1 == jumps2:
                can_collide = "YES"
                break
            x1 += v1
            x2 += v2
            jumps1 += 1
            jumps2 += 1

    return can_collide


def kangaroo_ahead_and_jumps_further(x1, v1, x2, v2):
    return (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1)


class Tests(unittest.TestCase):
    def test_simple_yes(self):
        self.assertEqual(kangaroo(0, 3, 4, 2), 'YES')

    def test_simple_no(self):
        self.assertEqual(kangaroo(0, 2, 5, 3), 'NO')

    def test_far_apart_with_equal_rates(self):
        self.assertEqual(kangaroo(43, 2, 70, 2), 'NO')


unittest.main()
