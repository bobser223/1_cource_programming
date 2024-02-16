# import requests
#
# def read_from_github(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         content = response.json()["blob"]["rawLines"]
#         return "\n".join(content)
#     else:
#         print("Failed to read file from GitHub")
#         return None
#
# # Приклад виклику функції
# github_url = "https://raw.githubusercontent.com/krenevych/oop/master/labs/lab01/aud/task1/input01.txt"
# file_content = read_from_github(github_url)
# if file_content:
#     print(file_content)
#
# from f1 import Quad
#
#
# with open("input01.txt", "rt") as f:
#     solution_list = []
#     while True:
#         try:
#             str_of_coef = f.readline()
#             list_of_coef = str_of_coef.split()
#             # for i in range(len(list_of_coef)):
#             #     list_of_coef[i] = float(list_of_coef[i])
#             list_of_coef = list(map(float, list_of_coef))
#             a = list_of_coef[0]
#             b = list_of_coef[1]
#             c = list_of_coef[2]
#             eq = Quad(a, b, c)
#             solution_list.append(eq)
#             print(eq.solution())
#         except IndexError:
#             break
counter = 0
for i in range(121):
    if i % 3 == 0 and (120 - i) % 4 == 0:
        counter += 1
        print(i)
print(counter)