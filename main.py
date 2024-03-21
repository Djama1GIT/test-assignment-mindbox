from mindbox import Circle, Triangle

# Пример использования
circle = Circle(5)
print(f"Площадь круга: {circle.area()}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area()}")
print(f"Треугольник прямоугольный: {triangle.is_right_angled()}")