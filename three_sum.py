def three_sum_bruteforce(numbers):
    """(list) -> int

    Returns a count of any three elements of the list that sums up to zero
    """
    # For every number "first" in numbers,
    # for every number "second" in numbers with index above index of "first",
    # for every number "third" in numbers with index above index of "third",
    # if the sum of "first", "second" and "third" is equal to 0 increment count

    index = range(len(numbers))
    count = 0

    # Get the three numbers
    for first_index in index:
        for second_index in index[first_index + 1:]:
            for third_index in index[second_index + 1:]:
                # if the sum of the three numbers is equal to 0 increment count
                if numbers[first_index] + numbers[second_index] + numbers[third_index] == 0:
                    count = count + 1  # print(numbers[i], numbers[j], numbers[k])
    return count


def three_sum(numbers):
    """(list) -> int

    Returns a count of any three elements of the list that sums up to zero
    """
    # For every number "first" in numbers,
    # for every number "second" in numbers with index above index of "first",
    # if the negative sum of "first" and "second" is in numbers indexed above the index of "second" increment count

    index = range(len(numbers))
    count = 0

    # Get two numbers
    for first_index in index:
        for second_index in index[first_index + 1:]:
            # increment count if the negative of sum is in rest of numbers
            if -(numbers[first_index] + numbers[second_index]) in numbers[second_index + 1:]:
                count = count + 1
    return count


if __name__ == "main":
    import unittest


    class MyTestCase(unittest.TestCase):
        def test_three_sum_bruteforce_1(self):
            self.assertEqual(three_sum_bruteforce([-5, -10, 0, -20, -40, 40, 30, 10, 25]), 5)

        def test_three_sum_1(self):
            self.assertEqual(three_sum_bruteforce([-5, -10, 0, -20, -40, 40, 30, 10, 25]), 5)
