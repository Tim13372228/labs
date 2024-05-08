#CибагатовТимурИПМбд01-23(1 лаба)


#Задание1(базовое)
x=2
x=x+3
print(x,type(x))
x=(x+1)/2
print(x,type(x))
x=x+1/2
print(x,type(x))
x=x<5
print(x,type(x))
x=str(x)
print(x,type(x))

#Задание2(базовое)
summa=1+2+3+4+5
srednee=summa/5
print(f"Среднее значение этих 5 чисел равно {srednee:.5f}")

#Задание3(базовое)
summa = 1 + 2 + 3 + 4 + 5
srednee = summa / 5
print(f"Среднее значение этих 5 чисел равно {srednee:.5f}")
new = float(input('Введите новое число'))
kolvo = 5
while new != 0:
    summa = summa + new
    kolvo += 1
    srednee = summa / kolvo
    print(f"Среднее значение этих {kolvo} чисел равно {srednee:.5f}")
    new = float(input('Введите новое число '))


#Дополнительное задание(число и цифра)
a = int(input('Введите целое число'))
b = 0
while a != 0:
    b += a % 10
    a  = a // 10
print(b)


#ДопЗадание(Максимум и минимум)

num = int(input('Введите количество чисел: '))

if num <= 0:
    print("Вы ввели некорректное количество чисел.")
else:
    minimum = maximum = int(input(f'Введите число №1: '))

    for i in range(2, num + 1):
        x = int(input(f'Введите число №{i}: '))
        maximum = max(maximum, x)
        minimum = min(minimum, x)

    print('Максимум - {}, минимум - {}'.format(maximum, minimum))

#Дополнительное задание (Без всяких условносей)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(f'Максимальное из двух чисел равно {int((a + b + abs(a - b)) / 2)}.')


