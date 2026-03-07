import math
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
print("Использовать калькулятор? [y/n] ")
input()
message = '''1. Сложение 2. Вычитание 3. Умножение 4. Корень 5. Степень '''
operation = input(message)

print("Первое число: ", n1)
print("Второе число: ", n2)
if operation == "1":
    result = n1 + n2
elif operation == "2":
    result = n1 - n2
elif operation == "3":
    result = n1 * n2
elif operation =="4":
    result = math.sqrt(n1)
elif operation == "5":
    result = n1 ** n1
print("Ваш результат:", result)
