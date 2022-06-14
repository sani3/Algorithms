def fibonacci(n):
    """(number) -> list

    Return the fibonacci sequence.
    """
    
    # Starting with 0 and 1, subsequent elements of the sequence is a sum of the last two elements
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]

    assert n >= 0, "n must be a positive integer"
    result = [0, 1]
    if n == 0:
        return result[0]
    elif n == 1:
        return result[1]
    else:
        for i in range(2, n):
            result.append(sum(result[-2:]))
        return result


if __name__ == 'main':
    fibonacci(0)
    fibonacci(1)
    fibonacci(2)
    fibonacci(3)
    fibonacci(4)
    fibonacci(9)
    fibonacci(10)
