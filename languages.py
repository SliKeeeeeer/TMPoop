from enum import Enum
import sys


class Language:
    def __init__(self):
        self.year = None
        self.references = None

    def read_from(self, stream):
        try:
            self.year = int(stream.readline().rstrip('\n'))
        except Exception:
            print('Reading year error')
            stream.close()
            sys.exit(1)

        try:
            self.references = int(stream.readline().rstrip('\n'))
        except Exception:
            print('Reading references error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f'Year: {self.year}\n')
            stream.write(f'Years passed: {self.years_passed()}\n')
            stream.write(f'References: {self.references}\n')
        except Exception:
            print('Writing to file error')
            stream.close()
            sys.exit(1)

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
        except Exception:
            print('Conversion to int error')
            stream.close()
            sys.exit(1)

        if k == 1:
            language = Procedure()
        elif k == 2:
            language = ObjectOriented()
        elif k == 3:
            language = Functional()
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

    @staticmethod
    def check_languages(language_1, language_2):
        match language_1, language_2:
            case Procedure(), Procedure():
                print("Languages are the same type: Procedure and Procedure")

            case Procedure(), Functional():
                print("Languages are different type: Procedure and Functional")

            case Procedure(), ObjectOriented():
                print("Languages are different type: Procedure and ObjectOriented")

            case Functional(), Procedure():
                print("Languages are different type: Functional and Procedure")

            case Functional(), Functional():
                print("Languages are the same type: Functional and Functional")

            case Functional(), ObjectOriented():
                print("Languages are different type: Functional and ObjectOriented")

            case ObjectOriented(), Procedure():
                print("Languages are different type: ObjectOriented and Procedure")

            case ObjectOriented(), Functional():
                print("Languages are different type: ObjectOriented and Functional")

            case ObjectOriented(), ObjectOriented():
                print("Languages are the same type: ObjectOriented and ObjectOriented")

            case _:
                print('Unknown type')
                return

        print(f"First: {language_1}, second: {language_2}")
        print()


class Procedure(Language):
    def __init__(self):
        super().__init__()
        self.has_abstract_type = None

    def read_from(self, stream):
        super().read_from(stream)
        try:
            self.has_abstract_type = bool(stream.readline())
        except Exception:
            print('Reading bool error')
            stream.close()
            sys.exit(1)

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
        try:
            self.inheritance_type = int(stream.readline())
        except Exception:
            print('Reading int error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        stream.write('[OOP language]\n')
        stream.write(f'Inheritance type: {self.inheritance_type}\n')
        super().write_to(stream)


class Functional(Language):
    def __init__(self):
        super().__init__()
        self.typification = None
        self.has_lazy_evaluation = None

    def read_from(self, stream):
        super().read_from(stream)
        try:
            self.typification = int(stream.readline())
        except Exception:
            print('Reading int error')
            stream.close()
            sys.exit(1)

        try:
            self.has_lazy_evaluation = bool(stream.readline())
        except Exception:
            print('Reading bool error')
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        stream.write('[Functional language]\n')
        stream.write(f'Inheritance type: {self.typification}\n')
        stream.write(f'Has lazy evaluation: {self.has_lazy_evaluation}\n')
        super().write_to(stream)


class InheritanceTypes(Enum):
    Single = 1
    Multiple = 2
    Interface = 3


class Typifications(Enum):
    Strongly = 1
    Weakly = 2
