import unittest
import math
import logging
from GeomOOPm2ClassLoop import Circle, Triangle, process_shape, is_right_triangle

# Настройка логирования
logging.basicConfig(level=logging.INFO)

class TestShape(unittest.TestCase):
    def tearDown(self):
        """Вызывается после каждого теста."""
        if self._outcome.success:  # Проверяем, прошел ли тест успешно
            print("Пройдено")
        else:
            print("Не пройдено")

    def test_circle_valid_radius(self):
        """Тест на валидный радиус круга."""
        print("Тест на валидный радиус круга.")
        circle = Circle(interactive=False, radius=5)
        self.assertTrue(circle.valid)
        self.assertEqual(circle.area(), math.pi * 5 ** 2)

    def test_circle_negative_radius(self):
        """Тест на отрицательный радиус круга (-5)."""
        print("Тест на отрицательный радиус круга (-5).")
        circle = Circle(interactive=False, radius=-5)
        self.assertFalse(circle.valid)
        self.assertIsNone(circle.area())
        self.assertIn("Радиус должен быть положительным числом", circle.message)

    def test_circle_negative_radius_another(self):
        """Тест на другой отрицательный радиус круга (-10)."""
        print("Тест на другой отрицательный радиус круга (-10).")
        circle = Circle(interactive=False, radius=-10)
        self.assertFalse(circle.valid)
        self.assertIsNone(circle.area())
        self.assertIn("Радиус должен быть положительным числом", circle.message)

    def test_circle_invalid_radius(self):
        """Тест на невалидный радиус круга (например, строка)."""
        print("Тест на невалидный радиус круга (например, строка).")
        circle = Circle(interactive=False, radius="a")
        self.assertFalse(circle.valid)
        self.assertIsNone(circle.area())
        self.assertIn("Радиус должен быть числом", circle.message)

    def test_triangle_valid_sides(self):
        """Тест на валидные стороны треугольника."""
        print("Тест на валидные стороны треугольника.")
        triangle = Triangle(interactive=False, a=3, b=4, c=5)
        self.assertTrue(triangle.valid)
        self.assertEqual(triangle.area(), 6.0)  # Площадь треугольника 3-4-5

    def test_triangle_one_negative_side(self):
        """Тест на треугольник с одной отрицательной стороной."""
        print("Тест на треугольник с одной отрицательной стороной.")
        triangle = Triangle(interactive=False, a=-1, b=4, c=5)
        self.assertFalse(triangle.valid)
        self.assertIsNone(triangle.area())
        self.assertIn("Все стороны треугольника должны быть положительными числами", triangle.message)

    def test_triangle_two_negative_sides(self):
        """Тест на треугольник с двумя отрицательными сторонами."""
        print("Тест на треугольник с двумя отрицательными сторонами.")
        triangle = Triangle(interactive=False, a=-1, b=-2, c=5)
        self.assertFalse(triangle.valid)
        self.assertIsNone(triangle.area())
        self.assertIn("Все стороны треугольника должны быть положительными числами", triangle.message)

    def test_triangle_all_negative_sides(self):
        """Тест на треугольник со всеми отрицательными сторонами."""
        print("Тест на треугольник со всеми отрицательными сторонами.")
        triangle = Triangle(interactive=False, a=-1, b=-2, c=-3)
        self.assertFalse(triangle.valid)
        self.assertIsNone(triangle.area())
        self.assertIn("Все стороны треугольника должны быть положительными числами", triangle.message)

    def test_triangle_impossible(self):
        """Тест на невозможный треугольник."""
        print("Тест на невозможный треугольник (сумма двух сторон меньше третьей).")
        triangle = Triangle(interactive=False, a=1, b=2, c=10)
        self.assertFalse(triangle.valid)
        self.assertIsNone(triangle.area())
        self.assertIn("Треугольник с такими сторонами не может существовать", triangle.message)

    def test_is_right_triangle(self):
        """Тест на проверку прямоугольности треугольника."""
        print("Тест на проверку прямоугольности треугольника.")
        triangle = Triangle(interactive=False, a=3, b=4, c=5)
        self.assertTrue(is_right_triangle(triangle)[0])
        self.assertIn("Треугольник является прямоугольным", is_right_triangle(triangle)[1])

        triangle = Triangle(interactive=False, a=2, b=3, c=4)
        self.assertFalse(is_right_triangle(triangle)[0])
        self.assertIn("Треугольник не является прямоугольным", is_right_triangle(triangle)[1])

    def test_process_shape(self):
        """Тест на обработку фигур через process_shape."""
        print("Тест на обработку фигур через process_shape.")
        # Круг с валидным радиусом
        circle = Circle(interactive=False, radius=5)
        with self.assertLogs(level="INFO") as log:
            process_shape(circle)
        self.assertIn("Площадь фигуры: 78.54", log.output[0])

        # Круг с невалидным радиусом
        circle = Circle(interactive=False, radius="a")
        with self.assertLogs(level="ERROR") as log:
            process_shape(circle)
        self.assertIn("Ошибка при вычислении площади", log.output[0])

if __name__ == "__main__":
    unittest.main()