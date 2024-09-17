def is_in(n):
    sq = str(n ** 2)
    str_n = str(n)
    if str_n == sq[-len(str_n):]:
        return True
    return False

lst = [5, 6]
def foo(n):
    if n < 5:
        print(1)
        return

    b = lst[-1]
    a = lst[-2]
    i = 10
    c = 0
    d = 0
    first = 1
    while lst[-1] <= n:
        if first == 1:
            a += i
            b += i
            first = 0
        if a not in lst:
            a += i
        if b not in lst:
            b += i
        if is_in(a) and a not in lst:
            lst.append(a)
        if is_in(b) and b not in lst:
            lst.append(b)

        if a in lst and b in lst:
            i *=10
            b = lst[-1]
            a = lst[-2]
            first = 1
    print(lst[-2])

a = int(input())
foo(a)

