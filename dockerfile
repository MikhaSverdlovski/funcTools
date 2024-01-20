# Используйте официальный образ Python
FROM python:3.8

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости (requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в контейнер
COPY . .

# Копирование файлов в контейнер
COPY templates /app/templates
COPY static /app/static

# Запускаем приложение
CMD ["python", "app.py"]
