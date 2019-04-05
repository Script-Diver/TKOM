# source.py
# zalozenie: przy inicjacji Source znak ustawiany jest na pierwsze miejsce


import os


class Source:
    def __init__(self, filename):
        self.line_number = 1
        self.position = 0
        self.file = open(filename, "r")
        self.character = self.get_next_char()
        print("Open")


    def __del__(self):
        self.file.close()
        print("Closed")


    def get_char(self):
        return self.character


    def get_line_number(self):
        return self.line_number


    def get_position(self):
        return self.position


    def get_next_char(self):
        self.character = self.file.read(1)
        if self.character == '#':
            while self.character != '\n' and self.character != '':
                self.character = self.file.read(1)
        if self.character == '\n':
            self.line_number += 1
            self.position = 0
        else:
            self.position += 1
        return self.character

# source = Source("../test/test.txt")
# print(f"{source.get_char()}, {source.get_line_number()}, {source.get_position()}")
# print(f"{source.get_next_char()}, {source.get_line_number()}, {source.get_position()}")
# print(f"{source.get_next_char()}, {source.get_line_number()}, {source.get_position()}")
# print(f"{source.get_next_char()}, {source.get_line_number()}, {source.get_position()}")
# print(f"{source.get_next_char()}, {source.get_line_number()}, {source.get_position()}")