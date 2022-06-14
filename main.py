import timeit
timeit.timeit("three_sum_bruteforce(a)",
              setup='''from three_sum import three_sum_bruteforce
a = [30, -40, -20, -10, 40, 0, 10, 5, 25, 50, 35, 15, -35, -25]
def three_sum_brute_force(a):
    a_length = range(len(a))
    count = 0
    for i in a_length:
        for j in a_length[i + 1:]:
            for k in a_length[j + 1:]:
                if a[i] + a[j] + a[k] == 0:
                    count = count + 1
                    # print(a[i], a[j], a[k])
    return count'''
              )


