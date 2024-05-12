# Инструкции по развертыванию сервера

## 1. Создание пользователя и добавление его в группу sudo

На сервере вы можете создать нового пользователя и добавить его в группу sudo для предоставления прав администратора. Выполните следующие команды:

```bash
# Создать нового пользователя
sudo adduser www

# Добавить пользователя в группу sudo
sudo usermod -aG sudo www
```

## 2. Установка Docker и Docker Compose

Для установки Docker и Docker Compose выполните следующие команды:

```bash
# Установка Docker
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce

# Установка Docker Compose
# Загрузка текущей стабильной версии Docker Compose:
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Применение исполняемых прав к бинарному файлу:
sudo chmod +x /usr/local/bin/docker-compose

# Проверка версии для убеждения в успешной установке:
docker-compose --version
```

## 3. Развертывание проекта на сервере

Теперь вы можете перенести свой проект на сервер, используя rsync, scp или любой другой способ, который вам удобен. Затем можно запустить Docker Compose на сервере, чтобы развернуть контейнеры:

```bash
# Перейдите в директорию проекта
cd path_to_your_project_directory

# Запустите Docker Compose
sudo docker-compose up -d
```

Это создаст и запустит все необходимые контейнеры в соответствии с вашим docker-compose.yml. Убедитесь, что все конфигурационные файлы и переменные окружения корректно установлены и доступны на сервере.



