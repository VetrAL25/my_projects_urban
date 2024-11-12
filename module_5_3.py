class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# h1 = House('Горгиппия', 11)
# h2 = House('Пляжный комплекс', 3)
# h3 = House('Один, Два, Три', 5)
#
# # __str__
# print(h1)
# print(h2)
# print(h3)
#
# # __len__
# print(len(h1))
# print(len(h2))
# print(len(h3))



    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('Горгиппия', 11)
h2 = House('Пляжный комплекс', 3)
h3 = House('Один, Два, Три', 5)
h4 = House('Блэк Джек', 21)

print(h1)
print(h2)
print(h3)
print(h4)

print(h1 == h2)  # __eq__

h2 = h2 + 2  # __add__
print(h2)
print(h2 == h3)

h2 += 6  # __iadd__
print(h2)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h4 != h2)  # __ne__