# main_module.py
import math
from abc import ABC, abstractmethod

# Базовый класс для всех фигур
class Shape(ABC):
    @abstractmethod
    def is_valid(self) -> tuple[bool, str]:
        """Проверяет корректность фигуры."""
        pass
    @abstractmethod
    def area(self) -> tuple[bool, str, float]:
        """Вычисляет площадь фигуры."""
        pass
    @abstractmethod
    def GetParameters(self):
        """Запрашивает у пользователя параметры фигуры."""
        pass        

# Класс для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def is_valid(self) -> tuple[bool, str]:
        try:
            radius = float(self.radius)
        except ValueError:
            return False, "Радиус должен быть числом."
        if radius <= 0:
            return False, "Радиус должен быть положительным числом."
        return True, "Круг возможен."
    def area(self) -> tuple[bool, str, float]:
        valid, message = self.is_valid()
        if not valid:
            return False, message, 0
        radius = float(self.radius)
        return True, "", math.pi * radius ** 2
    def GetParameters(self):
        self.radius = input("Введите радиус\n")        

# Класс для треугольника
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self) -> tuple[bool, str]:
        try:
            a = float(self.a)
            b = float(self.b)
            c = float(self.c)
        except ValueError:
            return False, "Все стороны треугольника должны быть числами."
        if a <= 0 or b <= 0 or c <= 0:
            return False, "Все стороны треугольника должны быть положительными числами."
        if not (a + b >= c and a + c >= b and b + c >= a):
            return False, "Треугольник с такими сторонами не может существовать."
        return True, "Треугольник возможен."
    def area(self) -> tuple[bool, str, float]:
        valid, message = self.is_valid()
        if not valid:
            return False, message, 0
        a = float(self.a)
        b = float(self.b)
        c = float(self.c)
        p = (a + b + c) / 2
        return True, "", math.sqrt(p * (p - a) * (p - b) * (p - c))
    def is_right_triangle(self) -> tuple[bool, str]:
        """Проверяет, является ли треугольник прямоугольным."""
        valid, message = self.is_valid()
        if not valid:
            return False, message
        a = float(self.a)
        b = float(self.b)
        c = float(self.c)
        sides = sorted([a, b, c])  # Сортируем стороны
        if math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2):
            return True, "Треугольник является прямоугольным."
        return False, "Треугольник не является прямоугольным."
    def GetParameters(self):
        self.side_a = input("Введите сторону А\n")
        self.side_b = input("Введите сторону В\n")
        self.side_c = input("Введите сторону С\n")
        
# Общая функция для обработки любой фигуры
def process_shape(shape: Shape):
    valid, message = shape.is_valid()
    if not valid:
        print(f"Ошибка: {message}")
        return
    _, _, area_value = shape.area()
    print(f"Площадь фигуры: {area_value:.2f}")

# Точка входа для изолированного запуска
if __name__ == "__main__":
    
    print("=== Пример использования ===\n")
     # Список классов фигур
    cShapeClasses = [Circle, Triangle]   
    """for shape_class in cShapeClasses:
        try:
            print(f"\n===      {shape_class.__name__}     ===\n")
            oShape = shape_class()  # Создаём экземпляр фигуры
            oShape.GetParameters()  # Запрашиваем параметры
            process_shape(oShape)

            # Дополнительная проверка для треугольника
            if isinstance(oShape, Triangle):
                print("\n=== Проверка прямоугольности ===")
                is_right, message = oShape.is_right_triangle()
                if is_right:
                    print(message)
                else:
                    print("Треугольник не является прямоугольным.")
        except Exception as oErr:
            print(f"Ошибка при работе с фигурой {shape_class.__name__}: {oErr}")
            
    """
    print("===         Круг         ===\n")
    try:
        oShape = Circle(input("Введите радиус\n"))
        process_shape(oShape)
    except Exception as oErr:
        print(f"Ошибка при работе с кругом: {oErr}")

    print("\n===      Треугольник     ===\n")
    try:
        oShape = Triangle(
            input("Введите сторону А\n")
            , input("Введите сторону В\n")
            , input("Введите сторону С\n")
        )
        process_shape(oShape)

        print("\n=== Треугольник, проверка прямоугольности ===")
        is_right, message = oShape.is_right_triangle()
        if is_right:
            print(message)
        else:
            print("Треугольник не является прямоугольным.")
    except Exception as oErr:
        print(f"Ошибка при работе с треугольником: {oErr}")
    
    # Ожидание завершения работы
    input("\nНажмите Enter для завершения работы...")