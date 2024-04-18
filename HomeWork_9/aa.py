# (n + 1)**2 = n**2 +2n + 1

# n++
# a0 = n(1)**2
# (n + 1)**2 = a0 + 2*n + 1

n = 1
a0 = 1
while n < 999999:
    a1 = a0 + 2*n + 1
    a0 = a1
    n += 1
    # defolt_square = n ** 2
    # if defolt_square != a0:
    #     print(defolt_square, a0, n)


