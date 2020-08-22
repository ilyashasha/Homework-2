my_list = [9, 2, 1, 8, 3]

print(f"Актуальный рейтинг: {str(my_list)[1:-1]}\n")

while True:
    user_answer = input("Для выхода из программы введите: exit\nВведите новый элемент рейтинг: ")
    if user_answer == 'exit':
        print("\nПрограмма закончена! Всего доброго!")
        break
    user_answer = int(user_answer)
    my_list.append(user_answer)
    my_list.sort()
    my_list.reverse()
    print(f"Новый рейтинг: {str(my_list)[1:-1]}\n")
