x = 28
k = 1


a = x
a0 = -(x ** 2) * (2*k - 1)
print(a0)
a1 = (k * (2*k + 1))
print(a1)
a3 = a0 / a1
print(a3)
a *= (-(x ** 2) * (2*k - 1)) / (k * (2*k + 1))

print(a)