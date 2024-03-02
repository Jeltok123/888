def calculator():
    try:
        n1 = float(input("Введите число: "))
        operator = input("Выберите(+, -, *, /): ")
        n2 = float(input("Введите число: "))
        if operator == "+":
            result = n1 + n2
        elif operator == "-":
            result = n1 - n2
        elif operator == "*":
            result = n1 * n2
        elif operator == "/":
            if n2 == 0:
                print("Ошибка: Деление на ноль недопустимо.")
                return
            result = n1 / n2
        else:
            print("Ошибка: Неправильная операция. Выберите +, -, *, или /.")
            return
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: Введите корректные числа.")
if __name__ == "__main__":
    calculator()