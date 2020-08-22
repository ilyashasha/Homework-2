size_list = int(input("Введите желаемое количество элементов в списке: "))
user_list = []
number_list = 1
for i in range(size_list):
    user_answer = input(f"Введите {number_list}-й элемент списка: ")
    user_list.append(user_answer)
    number_list += 1
print(f"Ваш список: \n{user_list}")

number_list = 0
while number_list < len(user_list[:-1]):
    user_list[number_list], user_list[number_list + 1] = user_list[number_list + 1], user_list[number_list]
    number_list +=2
print(f"Измененный список:\n{user_list}")
