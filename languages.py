from enum import Enum


class Language:
    def __init__(self):
        self.year = None
        self.references = None

    def read_from(self, stream):
        self.year = int(stream.readline().rstrip('\n'))
        self.references = int(stream.readline().rstrip('\n'))

    def write_to(self, stream):
        stream.write(f'Year: {self.year}\n')
        stream.write(f'Years passed: {self.years_passed()}\n')
        stream.write(f'References: {self.references}\n')

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        if k == 1:
            language = Procedure()
        elif k == 2:
            language = ObjectOriented()
        else:
            stream.close()
            raise Exception('Error type')

        language.read_from(stream)
        return language

    def years_passed(self):
        return 2022 - self.year

    def compare(self, other):
        return self.years_passed() < other.years_passed()

    def write_to_procedure(self, stream):
        pass


class Procedure(Language):
    def __init__(self):
        super().__init__()
        self.has_abstract_type = None

    def read_from(self, stream):
        super().read_from(stream)
        self.has_abstract_type = bool(stream.readline())

    def write_to(self, stream):
        stream.write('[Procedure language]\n')
        stream.write(f'Has abstract type: {self.has_abstract_type}\n')
        super().write_to(stream)

    def write_to_procedure(self, stream):
        self.write_to(stream)


class ObjectOriented(Language):
    def __init__(self):
        super().__init__()
        self.inheritance_type = None

    def read_from(self, stream):
        super().read_from(stream)
        self.inheritance_type = int(stream.readline())

    def write_to(self, stream):
        stream.write('[OOP language]\n')
        stream.write(f'Inheritance type: {self.inheritance_type}\n')
        super().write_to(stream)


class InheritanceTypes(Enum):
    Single = 1
    Multiple = 2
    Interface = 3
