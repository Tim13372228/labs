#Сибагатов Тимур ИПМбд 01-23 (лаб 8)

#Задание1
class A:
    variable1 = 1
    variable2 = 2

    @staticmethod
    def display():
        return f'variable1 = {A.variable1}, variable2 = {A.variable2}'

    @staticmethod
    def modify(v1, v2):
        A.variable1 = v1
        A.variable2 = v2

    @staticmethod
    def find_sum():
        return A.variable1 + A.variable2

    @staticmethod
    def find_max():
        return max(A.variable1, A.variable2)


A.modify(4, 5)
print(A.display())
print(A.find_sum())
print(A.find_max())


#Задание2
class Polynomial:
    def __init__(self, *coefficients: int):
        self._coefficients = tuple(coefficients)

    def __str__(self):
        out = str(self._coefficients[0]) if self._coefficients and self._coefficients[0] else ""
        for power, coefficient in enumerate(self._coefficients[1:], 1):
            if coefficient == 0:
                continue
            if out:
                out += " + " if coefficient > 0 else " - "
            if abs(coefficient) != 1:
                out += str(abs(coefficient))
            out += "x"
            if power > 1:
                out += f"^{power}"
        return out

    def __mul__(self, other: 'Polynomial'):
        result_coefficients = [0] * (len(self._coefficients) + len(other._coefficients) - 1)
        for i, coefficient1 in enumerate(self._coefficients):
            for j, coefficient2 in enumerate(other._coefficients):
                result_coefficients[i + j] += coefficient1 * coefficient2
        return Polynomial(*result_coefficients)


print(f'({Polynomial(1, 2, 3)}) * ({Polynomial(4, 5, 6)}) = {Polynomial(1, 2, 3) * Polynomial(4, 5, 6)}')



#Задание3
class Vector:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

    def add(self, other):
        return Vector(self.x_coord + other.x_coord, self.y_coord + other.y_coord, self.z_coord + other.z_coord)

    def subtract(self, other):
        return Vector(self.x_coord - other.x_coord, self.y_coord - other.y_coord, self.z_coord - other.z_coord)

    def dot_product(self, other):
        return self.x_coord * other.x_coord + self.y_coord * other.y_coord + self.z_coord * other.z_coord

    def length(self):
        return ((self.x_coord)**2 + (self.y_coord)**2 + (self.z_coord)**2)**0.5

    def cosine(self, other):
        return (self.dot_product(other)) / (self.length() * other.length())

v1 = Vector(2, 3, 4)
v2 = Vector(5, 3, 4)
v3 = v1.add(v2)
v4 = v1.subtract(v2)
res = v1.dot_product(v2)
res2 = v1.length()
res3 = v1.cosine(v2)
print(v3, v4, res, res2, res3)





#Задание 4
class Train:
    def __init__(self, departure, arrival, start_time, stop_time):
        self.departure = departure
        self.arrival = arrival
        self.start_time = start_time
        self.stop_time = stop_time

    def __add__(self, other):
        if self.arrival == other.departure and self.stop_time < other.start_time:
            departure = self.departure
            arrival = other.arrival
            start_time = self.start_time
            stop_time = other.stop_time
            return Train(departure, arrival, start_time, stop_time)
        else:
            print('Оперция сложения для этих поездов не доступна')


tr1 = Train('Москва', "Астрахань", 15.14, 22.15)
tr2 = Train("Астрахань", "Астана", 22.35, 23.59)
print(tr1 + tr2)
