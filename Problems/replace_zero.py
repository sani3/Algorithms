# Write a function to replace zero with 5 in a digit
# Do not use strings, list or any such data structure

def replace_zero(number):
    result = 0
    i = 0
    sign = 1
    if number < 0:
        sign = -1
        number = abs(number)
    if number == 0:
        result = 5
        return result
    while not(number == 0):
        remainder = number % 10
        number = number // 10
        if remainder == 0:
            remainder = 5
        result = result + (remainder * 10**i)
        i += 1
    return sign * result

# time complexity O(N) = ~NlogN
# space complexity O(o) = 1
