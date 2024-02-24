from collections import Counter

def most_common(lst):
    counts = Counter(lst)
    most_common_element = max(counts, key=counts.get)
    return most_common_element

# Приклад використання
my_list = [1, 2, 3, 2, 2, 4, 5, 2, 3, 3]
result = most_common(my_list)
print("Найчастіше зустрічається елемент:", result)