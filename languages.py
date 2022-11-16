from enum import Enum


class Language:
    def __init__(self):
        self.year = None

    def read_from(self, stream):
        self.year = int(stream.readline().rstrip('\n'))

    def write_to(self, stream):
        stream.write(f'Year: {self.year}\n')

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
