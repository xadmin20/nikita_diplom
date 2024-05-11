import unittest
from django.test import TestCase

from dormitory.models import Dormitory


class TestDormitory(TestCase):
    """Тестируем модель общежития."""

    def setUp(self):
        """Создание объектов общежития для тестирования."""
        self.dormitory1 = Dormitory.objects.create(name='Dorm1', address='Address1', phone='1234567890')
        self.dormitory2 = Dormitory.objects.create(name='Dorm2', address='Address2', phone='0987654321')

    def tearDown(self):
        """Удаление объектов после тестирования."""
        try:
            self.dormitory1.delete()
            self.dormitory2.delete()
        except Exception:
            pass

    def test_dormitory_creation(self):
        """Тест создания объекта общежития."""
        self.assertIsInstance(self.dormitory1, Dormitory)
        self.assertIsInstance(self.dormitory2, Dormitory)

    def test_dormitory_str(self):
        """Тест отображения объекта общежития."""
        self.assertEqual(str(self.dormitory1), 'Dorm1')
        self.assertEqual(str(self.dormitory2), 'Dorm2')

    def test_dormitory_unique_name(self):
        """Тест уникальности названия общежития."""
        with self.assertRaises(Exception):  # Expect an exception since name should be unique
            Dormitory.objects.create(name='Dorm1', address='Address3', phone='1122334455')

    def test_dormitory_phone(self):
        """Тест телефона общежития."""
        self.assertEqual(self.dormitory1.phone, '1234567890')
        self.assertEqual(self.dormitory2.phone, '0987654321')

    def test_dormitory_addr(self):
        """Тест адреса общежития."""
        self.assertEqual(self.dormitory1.address, 'Address1')
        self.assertEqual(self.dormitory2.address, 'Address2')


if __name__ == '__main__':
    unittest.main()
