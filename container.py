from languages import Language


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Container:
    def __init__(self):
        self.start_node = None
        self.size = 0

    def push_back(self, data):
        if self.start_node is None:
            self.start_node = Node(data)
        else:
            n = self.start_node
            while n.next is not None:
                n = n.next
            n.next = Node(data)

        self.size += 1

    def read_from(self, stream):
        while line := stream.readline():
            item = Language.create_from(stream, line)
            self.push_back(item)

    def write_to(self, stream):
        stream.write(f'Container has {self.size} elements\n')

        if self.start_node != None:
            n = self.start_node
            while n is not None:
                n.data.write_to(stream)
                n = n.next

    def clear(self):
        self.start_node = None
        self.size = 0

    def sort(self):
        if self.start_node is None:
            print('Empty list')
        else:
            n1 = self.start_node
            n2 = self.start_node
            while n1 is not None:
                while n2 is not None:
                    if n1.data.compare(n2.data):
                        n1.data, n2.data = n2.data, n1.data
                    n2 = n2.next
                n1 = n1.next
                n2 = self.start_node

    def __iter__(self):
        return self.next

    def check_languages(self):
        languages_1 = []
        n = self.start_node
        while n is not None:
            languages_1.append(n.data)
            n = n.next

        languages_2 = languages_1.copy()

        for language_1 in languages_1:
            for language_2 in languages_2:
                Language.check_languages(language_1, language_2)

    def write_to_procedure(self, stream):
        print("Only procedure languages")

        n = self.start_node
        while n is not None:
            n.data.write_to_procedure(stream)
            n = n.next

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.start_node)
