class Alphabet:
    def __init__(self):
        self.string = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.R = len(self.string)

    def to_index(self, char):
        for index, key in enumerate(self.string):
            if char == key:
                return index

    def to_char(self, place):
        for index, key in enumerate(self.string):
            if place == index:
                return key


def least_significant_digit_sort(str_list):
    """(list) -> list

    return sorted list of str_list.
    """

    width = len(str_list[0])

    width_test = True

    for i in str_list:
        if len(i) != width:
            width_test = False

    assert width_test, "All elements of str_list must have the same length"

    # the characters of alphabets of base R
    alphabets = Alphabet()

    result = [0] * len(str_list)

    for place_value in range(width - 1, -1, -1):

        # accumulator for frequency count
        count = [0] * (alphabets.R + 2)

        # compute frequency of values
        for i in range(len(str_list)):
            count[alphabets.to_index(str_list[i][place_value]) + 1] += 1

        # compute cumulative frequency (transforms count to indices)
        for i in range(len(count) - 1):
            count[i + 1] = count[i + 1] + count[i]

        # for each element k at index i of int_list (k = int_list[i]),
        #   set item at index count[k] of result to the element k
        #   increment count[k] by 1
        for i in range(len(str_list)):
            # item = str_list[i]
            # digit = alphabets.to_index(item[place_value])
            # result[count[digit]] = item
            # count[digit] = count[digit] + 1

            result[count[alphabets.to_index(str_list[i][place_value])]] = str_list[i]
            count[alphabets.to_index(str_list[i][place_value])] += 1

        str_list = result.copy()

    return result


if __name__ != 'main':
    data = ['AB124', 'KD354', 'LG112', 'KG352', 'SK871', 'BA611', 'YO100', 'NG200', 'BA418']
    print(least_significant_digit_sort(data))
