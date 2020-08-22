season_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

user_answer = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if user_answer > 13:
    print("Внимательно читайте условия ввода!")
for key, value in season_dict.items():
    if user_answer in value:
        print(f'Ваша цифра ссотвествует времени года: {key}')
        break
