FROM python as builder

WORKDIR /app

# Создание виртуального окружения
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка системных зависимостей для psycopg2
RUN apt-get update && apt-get install -y libpq-dev

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Очистка кеша
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Копирование кода
COPY . .

# Копируем скрипт в контейнер
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh  # Даем права на выполнение

# Активация venv при входе в контейнер
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/venv/bin/activate" >> ~/.bashrc
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]