import math

def find_max_num(vec, str_):
    max_n = -1
    max_i = -1

    start = 0 if str_[0] == 'r' else 1

    for i in range(start, len(vec)):
        if str_[i] == 'r' and i < len(vec) - 1 and vec[i] >= max_n and vec[i] >= vec[i + 1]:
            max_n = vec[i]
            max_i = i
            pos = 1
        elif str_[i] == 'l' and vec[i] > max_n and vec[i] > vec[i - 1]:
            max_n = vec[i]
            max_i = i
            pos = -1

    if max_n == -1 and max_i == -1:
        return -1, -1, -1

    for i in range(len(vec)):
        if vec[i] > max_n:
            if str_[i] == 'l':
                str_[i] = 'r'
            elif str_[i] == 'r':
                str_[i] = 'l'

    return max_n, max_i, pos

def SHDT(num):
    vect = []
    if num == 1:
        print(1)
        vect.append([1])
        return vect

    vec = list(range(1, num + 1))
    str_ = ['l'] * num

    print(*vec)
    vect.append(vec.copy())
    while True:
        max_num, max_iter, pos_pointer = find_max_num(vec, str_)
        if max_iter == -1 and max_num == -1:
            break
        vec[max_iter], vec[max_iter + pos_pointer] = vec[max_iter + pos_pointer], vec[max_iter]
        str_[max_iter], str_[max_iter + pos_pointer] = str_[max_iter + pos_pointer], str_[max_iter]

        vect.append(vec.copy())

        print(*vec)
    return vect

def count_inversions(perm):
    inv_count = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                inv_count += 1
    return inv_count

def find_permutations_with_inversions(permutations, num_inversions):
    found = False
    for perm in permutations:
        if count_inversions(perm) == num_inversions:
            print(*perm)
            found = True
    if not found:
        print(f"Немає перестановок з {num_inversions} інверсіями.")

if __name__ == "__main__":
    num = int(input("Введіть число елементів у перестановках: "))
    permutations = SHDT(num)
    inv_num = int(input("Введіть кількість інверсій: "))
    print(f"\nПерестановки з {inv_num} інверсіями:")
    find_permutations_with_inversions(permutations, inv_num)
