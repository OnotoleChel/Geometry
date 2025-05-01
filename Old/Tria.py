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
            bStatus, sMessage = self.set_parameters(a, b, c)
    def is_valid(self) -> tuple[bool, str]:
        try:
            self.a, self.b, self.c = float(self.a), float(self.b), float(self.c)
            lSides = sorted([self.a, self.b, self.c])  # Сортируем стороны
        except ValueError:
            return False, "Все стороны треугольника должны быть числами."
        if lSides[  0] <= 0:
            return False, "Все стороны треугольника должны быть положительными числами."
        if lSides[0] + lSides[1] < lSides[2]:
            return False, "Треугольник с такими сторонами не может существовать."
        self._valid = True  # Устанавливаем _valid в True только при успешной проверке
        return True, "Треугольник возможен."
    def area(self) -> tuple[bool, str, float]:  
        """кортеж добавлен под расширение функционала"""
        """Вычисляет площадь треуга."""
        fA, fB, fC = self.a, self.b, self.c
        fP = (fA + fB + fC) / 2
        return True, "", math.sqrt(fP * (fP - fA) * (fP - fB) * (fP - fC))
    def is_right_triangle(self) -> tuple[bool, str]:
        """Проверяет, является ли треуг прямоугольным."""
        lSides = sorted([self.a, self.b, self.c])  # Сортируем стороны
        if math.isclose(lSides[0] ** 2 + lSides[1] ** 2, lSides[2] ** 2):
            return True, "Треугольник является прямоугольным.\n"
        return False, "Треугольник не является прямоугольным.\n"  
    def request_parameters(self) -> tuple[bool, str]:
        while True:
            self.a = input("Введите сторону А\n")
            self.b = input("Введите сторону В\n")
            self.c = input("Введите сторону С\n")
            valid, message = self.is_valid()
            if valid:
                break
            print(f"Ошибка: {message}. Попробуйте снова.")
        return True, "" #для единообразия с set_parameters   
    def set_parameters(self, a, b, c) -> tuple[bool, str]:
        """
        :param a, b, c: нужны числовые значения сторон треугольника.
        """
        self.a, self.b, self.c = a, b, c     
        bStatus, sMessage = self.is_valid()
        return bStatus, sMessage  