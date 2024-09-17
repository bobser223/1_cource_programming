
list = []
def is_workable(num):
    if num < len(list):
        i = num
        while i > 0:
            if list[i] != -1:
                print(list[i])
                break
                return 0
            i -= 1

    else:
        max_i = 1
        for i in range(len(list), num+1):
            sq = str(i**2)
            str_i = str(i)
            if str_i == sq[-len(str_i):] :
                list.append(i)
                max_i = i
            else:
                list.append(-1)
        print(max_i)



is_workable(100000000)
for i in list:
    if i != -1:
        print(i)

