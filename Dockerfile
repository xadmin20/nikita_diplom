# Используйте официальный образ Python как родительский
FROM python:3.10-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте содержимое локальной директории в контейнер
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput --verbosity 2
# Выводим содержимое каталога статических файлов в файл для последующей проверки
RUN ls -la /app/staticfiles > /app/staticfiles_list.txt
# Применяет миграции и создает суперпользователя (не рекомендуется для продакшена)
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '0') | python manage.py shell && gunicorn --bind 0.0.0.0:8000 Nikita.wsgi:application"]
