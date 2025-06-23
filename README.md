# Грузовозофф - Портал для заказа грузоперевозок

Информационная система для заказа грузоперевозок автомобильным транспортом.

## Функциональность

- Регистрация и авторизация пользователей
- Подача заявок на перевозку грузов
- Просмотр истории заявок пользователя

## Технический стек

- **Frontend**: HTML, CSS, Bootstrap 5
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Authentication**: Flask-Login

## Установка и запуск

### Предварительные требования

- Python 3.8 или выше
- PostgreSQL 12 или выше

### Шаги установки

1. Клонировать репозиторий:

```bash
git clone <url_репозитория>
cd gruzovozoff
```

2. Создать виртуальное окружение и активировать его:

```bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для Linux/Mac:
source venv/bin/activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Создать базу данных в PostgreSQL:

```sql
CREATE DATABASE gruzovozoff;
```

5. Скопировать файл `.env-example` в `.env` и настроить переменные окружения:

```bash
cp .env-example .env
# Отредактировать файл .env, указав правильные значения для SECRET_KEY и DATABASE_URL
```

6. Запустить приложение:

```bash
python app.py
```

## Доступ к системе

После запуска приложение будет доступно по адресу http://localhost:5000.

## Структура проекта

```
gruzovozoff/
├── app/
│   ├── models/              # Модели данных
│   ├── routes/              # Маршруты и контроллеры
│   ├── forms/               # Формы и их валидация
│   ├── templates/           # HTML-шаблоны
│   ├── static/              # Статические файлы (CSS, JS)
│   └── __init__.py          # Инициализация приложения
├── app.py                   # Точка входа приложения
├── requirements.txt         # Зависимости
└── .env-example             # Пример файла конфигурации
```

## Автор

- [Ваше имя](mailto:your.email@example.com) 