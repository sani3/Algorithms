# Write a function to return the k largest elements in an array
# in the order largest to smallest

# def largest_three(numbers):
#     numbers.sort(reverse=True)
#     return numbers[:3]


def max_index(numbers):
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            return i


def swap(numbers, index1, index2):
    dummy = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = dummy
    return numbers


def selsort(numbers):
    for i in range(len(numbers) - 1):
        max_index_of_rest = max_index(numbers[i + 1:]) + 1 + i
        if numbers[max_index_of_rest] > numbers[i]:
            swap(numbers, i, max_index_of_rest)
    return numbers[:3]
    # O(~N**2)


if __name__ != 'main':
    selsort([2, 8, 4, 9, 4, 6, 12])
    # see ds_queue_priority_binary_heap.py
