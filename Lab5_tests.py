import data
import Lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        F_time = data.Time(3, 20, 10)
        S_time = data.Time(4, 30, 40)
        Total = Lab5.time_add(F_time, S_time)
        assert Total == (7, 50, 50)

    def test_time_add_2(self):
        F_time = data.Time(5, 13, 50)
        S_time = data.Time(6, 20, 50)
        Total = Lab5.time_add(F_time, S_time)
        assert Total == (11, 34, 40)

    def test_time_add_3(self):
        F_time = data.Time(23, 120, 34)
        S_time = data.Time(24, 80, 69)
        Total = Lab5.time_add(F_time, S_time)
        assert Total == (50, 21, 43)


    # Part 4
    def test_is_descending_1(self):
        nums = [4, 3, 2, 1]
        Out_put = Lab5.is_descending(nums)
        assert Out_put == True

    def test_is_descending_2(self):
        nums = [1.21, 2.21, 3, 4.3]
        Out_put = Lab5.is_descending(nums)
        assert Out_put == False

    def test_is_descending_3(self):
        nums = []
        Out_put = Lab5.is_descending(nums)
        assert Out_put == None

    # Part 5
    def test_largest_between_1(self):
        numbers = [5, 2, 6, 3, 9, 1, 8, 4, 7, 0]
        lower = 3
        upper = 8
        expected = 4
        result = Lab5.largest_between(numbers, lower, upper)
        self.assertEqual(result, expected)

    def test_largest_between_2(self):
        numbers = [5, 2, 6, 3, 9, 1, 8, 4, 7, 0]
        lower = -3
        upper = 7
        expected = None
        result = Lab5.largest_between(numbers, lower, upper)
        self.assertEqual(result, expected)


    # Part 6
    def test_furthest_from_origin_1(self):
        points = [data.Point(0, 0), data.Point(1, 1), data.Point(2, 2), data.Point(3, 3), data.Point(4, 4)]
        assert Lab5.furthest_from_origin(points) == 4

    def test_furthest_from_origin_2(self):
        points = [data.Point(53, 83), data.Point(-60, 90), data.Point(70, -66)]
        assert Lab5.furthest_from_origin(points) == 1




if __name__ == '__main__':
    unittest.main()
