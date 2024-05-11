from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

import random

from dormitory.models import Student, Event, PointsHistory

def random_date(start, end):
    """Генерирует случайную дату в пределах заданного диапазона."""
    fake = Faker()
    return fake.date_time_between(start_date=start, end_date=end)

class Command(BaseCommand):
    help = 'Populates events and assigns them to students'

    def random_date(self, start, end):
        """Генерирует случайную дату в пределах заданного диапазона."""
        time_between_dates = end - start
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_time = timedelta(hours=random.randrange(24), minutes=random.randrange(60))
        return start + timedelta(days=random_number_of_days) + random_time

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        Faker.seed(0)
        students = list(Student.objects.all())

        # Создание событий
        event_data = [
            ('Уборка территорий', 20, 'admin'),
            ('Помощь на мероприятиях', 10, 'admin'),
            ('Организация мероприятия', 30, 'sso'),
            ('Волонтерство', 40, 'sso'),
            ('Нарушение порядка', -20, 'admin'),
            ('Прогул занятий', -10, 'sso'),
            ('Поддержка младших студентов', 15, 'sso'),
            ('Участие в донорской программе', 25, 'admin'),
            ('Организация студенческого фестиваля', 35, 'sso'),
            ('Активное участие в спортивных соревнованиях', 30, 'sso'),
            ('Разработка научного проекта', 40, 'admin'),
            ('Неуважительное отношение к сотрудникам', -20, 'admin'),
            ('Использование запрещенных веществ', -40, 'admin'),
            ('Фальсификация учебных результатов', -30, 'sso'),
            ('Несоблюдение техники безопасности', -15, 'admin'),
            ('Участие в несанкционированных акциях', -25, 'sso')
        ]

        # Создаем или получаем события
        events = []
        for name, points, event_type in event_data:
            event, created = Event.objects.get_or_create(
                name=name,
                defaults={'description': fake.text(max_nb_chars=200), 'points': points, 'event_type': event_type}
            )
            events.append(event)

        # Распределение событий среди студентов и запись в историю баллов
        start_date = datetime.strptime('2023-09-01', '%Y-%m-%d')
        end_date = datetime.strptime('2024-05-16', '%Y-%m-%d')

        for student in students:
            number_of_events = random.randint(10, 20)
            selected_events = random.choices(events, k=number_of_events)
            for event in selected_events:
                event_date = self.random_date(start_date, end_date)
                PointsHistory.objects.create(
                    student=student,
                    event=event,
                    date=event_date
                )
                print(f'Assigned event "{event.name}" with date {event_date} to {student.full_name}')

        print("Successfully populated events and updated student points.")
