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

    # base R. here R = 10, the characters of base 10 are 0 - 9
    alphabets = 10

    result = [0] * len(str_list)

    for place_value in range(width - 1, -1, -1):

        # accumulator for frequency count
        count = [0] * (alphabets + 2)

        # compute frequency of values
        for i in range(len(str_list)):
            count[int(str_list[i][place_value]) + 1] += 1

        # compute cumulative frequency (transforms count to indices)
        for i in range(len(count) - 1):
            count[i + 1] = count[i + 1] + count[i]

        # for each element k at index i of int_list (k = int_list[i]),
        #   set item at index count[k] of result to the element k
        #   increment count[k] by 1
        for i in range(len(str_list)):
            # item = str_list[i]
            # digit = int(item[place_value])
            # result[count[digit]] = item
            # count[digit] = count[digit] + 1

            result[count[int(str_list[i][place_value])]] = str_list[i]
            count[int(str_list[i][place_value])] += 1

        str_list = result.copy()

    return result


if __name__ != 'main':
    data = ['124', '354', '112', '352', '871', '611', '100', '200', '418']
    print(least_significant_digit_sort(data))
