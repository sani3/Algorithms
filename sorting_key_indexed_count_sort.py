def key_indexed_count_sort(int_list):

    """(list) -> list

    return sorted list of int_list
    """

    result = [0] * len(int_list)

    # accumulator for frequency count
    count = [0] * (max(int_list) + 2)

    # compute frequency of values
    for i in range(len(int_list)):
        count[int_list[i] + 1] = count[int_list[i] + 1] + 1

    # compute cumulative frequency (transforms count to indices)
    for i in range(len(count) - 1):
        count[i + 1] = count[i + 1] + count[i]

    # for each element k at index i of int_list (k = int_list[i]),
    #   set item at index count[k] of result to the element k
    #   increment count[k] by 1
    for i in range(len(int_list)):
        result[count[int_list[i]]] = int_list[i]
        count[int_list[i]] += 1

    return result


if __name__ != 'main':
    data = [2, 3, 3, 4, 1, 3, 4, 3, 1, 2, 2, 1, 2, 4, 3, 4, 4, 2, 3, 4]
    print(key_indexed_count_sort(data))
