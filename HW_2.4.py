user_line = input("Введите несколько слов через пробел для распознавания:\n>>> ")
user_list = user_line.split()
number_list = 1
for i in user_list:
    print(f"{number_list}) {i[0:10]}")
    number_list += 1