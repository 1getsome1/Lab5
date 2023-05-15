

import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    def test_Time_eq_1(self):
        time1 = (12, 0, 0)
        time2 = (12, 0, 0)
        time3 = (11, 59, 59)
        assert (time1 == time2) == True
        assert (time1 == time3) == False

    def test_Time_eq_2(self):
        time1 = (7, 30, 0)
        time2 = (0, 8, 30)
        time3 = (0, 8, 30)
        assert (time3 == time2) == True
        assert (time1 == time3) == False

    #### Add tests for Time.__repr__
    def test_Time_repr_1(self):
        str_time = data.Time(17, 23, 53)
        self.assertEqual(repr(str_time), "Time(17, 23, 53)")

    def test_Time_repr_2(self):
        str_time = data.Time(12, 34, 47)
        self.assertEqual(repr(str_time), "Time(12, 34, 47)")


    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
