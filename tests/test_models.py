import unittest
from django.test import TestCase
from dormitory.models import News, Dormitory


class TestNewsModel(TestCase):
    """Тестируем модель новостей"""

    def setUp(self):
        """Создание объекта общежития для тестирования новости."""
        self.dormitory1 = Dormitory.objects.create(name='test dormitory1')

    def test_news_creation(self):
        """Тест создания объекта новости."""
        news = News.objects.create(title='test title', content='test content', dormitory=self.dormitory1)
        self.assertTrue(isinstance(news, News))
        self.assertEqual(news.__str__(), 'test title')

    def test_news_title_length(self):
        """Тест максимальной длины заголовка новости."""
        news = News.objects.create(title='t' * 255, content='test content', dormitory=self.dormitory1)
        self.assertTrue(len(news.title) <= 255)

    def test_news_content_readability(self):
        """Тест читабельности содержания новости."""
        news = News.objects.create(title='test title', content='test content', dormitory=self.dormitory1)
        self.assertEqual(news.content, 'test content')

    def test_news_dormitory(self):
        """Тест общежития новости."""
        news = News.objects.create(title='test title', content='test content', dormitory=self.dormitory1)
        self.assertEqual(news.dormitory.name, 'test dormitory1')


if __name__ == '__main__':
    unittest.main()
