def func(a):
    for num in range(a, 0, -1):
        sqrNum = num ** 2
        sqrNum = str(sqrNum)
        sqrNum = list(sqrNum)
        sqrNum.reverse()
        num_string = str(num)
        num_string = list(num_string)
        num_string.reverse()
        for i in range(len(num_string)):
            if num_string[i] != sqrNum[i]:
                break
        else:
            return num






n = int(input())
print(func(n))