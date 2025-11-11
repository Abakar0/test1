def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите число!")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Ошибка: деление на ноль!":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            next_calculation = input("Хотите выполнить ещё одну операцию? (да/нет): ")
            if next_calculation.lower() != 'да':
                print("Выход из калькулятора.")
                break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

if __name__ == "__main__":
    calculator()