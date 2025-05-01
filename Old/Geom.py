import math

def calculate_circle_area(radius) -> tuple[bool, str, float]:
    """
    Вычисляет площадь круга по радиусу.
    :param radius: Радиус круга (должен быть положительным числом).
    :return: Площадь круга.
    :raises ValueError: Если радиус меньше или равен нулю.
    """
    try:
        # Проверка, что все значения можно преобразовать в числа
        radius = float(radius)
    except ValueError:
        return False, "Радиус должен быть числом.", 0
    if radius <= 0:
        return False, "Радиус должен быть положительным числом.", 0
    return True, "", math.pi * radius ** 2

def triangle_check(a, b, c) -> tuple[bool, str]:
    """
    Проверяет возможность существования треугольника.
    :param a: Длина первой стороны.
    :param b: Длина второй стороны.
    :param c: Длина третьей стороны.
    :return: Кортеж (bool, str), где bool указывает на возможность существования треугольника,
             а str содержит сообщение об ошибке или подтверждение.
    """
    lSides = sorted([a, b, c])    
    if lSides[0] <= 0:
        return False, "Все стороны треугольника должны быть положительными числами."
    if (lSides[0] + lSides[1] < lSides[2]):
        return False, "Треугольник с такими сторонами не может существовать."
    return True, "Треугольник возможен."      

def calculate_triangle_area(a, b, c) -> tuple[bool, str, float]:
    """
    Вычисляет площадь треугольника по трем сторонам.

    :param a: Длина первой стороны (должна быть положительной).
    :param b: Длина второй стороны (должна быть положительной).
    :param c: Длина третьей стороны (должна быть положительной).
    :return: Площадь треугольника.
    """
    # Проверка треугольника на реальность
    bStatus, sMessage = triangle_check(a, b, c) 
    if not bStatus:
        return False, sMessage, 0
    
    # Вычисление полупериметра
    fP = (a + b + c) / 2
    # Формула Герона 
    return True, "", math.sqrt(fP * (fP - a) * (fP - b) * (fP - c))
    
def is_right_triangle(a, b, c) -> tuple[bool, str]:
    """
    Проверяет, является ли треугольник прямоугольным.
    :param a: Длина первой стороны.
    :param b: Длина второй стороны.
    :param c: Длина третьей стороны.
    :return: True, если треугольник прямоугольный, иначе False.
    :raises ValueError: Если треугольник невозможен.
    """
    # Проверка треугольника на реальность
    bStatus, sMessage = triangle_check(a, b, c) 
    if not bStatus:
        return False, sMessage
    
    lSides = sorted([a, b, c])
    return math.isclose(lSides[0] ** 2 + lSides[1] ** 2, lSides[2] ** 2), ""
    
    
if __name__ == "__main__":
    try:
        # Пример расчета площади круга
        fRadius = input("Введите радиус круга: ")

        bStatus, sMessage, fCircleArea = calculate_circle_area(fRadius)
        if bStatus:
            print(f"Площадь круга с радиусом {fRadius}: {fCircleArea:.2f}")
        else:
            raise ValueError(sMessage)

        # Ввод сторон треугольника
        print("Введите стороны треугольника")
        fA = input("Введите сторону А: ")
        fB = input("Введите сторону B: ")
        fC = input("Введите сторону C: ")

        # Преобразование в числа
        try:
            fA, fB, fC = float(fA), float(fB), float(fC)
        except ValueError:
            raise ValueError("Все стороны треугольника должны быть числами.")

        # Пример расчета площади треугольника
        bStatus, sMessage, fTriangleArea = calculate_triangle_area(fA, fB, fC)
        if bStatus:
            print(f"Площадь треугольника со сторонами {fA}, {fB}, {fC}: {fTriangleArea:.2f}")
        else:
            raise ValueError(sMessage)

        # Проверка на прямоугольный треугольник
        is_right = is_right_triangle(fA, fB, fC)[0]
        print(f"Треугольник со сторонами {fA}, {fB}, {fC} - {['не прямоугольный', 'прямоугольный'][is_right]}")

    except ValueError as oEr:
        print(f"Ошибка: {oEr}")
    
    input("Для продолжения нажмите клавишу")