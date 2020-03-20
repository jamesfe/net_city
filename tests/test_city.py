import unittest

import city


class TestCityMethods(unittest.TestCase):

    def test_city_init(self):
        testcity = city.City(3, 3)
        self.assertIsNotNone(testcity)


if __name__ == '__main__':
    unittest.main()
