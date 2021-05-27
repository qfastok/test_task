import random

# вивести суму кожного 3, 5, 9 елемента від 0 - 100
for i in [3, 5, 9]:
    print(sum(range(0, 100, i)))

# Є словник | ключ- без різниці | value - 20 елементів інтові
# | вивести ключі трьох найбільший значень в порядку зростання значень
my_dict = {}

for i in range(20):
    my_dict[i] = random.randint(0, 100)

print(my_dict)

for i in range(17):
    my_dict.pop(min(my_dict, key=my_dict.get))

for i in range(3):
    max_val = max(my_dict, key=my_dict.get)
    print(max_val)
    my_dict.pop(max_val)

