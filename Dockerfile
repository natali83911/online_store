FROM python:3.12-slim

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы зависимостей (уберите poetry.lock, если его нет!)
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости (без dev и без создания venv внутри контейнера)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем проект
COPY . .

EXPOSE 8000

# Запуск через gunicorn (или укажите нужную команду)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
