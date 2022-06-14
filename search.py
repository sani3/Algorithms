def linear_search(value, items):
    """(any, list) -> number

    Return the index of a value in a list if it exist
    :param value: any
    :param items: list
    :return: number
    """
    result = -1

    # for index in items
    #   if value == item at index
    #       result gets index
    for index, item in enumerate(items):
        if value == item:
            result = index

    return result


def binary_search(value, items):
    """(any, list) -> number

    Return the index of a value in a sorted list if it exist
    :param value: any
    :param items: list
    :return: number
    """
    # NOTE: items must be sorted
    upper = len(items)-1
    lower = 0
    while lower <= upper:
        # mid gets index at middle of upper and lower bound
        mid = (lower + (upper - lower))+1 // 2
        # if value is less than item at mid of upper and lower bounds of items
        #   update upper bound to exclude all indexes greater or equal to mid
        # else if value is greater than item at mid of upper and lower bounds of items
        #   update lower bound to exclude all indexes less than or equal to mid
        # else return item at mid
        if value < items[mid]:
            upper = mid - 1
        elif value > items[mid]:
            lower = mid + 1
        else:
            return mid
    return -1


if __name__ == "main":
    import unittest

    class MyTestCase(unittest.TestCase):
        def test_linear_search_1(self):
            self.assertEqual(linear_search(30, [-5, -10, 0, -20, -40, 40, 30, 10, 25]), 6)

        def test_linear_search_2(self):
            self.assertEqual(linear_search(50, [-5, -10, 0, -20, -40, 40, 30, 10, 25]), -1)

        def test_binary_search_1(self):
            self.assertEqual(binary_search(30, [-40, -20, -10, -5, 0, 10, 25, 30, 40]), 7)

        def test_binary_search_2(self):
            self.assertEqual(binary_search(-40, [-40, -20, -10, -5, 0, 10, 25, 30, 40]), 0)

        def test_binary_search_3(self):
            self.assertEqual(binary_search(40, [-40, -20, -10, -5, 0, 10, 25, 30, 40]), 8)

        def test_binary_search_4(self):
            self.assertEqual(binary_search(50, [-40, -20, -10, -5, 0, 10, 25, 30, 40]), -1)
