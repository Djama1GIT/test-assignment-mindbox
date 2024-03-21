import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный базовый класс для геометрических фигур.

    Определяет интерфейс для вычисления площади фигуры.
    """

    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры.

        Returns:
            float: Площадь фигуры.
        """
        raise NotImplemented


class Circle(Figure):
    """Класс для представления круга.

    Attributes:
        radius (float): Радиус круга.
    """

    def __init__(self, radius):
        """Инициализация круга с заданным радиусом.

        Args:
            radius (float): Радиус круга.
        """
        if radius <= 0:
            raise ValueError("Некорректное значение радиуса.")
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга.

        Returns:
            float: Площадь круга.
        """
        return math.pi * self.radius ** 2


class Triangle(Figure):
    """Класс для представления треугольника.

    Attributes:
        a (float): Длина стороны a.
        b (float): Длина стороны b.
        c (float): Длина стороны c.
    """

    def __init__(self, a, b, c):
        """Инициализация треугольника с заданными сторонами.

        Args:
            a (float): Длина стороны a.
            b (float): Длина стороны b.
            c (float): Длина стороны c.
        """
        if not self.is_valid(a, b, c):
            raise ValueError("Стороны не образуют треугольник.")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """Проверяет, образуют ли заданные стороны треугольник.

        Использует теорему о неравенстве треугольника.

        Args:
            a (float): Длина стороны a.
            b (float): Длина стороны b.
            c (float): Длина стороны c.

        Returns:
            bool: True, если стороны образуют треугольник, иначе False.
        """
        return a + b > c and a + c > b and b + c > a

    def area(self):
        """Вычисляет площадь треугольника.

        Использует формулу Герона.

        Returns:
            float: Площадь треугольника.
        """
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self):
        """Проверяет, является ли треугольник прямоугольным.

        Использует теорему Пифагора.

        Returns:
            bool: True, если треугольник прямоугольный, иначе False.
        """
        return self.a ** 2 + self.b ** 2 == self.c ** 2 or \
            self.a ** 2 + self.c ** 2 == self.b ** 2 or \
            self.b ** 2 + self.c ** 2 == self.a ** 2
