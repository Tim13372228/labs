 #CибагатовТимурИПМбд01-23(4 лаба)


#Задание1(базовое)

a = input('Введите первое значение: ')
b = input('Введите второе значение: ')

if testInput(a) and testInput(b):
    print(int(a) + int(b))
else:
    print(a + b)




 #задание 2(базовое)
n = int(input('Введите число гостей: '))
# Каждому гостю достался хотя бы 1 кусок
k1 = 1
while k1 < n:
    k1 += 1
    if k1 >= n:
        break
print('Чтобы всем досталось по куску, пирог разделили на', k1, 'кусков.')
k2 = 1
while k2 < (n + n / 2):
    k2 += 1
    if k2 >= (n + n / 2):
        break
print('Чтобы хотя бы половине гостей досталось по 2 куска, пирог разрезали на', k2, 'кусков.')


#Задание 3(базовое)

from math import sqrt as sq

epsilon = float(input('Введите число, на которое должны отличаться значения (например, 0.001): '))

def Fibonacci(n):
    fib = [0] * max(2, n)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n - 1]

def ClearFibonacci(n):
    return (((1 + sq(5)) / 2) ** n - ((1 - sq(5)) / 2) ** n) / sq(5)

def calculator():
    n = 1
    while True:
        if abs(Fibonacci(n) - ClearFibonacci(n)) >= epsilon:
            return print(f'n, начиная с которого, отличие от истинного значения превысит {epsilon} равен {n}')
        n += 1

calculator()


#Задание 4(базовое)

n, m = int(input('Введите количество детей: ')), int(input('Введите количество кубиков: '))

def listGenerator(init = 1, max = 25):
    sequence = []
    while init not in sequence:
        if init <= max:
            sequence.append(init)
        else:
            init -= max
            if init in sequence:
                break
            sequence.append(init)
        init *= 2
    return sequence

def Kids(m, n):
    init = 1
    max = 25
    sequence = listGenerator(init, max)
    currentStep = 0
    while m >= 0:
        m -= sequence[currentStep % len(sequence)]
        currentStep += 1
    return (currentStep) % n or n

print(f'Проиграет {Kids(m, n)}-й ребенок')



#Задание 5(базовое)
#Через рекурсию
def move(n, x, y):
    if n == 1:
        print(f'Переложить диск 1 со стержня {x} на стержень {y}')
    else:
        z = 6-x-y
        move(n-1, x, z)
        print(f'Переложить диск {n} со стержня {x} на стержень {y}')
        move(n-1, z, y)
