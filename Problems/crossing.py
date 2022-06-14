# You are crossing a river by stepping on stones,
# You can step across a stone or jump to move ahead two stones.
# Given  r stones, in how many ways, n, can you cross.

def n(r):
    # let the starting point be r = 0
    # There is only one way to get to the stone at r = 1 from r = 0
    # there is only one way to get to the stone at r = 2 from r = 0
    # You may not jump from r = 0, you may only jump from stone to stone
    # The end point is also a stone
    # Representation:                       = _ _ _ _ _ ...
    # Number of ways to get to stone n:     0 1 1 2 3 5 ...

    a = 0
    b = 1
    c = 0

    if r == 0:
        return a
    elif r == 1:
        return b
    else:
        for i in range(2, r + 1):
            c = a + b
            a = b
            b = c
        return c

# time complexity O(N) = ~N
# space complexity O(o) = 1
