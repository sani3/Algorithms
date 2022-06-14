import random


def swap(data, a, b):
    dummy = data[a]
    data[a] = data[b]
    data[b] = dummy
    return data


def shuffle(data):
    """(list) -> list

    Returns a uniform random shuffle of the input list
    """
    for i in range(len(data)):
        rand_int = random.randint(0, i)
        swap(data, i, rand_int)
    return data
