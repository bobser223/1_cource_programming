import math
def buzz(number_we_need):
    sequence_length = 0
    current_square = 1
    n = 1
    while number_we_need >= sequence_length:

        current_number_length = int(math.log10(current_square)) + 1
        if sequence_length + current_number_length >= number_we_need:
            return int(str(current_square)[number_we_need - sequence_length - 1]) # I can use a generator, but it's senseless
        sequence_length += current_number_length
        current_square = current_square + 2 * n + 1

        n += 1

# numeration starts from 1, not 0
def number_reconstructor(n):
    while n > 0:
        number = n % 10
        n //= 10
        yield number



def buz(number_we_need):
    sequence_length = 0
    current_square = 1
    n = 1
    while number_we_need >= sequence_length:

        current_number_length = int(math.log10(current_square)) + 1
        if sequence_length + current_number_length >= number_we_need:
            i = 1
            for number in number_reconstructor(current_square):
                current_index = current_number_length - (number_we_need - sequence_length - 1)
                if i == current_index:
                    return number
                i += 1
        sequence_length += current_number_length
        current_square = current_square + 2 * n + 1

        n += 1


print(buz(100))
print(buzz(100))