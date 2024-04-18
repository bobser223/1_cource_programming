import math
# def expand_number(number):
#     length = 0
#     while number > 0:
#         remainder = number % 10
#         number = number // 10
#         length += 1
#         yield remainder
#
# def length(number):
#     return math.floor(math.log10(abs(number))) + 1
#
# print(expand_number(12))
# print(length(1))
# for number in expand_number(12):
#     print(number)
# def expand_number(number):
#     length = 0
#     while number > 0:
#         remainder = number % 10
#         number = number // 10
#         length += 1
#         yield remainder

# def find_digit_in_natural_numbers(k):
#     if k <= 0:
#         return -1
#     number = 1
#     total_length = 0
#     while True:
#         current_length = math.floor(math.log10(number)) + 1
#         if total_length + current_length >= k:
#             return int(str(number)[k - total_length - 1])
#         total_length += current_length
#         number += 1
def number_reconstructor(n):
    while n > 0:
        number = n % 10
        n //= 10
        yield number

def buz(number_we_need):
    sequence_length = 0
    current_number = 1
    while number_we_need >= sequence_length:

        current_number_length = int(math.log10(current_number)) + 1
        if sequence_length + current_number_length >= number_we_need:
            i = 1
            for number in number_reconstructor(current_number):
                iter = current_number_length - (number_we_need - sequence_length - 1)
                if i == iter:
                    return number
                i += 1

        sequence_length += current_number_length

        current_number += 1

def buzz(number_we_need):
    sequence_length = 0
    current_number = 1
    while number_we_need >= sequence_length:

        current_number_length = int(math.log10(current_number)) + 1
        if sequence_length + current_number_length >= number_we_need:
            return int(str(current_number)[number_we_need - sequence_length - 1])
        sequence_length += current_number_length

        current_number += 1

n = int(input())
print(buzz(n))
print(buz(n))

# for n in number_reconstructor(100):
#     print(n)


