from Student import Student


class NaturalStudent(Student):
    def __init__(self, name: str, credits_required: int, uah: float):
        super().__init__(name, credits_required, uah)

    def teach_humanitarian(self, teacher, credits: int) -> None:
        teacher.teach_humanitarian(self, credits)

    def teach_natural(self, teacher, credits: int) -> None:
        teacher.teach_natural(self, credits)

    def __str__(self):
        return (f'Natural student {self.name}, credits required: {self.credits_required}, money left: {self.uah}'
                f', number of learned subjects: {self.natural_count + self.humanities_count}')