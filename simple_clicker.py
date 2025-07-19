
# simple_clicker.py

score = 0

print("Добро пожаловать в простой кликер!")
print("Нажмите Enter, чтобы 'кликнуть'. Наберите 'exit', чтобы выйти.")

while True:
    user_input = input("Кликните (нажмите Enter) или 'exit': ").strip().lower()
    if user_input == "":
        score += 1
        print(f"Клики: {score}")
    elif user_input == "exit":
        print(f"Финальный счёт: {score}. Спасибо за игру!")
        break
    else:
        print("Неверный ввод. Нажмите Enter, чтобы кликнуть, или введите 'exit'.")
