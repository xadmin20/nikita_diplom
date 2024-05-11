from django.db import models


class Dormitory(models.Model):
    """Модель общежития."""
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Общежитие'
        verbose_name_plural = 'Общежития'


class Student(models.Model):
    """Модель студента."""
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, verbose_name='Общежитие')
    institute = models.CharField(max_length=255, verbose_name='Институт', blank=True, null=True)
    group = models.CharField(max_length=255, verbose_name='Группа', blank=True, null=True)
    room = models.CharField(max_length=255, verbose_name='Комната', blank=True, null=True)
    admin_points = models.IntegerField(default=0, verbose_name='Административные баллы', blank=True, null=True)
    sso_points = models.IntegerField(default=0, verbose_name='ССО баллы', blank=True, null=True)

    def __str__(self):
        return self.full_name

    def total_points(self):
        return self.admin_points + self.sso_points

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Event(models.Model):
    """Модель события."""
    CHOISES = (
        ('admin', 'Административное'),
        ('sso', 'ССО'),
    )
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    points = models.IntegerField(default=0, verbose_name='Баллы')
    event_type = models.CharField(max_length=255, choices=CHOISES, verbose_name='Тип события')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class PointsHistory(models.Model):
    """Модель истории баллов."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент', related_name='pointshistory')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие')
    date = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return f'{self.student} - {self.event}'

    def save(self, *args, **kwargs):
        """Переопределяем метод сохранения записи в истории баллов."""
        # Если это новая запись в истории баллов
        if not self.pk:
            # Обновляем баллы студента в зависимости от типа события
            if self.event.event_type == 'admin':
                self.student.admin_points += self.event.points
            elif self.event.event_type == 'sso':
                self.student.sso_points += self.event.points
            self.student.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'История баллов'
        verbose_name_plural = 'История баллов'


class News(models.Model):
    """Модель новостей."""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, verbose_name='Общежитие')
    images = models.ImageField(upload_to='news/', verbose_name='Изображения', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
