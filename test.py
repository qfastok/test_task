import random

# вивести суму кожного 3, 5, 9 елемента від 0 - 100
for i in [3, 5, 9]:
    print(sum(range(1, 101, i)))

# Є словник | ключ- без різниці | value - 20 елементів інтові
# | вивести ключі трьох найбільший значень в порядку зростання значень
my_dict = dict((key, random.randint(0, 100)) for key in range(20))
print(my_dict)

res = sorted(my_dict.items(),
             key=lambda item: item[1])[len(my_dict) - 3:len(my_dict):]
for k, _ in res:
    print(k)

