
class RationalListIterator:
    def __init__(self, list_of_rational_numbers):
        self.list_of_rational_numbers_non_changed = tuple(list_of_rational_numbers.list)
        self.list_of_rational_numbers = list_of_rational_numbers.list
        self.list_of_rational_numbers.sort()
        self.list_of_rational_numbers.reverse() #Business logic
        self.index = 0


    def __next__(self):
        try:
            # current = self.list_of_rational_numbers_non_changed.index(self.list_of_rational_numbers[self.index])
            current = self.list_of_rational_numbers[self.index]
            self.index += 1
            return current
        except IndexError:
            raise StopIteration

    # @staticmethod
    # def list_with_correct_order(list_of_rational_numbers):
    #     new_list = []
    #     while len(list_of_rational_numbers) > 0:
    #         max_el = list_of_rational_numbers[0]
    #         max_el_index = list_of_rational_numbers.index()
    #         for i in range(len(list_of_rational_numbers)):


