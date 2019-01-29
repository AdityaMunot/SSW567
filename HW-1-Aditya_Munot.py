'''
First Homework



Author = Aditya Munot
'''
import math
import unittest


def classify_Triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[2] >= sides[1] + sides[0]:
        return('Not a Triangle')
    elif a == b and b == c and a == c:
        return('Equilateral')
    elif a == b or b == c or a == c:
        return('Isoceles')
    else:
        sides = sorted([a, b, c])
        if sides[2] == math.sqrt((sides[0] ** 2) + (sides[1] ** 2)):
            return('Right')
        else:
            return('Scalene')


def main():
    print(classify_Triangle(1, 2, 3))
    print(classify_Triangle(2, 2, 3))
    print(classify_Triangle(5, 12, 13))
    print(classify_Triangle(3, 3, 3))
    print(classify_Triangle(6, 7, 8))


class RepositoryTest(unittest.TestCase):
    def test1_Right_Triangle(self):
        self.assertEqual(classify_Triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_Triangle(5, 12, 13), 'Right')
        self.assertEqual(classify_Triangle(7, 24, 25), 'Right')
        self.assertEqual(classify_Triangle(8, 15, 17), 'Right')

    def test2_Equilateral_Triangle(self):
        self.assertEqual(classify_Triangle(1, 1, 1 ** 0.5), 'Equilateral')
        self.assertNotEqual(classify_Triangle(2, 2, 3), 'Equilateral', 'Should be Isoceles')
        self.assertEqual(classify_Triangle(3, 3, 3), 'Equilateral')
        self.assertEqual(classify_Triangle(4, 4, 4), 'Equilateral')
        self.assertEqual(classify_Triangle(5, 5, 5), 'Equilateral')
        self.assertEqual(classify_Triangle(6, 6, 6), 'Equilateral')

    def test3_Isoceles_Triangle(self):
        self.assertEqual(classify_Triangle(2, 1, 2), 'Isoceles')
        self.assertEqual(classify_Triangle(100, 100, 2), 'Isoceles')
        self.assertEqual(classify_Triangle(20, 10, 20), 'Isoceles')
        self.assertEqual(classify_Triangle(10, 10, 15), 'Isoceles')
        self.assertEqual(classify_Triangle(1, 1, (2 ** (0.5))), 'Isoceles', 'Should be Right Triangle')
        self.assertEqual(classify_Triangle(2, 2, 8 ** 0.5), 'Isoceles', 'Should be Right Triangle')

    def test4_Not_A_Triangle(self):
        self.assertEqual(classify_Triangle(1, 1, 2), 'Not a Triangle')
        self.assertEqual(classify_Triangle(16, 1, 1), 'Not a Triangle')
        self.assertEqual(classify_Triangle(10, 10, 20), 'Not a Triangle')

    def test5_Scalene_Triangle(self):
        self.assertEqual(classify_Triangle(3, 2, 4), 'Scalene')
        self.assertEqual(classify_Triangle(3, 6, 4), 'Scalene')
        self.assertEqual(classify_Triangle(3, 14, 12), 'Scalene')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
