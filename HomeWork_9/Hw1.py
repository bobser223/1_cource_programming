#123456789101112131415161718192021

import math

def buzz(number_we_need):
    sequence_length = 0
    current_number = 1
    while number_we_need >= sequence_length:

        current_number_length = int(math.log10(current_number)) + 1
        if sequence_length + current_number_length >= number_we_need:
            return int(str(current_number)[number_we_need - sequence_length - 1])
        sequence_length += current_number_length

        current_number += 1


print(buzz(99))

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
                current_index = current_number_length - (number_we_need - sequence_length - 1)
                if i == current_index:
                    return number
                i += 1

        sequence_length += current_number_length

        current_number += 1

