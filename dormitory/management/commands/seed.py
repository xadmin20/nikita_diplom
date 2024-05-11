from django.core.management.base import BaseCommand
from faker import Faker
import random

from dormitory.models import Dormitory, Student


class Command(BaseCommand):
    help = 'Populates the database with student records'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')  # Установка локали Faker на русский язык
        Faker.seed(0)  # Для воспроизводимости
        dormitories = list(Dormitory.objects.all())
        rooms = list(range(100, 126)) + list(range(200, 226)) + list(range(300, 326))

        if len(dormitories) != 3:
            print("Please ensure there are exactly three dormitories.")
            return

        students_created = 0
        while students_created < 100:
            dormitory = random.choice(dormitories)
            room = str(random.choice(rooms))
            # Проверяем, не превышено ли количество студентов в комнате
            if Student.objects.filter(dormitory=dormitory, room=room).count() < 2:
                full_name = fake.name()  # Генерация русского имени
                institute = "МГУ"
                group = f"{random.randint(1, 10):03d}"  # Трехзначный номер группы
                # Баллы уже инициализированы как 0 по умолчанию в модели
                Student.objects.create(
                    full_name=full_name,
                    dormitory=dormitory,
                    institute=institute,
                    group=group,
                    room=room
                )
                students_created += 1
                print(f"Created {full_name} in {dormitory.name}, room {room}")

        print(f"Successfully created {students_created} students.")
