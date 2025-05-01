# термины
# треуг = треугольник

# main_module.py
import math
import logging
from abc import ABC, abstractmethod

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Базовый класс для всех фигур
class Shape(ABC):
    def __init__(self):
        """Инициализация приватного атрибута"""
        self._valid = False  
        self._message = "" 
        
    @property
    def valid(self) -> bool:
        return self._valid  # Реализация абстрактного свойства
        
    @property
    def message(self) -> str:
        return self._message  # Реализация абстрактного свойства    

    @abstractmethod
    def is_valid(self) -> tuple[bool, str]:
        pass  # Проверяет корректность фигуры

    @abstractmethod
    def area(self) -> float | None:
        pass  # Вычисляет площадь фигуры

    @abstractmethod
    def request_parameters(self):
        pass  # Запрашивает у пользователя параметры фигуры

    @abstractmethod
    def set_parameters(self):
        pass  # Программно устанавливает параметры фигуры        

class Circle(Shape):
    def __init__(self, interactive=True, radius=None):
        """
        :param interactive: Если True, запрашивает параметры у пользователя.
                            Если False, использует программно переданный радиус.
        :param radius: Радиус круга (используется только при interactive=False).
        """
        if interactive:
            self.request_parameters()
        else:
            self.set_parameters(radius)

    def is_valid(self) -> tuple[bool, str]:
        """Проверяет корректность круга."""
        self._valid = False
        self._message = ""
        # проверка того что радиус - не ноне
        if self.radius is None:
            self._message = "Радиус не может быть None."
            return False, self._message
        # проверка того что радиус - число  
        try:
            self.radius = float(self.radius)
        except ValueError:
            self._message = "Радиус должен быть числом."
            return False, self._message
        # проверка положительности радиуса    
        if self.radius < 0:
            self._message = "Радиус должен быть положительным числом."
            return False, self._message    
        # Устанавливаем _valid в True только при успешной проверке    
        self._valid = True  
        return True, ""
            
       
    def area(self) -> float | None:  # Используем Union-тип (float или None)
        """Вычисляет площадь круга. Работает только если радиус проверен"""
        if self._valid:
            return math.pi * self.radius ** 2
        return None
    
    def request_parameters(self):
        while True:
            self.radius = input("Введите радиус - положительное число\n")
            bStatus, sMessage = self.is_valid()
            if bStatus:
                break
            print(f"Ошибка: {sMessage}. Попробуйте снова.")      
        
    def set_parameters(self, radius):
        self.radius = radius
        self.is_valid()
        
# Класс для треугольника
class Triangle(Shape):
    def __init__(self, interactive=True, a=None, b=None, c=None):
        """
        :param interactive: Если True, запрашивает параметры у пользователя.
        Если False, использует программно переданные стороны.
        :param a, b, c: Стороны треугольника (используются только при interactive=False).
        """
        if interactive:
            self.request_parameters()
        else:
            self.set_parameters(a, b, c)
                  
    def is_valid(self) -> tuple[bool, str]:
        """Проверяет корректность треуга"""
        self._valid = False
        self._message = ""
        # проверка того что параметры - не ноне       
        if None in (self.a, self.b, self.c):
            self._message = "Длинна сторон не может быть None."
            return False, self._message        
        # проверка того что длинны сторон - числа  
        try:
            self.a, self.b, self.c = float(self.a), float(self.b), float(self.c)
            lSides = sorted([self.a, self.b, self.c])  # Сортируем стороны
        except ValueError:
            self._message = "Все стороны треугольника должны быть числами."
            return False, self._message
        # проверка положительности сторон - достаточно проверить меньшую из сторон
        if lSides[0] < 0:
            self._message = "Все стороны треугольника должны быть положительными числами."
            return False, self._message
        if lSides[0] + lSides[1] < lSides[2]:
            self._message = "Треугольник с такими сторонами не может существовать."
            return False, self._message
        self._valid = True  # Устанавливаем _valid в True только при успешной проверке
        return True, ""
    
    def area(self) -> float | None:  # Используем Union-тип (float или None)  
        """кортеж добавлен под расширение функционала"""
        """Вычисляет площадь треуга."""
        if self._valid:
            fA, fB, fC = self.a, self.b, self.c
            fP = (fA + fB + fC) * 0.5
            return math.sqrt(fP * (fP - fA) * (fP - fB) * (fP - fC))
        return None

    def request_parameters(self):
        print("Введите стороны - положительные числа")
        while True:
            self.a = input("А\n")
            self.b = input("В\n")
            self.c = input("С\n")
            bStatus, sMessage = self.is_valid()
            if bStatus:
                break
            print(f"Ошибка: {sMessage}. Попробуйте снова.")  

    def set_parameters(self, a, b, c):
        """
        :param a, b, c: нужны числовые значения сторон треугольника.
        """
        self.a, self.b, self.c = a, b, c  
        self.is_valid()       

def is_right_triangle(triangle: Triangle) -> tuple[bool, str]:
    """
    Проверяет, является ли треугольник прямоугольным.
    :param triangle: Экземпляр класса Triangle.
    :return: Кортеж (bool, str) — результат проверки и сообщение.
    вынесен из класса для соблюдения Лисковой 
    не добавлен в родителя для соблюдения Оккама
    """
    if not isinstance(triangle, Triangle):
        return False, "Метод is_right_triangle применим только к объектам класса Triangle."
    lSides = sorted([triangle.a, triangle.b, triangle.c])  # Сортируем стороны
    if math.isclose(lSides[0] ** 2 + lSides[1] ** 2, lSides[2] ** 2):
        return True, "Треугольник является прямоугольным."
    return False, "Треугольник не является прямоугольным."               

# Общая функция для обработки любой фигуры
def process_shape(processed_shape: Shape):
    fAreaValue = processed_shape.area()
    if fAreaValue is not None:
        print(f"Площадь фигуры: {fAreaValue:.2f}")
        logging.info(f"Площадь фигуры: {fAreaValue:.2f}")
    else:
        print(f"Ошибка при вычислении площади: {processed_shape.message}")
        logging.error(f"Ошибка при вычислении площади: {processed_shape.message}")

# Точка входа для изолированного запуска
if __name__ == "__main__":
    print("=== Пример использования ===")  
    """oShape = Circle(False,"a")
    process_shape(oShape)"""
    for oShapeClass in [Circle, Triangle]:  #Shape Classes
        try:
            print(f"===      {oShapeClass.__name__}     ===")
            oShape = oShapeClass()  # Создаём экземпляр фигуры
            process_shape(oShape)
            # Дополнительная проверка для треугольника (на остальных фигурах не сработает)
            if isinstance(oShape, Triangle):
                print("=== Проверка прямоугольности ===")
                print(is_right_triangle(oShape)[1])
        except Exception as oErr:
            print(f"Ошибка при работе с фигурой {oShapeClass.__name__}: {oErr}")
    # Ожидание завершения работы
    input("\nНажмите Enter для завершения работы...")