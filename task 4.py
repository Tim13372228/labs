 #CибагатовТимурИПМбд01-23(3лаба)

#Задание1(базовое)
def task1(x):
    return (((99 < x < 1000) and (x % 10 == 0)) or
            ((x % 2 != 0) and ((x % 3 == 0) or (x % 5 == 0))) or
            (2 <= x <= 6) or
            ((99 < x < 1000) and (len(set(str(x))) == 1)))

print(task1(int(input('Введите число: '))))

#Задание 2(базовое)
def true(x):
    return (abs(x) + 5 > 3)
def false(x):
    return (abs(x) + 5 < 3)

num = int(input("Введите номер: "))

print(true(num))
print(false(num))

#Заданние 3(базовое)

def a(x, y):
    return (x >= 4 and y >= 3) or (x < 4 and y < 3 and x + y <= 0)
def b(x, y):
    return (3 - abs(x) >= 0) and (3 - abs(y) >= 0) and (x ** 2 + y ** 2 >= 9)
def c(x, y):
    return (0 <= x <= 5) and (0 <= y <= 5) and ((x - 5) ** 2 + (y - 5) ** 2 >= 25)
x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))

print(a(x, y))
print(b(x, y))
print(c(x, y))


#Задание 4(базовое)
def test():
    x = int(input("Enter a number: "))
    if x >= 0:
        print(positive(x))
    else:
        print(negative(x))

def positive(x):
    return 'Положительное'

def negative(x):
    return 'Отрицательное'

test()



#Задание 5(базовое)
def getInput():
    return input("Введите строку: ")

def testInput(x):
    try:
        int(x)
        return True
    except:
        return False

def strToInt(x):
    return int(x)

def printInt(x):
    print(x)

x = getInput()
if testInput(x):
    printInt(strToInt(x))