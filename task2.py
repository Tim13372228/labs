  #CибагатовТимурИПМбд01-23(2лаба)


#Задание1(базовое)
def symmetric(number):
    number_str = str(number).zfill(4)
    if number_str == number_str[::-1]:
        return 1
    else:
        return -1

pool = int(input("Введите четырехзначное число: "))
rez = symmetric(pool)
print(rez)

#Задание 2(базовое)
def years(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "YES"
    else:
        return "NO"

год = int(input("Введите год: "))
результат = years(год)
print(результат)

#Задание3(базовое)
def count(low):
    if low % 10 == 1 and low % 100 != 11:
        return "На лугу пасется " + str(low) + " корова"
    elif 2 <= low % 10 <= 4 and (low % 100 < 10 or low % 100 >= 20):
        return "На лугу пасется " + str(low) + " коровы"
    else:
        return "На лугу пасется " + str(low) + " коров"

number = int(input("Введите целое число: "))
output = count(number)
print(output)

#Задание 4.1(базовое)
chislo = int(input("Введите целое число, не меньшее 2: "))

for i in range(2, chislo + 1):
    if chislo % i == 0:
        print("Наименьший натуральный делитель, отличный от 1, равен", i)
        break


#Задание 4.2(базовое)


chislo= int(input("Введите целое число, не меньшее 2: "))
divisor = 2

while chislo % divisor != 0:
    divisor += 1

print("Наименьший натуральный делитель, отличный от 1, равен", divisor)

#Задание 5(базовое)

numbers = []
number = int(input("Введите целое неотрицательное число (или 0 для завершения ввода): "))
while number != 0:
    numbers.append(number)
    number = int(input("Введите следующее число: "))

print("Количество чисел в последовательности (без учета 0):", len(numbers))

operation = input("""
Выберите операцию:
1 - Найти сумму введенных чисел
2 - Найти произведение введенных чисел
3 - Найти среднее значение введенных чисел
4 - Найти максимальное число
5 - Найти минимальное число
6 - Определить количество четных и нечетных элементов
Введите номер операции: """)

if operation == "1":
    print("Сумма введенных чисел:", sum(numbers))
elif operation == "2":
    result = 1
    for num in numbers:
        result *= num
    print("Произведение введенных чисел:", result)
elif operation == "3":
    average = sum(numbers) / len(numbers)
    print("Среднее значение введенных чисел:", average)
elif operation == "4":
    print("Максимальное число:", max(numbers))
elif operation == "5":
    print("Минимальное число:", min(numbers))
elif operation == "6":
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    print("Количество четных элементов:", even_count)
    print("Количество нечетных элементов:", odd_count)
else:
    print("Некорректный ввод операции.")






