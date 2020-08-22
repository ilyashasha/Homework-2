# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

random_list = [2, 'up', 6, 'down', 9, 15, 'fifty', 60]
print(random_list)

random_list.append(6)
random_list.append(15)
print(random_list)

add_list = [80, 90, 100]
random_list.extend(add_list)
print(random_list)

random_list.insert(0, 1)
print(random_list)

random_list.remove(9)
print(random_list)

print(random_list.index(6))

print(random_list.count(15))

random_list.reverse()
print(random_list)

print(type(random_list))

for i in random_list:
    print(f"{i} - {type(i)}")
