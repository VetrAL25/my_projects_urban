class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        dom = super().__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return dom


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории.")


h1 = House('ЖК \"Горгиппия\"', 11)
print(House.houses_history)
h2 = House('ЖК \"Пляжный комплекс\"', 3)
print(House.houses_history)
h3 = House('ЖК \"Один, Два, Три\"', 5)
print(House.houses_history)
# h4 = House('Блэк Джек', 21)
# print(House.houses_history)

#del h1
del h2
del h3

print(House.houses_history)
