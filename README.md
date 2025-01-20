# Cервис для получения тарифов

## Описание

Этот проект представляет собой веб-приложение на базе **FastAPI**, которое
позволяет получить список тарифов из внешнего API. Приложение принимает
параметры запроса, такие как валюта и тип CRM, отправляет запрос к стороннему
API, а затем возвращает JSON с информацией о тарифах.

## Установка и запуск

### 1. Клонирование репозитория

Склонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/artemmikh/tariffs-api.git
cd tariffs-api
```

### 2. Установка зависимостей

Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. Запуск приложения

Запустите сервер разработки:

```bash
uvicorn app:app --reload
```

Интерфейс для запросов будет доступен по
адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Использование

Чтобы получить список тарифов, отправьте GET-запрос на эндпоинт:

```
GET /tariffs
```

### Параметры запроса

`currency` (строка): Валюта тарифов. Значение по умолчанию — RUB.

`crm` (строка): Тип CRM. Значение по умолчанию — lk.

### Пример запроса:

```
http://127.0.0.1:8000/tariffs?currency=RUB&crm=lk
```

### Пример ответа

```json
{
  "194": "1 месяц 1390.00/30 дней - Всего: 1 390.00₽",
  "195": "3 месяца 1390.00/месяц - Всего: 4 170.00₽",
  "196": "6 месяцев 1251.00/месяц - Всего: 7 506.00₽ - Скидка 10%",
  "197": "1 год 1042.50/месяц - Всего: 12 510.00₽ - Скидка 25%",
  "198": "1 месяц 2390.00/30 дней - Всего: 2 390.00₽",
  "199": "3 месяца 2390.00/месяц - Всего: 7 170.00₽",
  "200": "6 месяцев 2151.00/месяц - Всего: 12 906.00₽ - Скидка 10%",
  "201": "1 год 1792.50/месяц - Всего: 21 510.00₽ - Скидка 25%",
  "360": "1 месяц 4390.00/30 дней - Всего: 4 390.00₽",
  "361": "3 месяца 4390.00/месяц - Всего: 13 170.00₽",
  "362": "6 месяцев 3951.00/месяц - Всего: 23 706.00₽ - Cкидка 10%",
  "363": "12 месяцев 3292.50/месяц - Всего: 39 510.00₽ - Скидка 25%"
}
```