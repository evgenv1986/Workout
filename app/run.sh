#!/bin/bash

# Путь к директории проекта
PROJECT_DIR="/Users/evgeny/Documents/Projects/PetProjects/Workout/app"

# Переходим в директорию проекта
cd "$PROJECT_DIR" || { echo "Ошибка: не удалось перейти в директорию $PROJECT_DIR"; exit 1; }

# Активируем виртуальное окружение
source venv/bin/activate || { echo "Ошибка: не удалось активировать виртуальное окружение"; exit 1; }

# Переходим в директорию Django-проекта
# cd workout_django || { echo "Ошибка: не удалось перейти в директорию workout_django"; exit 1; }

# Запускаем сервер разработки
python ./workout_django/manage.py runserver 8000 || { echo "Ошибка: не удалось запустить сервер"; exit 1; }

echo "Запуск приложения $(date)" >> run.log

open "http://127.0.0.1:8000/"

# Деактивируем виртуальное окружение при завершении
deactivate