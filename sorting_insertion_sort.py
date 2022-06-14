class Sorting:
    def __init__(self, data):
        self.data = data

    def is_sorted(self):
        """
        Returns True if self.data is sorted (ascending) and False if data is not sorted (ascending)
        :return: bool
        """
        for index in range(len(self.data) - 1):
            if self.data[index] > self.data[index + 1]:
                return False
        return True

    def swap(self, index1, index2):
        """
        Swaps the elements at index1 nd index2 of a list
        :param index1: number
        :param index2: number
        :return: None
        """
        dummy = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = dummy

    def insertion_sort(self):
        """
        Sort a list in-place (ascending)
        :return: None
        """
        for outer in range(len(self.data)):
            i = outer
            while self.data[i] < self.data[i-1] and i >= 1:
                self.swap(i, i - 1)
                i = i - 1
        # O(o) = ~(1/4)N**2


if __name__ != 'main':
    import unittest


    class SortingTest(unittest.TestCase):
        def test_sorting_1(self):
            s = Sorting([7, 10, 5, 3, 8, 4, 2, 9, 6, 1, 0])
            s.insertion_sort()
            self.assertEqual(s.is_sorted(), True)

        def test_sorting_2(self):
            s = Sorting(["k", "b", "j", "c", "i"])
            s.insertion_sort()
            self.assertEqual(s.is_sorted(), True)
