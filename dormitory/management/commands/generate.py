from django.core.management.base import BaseCommand
from django.utils import timezone

from dormitory.models import Student, Event, PointsHistory
from faker import Faker
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populates events and assigns them to students'

    def random_date(self, start, end):
        """Генерирует случайную дату в пределах заданного диапазона с учетом часового пояса."""
        fake = Faker()
        # Генерация наивной даты
        naive_date = fake.date_time_between(start_date=start, end_date=end)
        # Преобразование наивной даты в осведомленную дату
        aware_date = timezone.make_aware(naive_date, timezone.get_current_timezone())
        return aware_date

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        Faker.seed(0)
        students = list(Student.objects.all())
        events = list(Event.objects.all())

        start_date = datetime.strptime('2023-09-01', '%Y-%m-%d')
        end_date = datetime.strptime('2024-05-16', '%Y-%m-%d')

        for student in students:
            number_of_events = random.randint(1, 20)
            for _ in range(number_of_events):
                event = random.choice(events)
                event_date = self.random_date(start_date, end_date)
                PointsHistory.objects.create(
                    student=student,
                    event=event,
                    date=event_date
                )
                print(f'Assigned event "{event.name}" with date {event_date} to {student.full_name}')

        print("Successfully populated events and updated student points.")