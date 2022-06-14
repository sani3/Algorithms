def mergesort(array):
    """(list) -> list

    Return a sorted list of an input list: both halves of the input list are themselves sorted
    """

    # getting the mid is tricky
    mid = (len(array) // 2) - 1 + len(array) % 2
    j = 0
    k = mid + 1
    new_array = [None] * len(array)

    # must assert to validate mid
    assert array[:mid] == sorted(array[:mid]), "The first half of list must be sorted"
    assert array[k:] == sorted(array[k:]), "The second half of list must also be sorted"

    # the rest is reasonable
    for i in range(len(array)):
        if j <= mid and k <= len(array):
            if array[j] <= array[k]:
                new_array[i] = array[j]
                j = j + 1
            elif array[j] > array[k]:
                new_array[i] = array[k]
                k = k + 1
        elif k > len(array):
            new_array[i] = array[j]
            j = j + 1
        elif j > mid:
            new_array[i] = array[k]
            k = k + 1

    return new_array

# O(o) = Nlg(N)
