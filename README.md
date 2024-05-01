# Anverali
тестовое задание для Anverali

# Task_1
Программа получает данные контакта (ID, Имя) из Битрикс24 по Webhook проверять имя контакта на наличие его в БД (SQLite) 
Женские имена таблица names_womanМужские имена таблица names_man
Далее, если нашел имя в БД мужчин ставить пол Мужчина, если нашел имя в БД женщин ставить Женщина
Далее передаёт данные по гендеру обратно в контакт по ID

## Запуск Task_1

Создаем и активируем виртуальное окружение (Если ещё не создали):

```
python3 -m venv venv

source venv/bin/activate
```

Устанавливаем зависимости из requiremets.txt (Если ещё не установили):

```
pip install -r requiremetns.txt
```

Переходим в корневую папку проета task_1:

```
cd task_1
```

Создаём файл .env и заполняем его по примеру .env.example:
```
# Адрес вашего bitrix24
BITRIX_URL = https://yours_bitrix.bitrix24.ru/rest/1/
# Токены для webhook
GET_CONTACT_TOKEN = token_get
UPDATE_CONTACT_TOKEN = token_update
```

Заходим в файл constants.py изменяем константу CONTACT_ID на id записи контакта в Bitrix24:
```
CONTACT_ID = some_id
```

Стартуем:

```
python main.py
```


# Task_2
Cайт с админ панелью и 2-мя кабинетами на Django. Визуальное оформление присутствует. За основу взят сайт kwork.ru. На сайте есть админка, а так же два кабинета заказчика и исполнителя. В проекте используется бд SQLite, но я думаю, что тут не проблем подключить любую SQL бд.

## Запуск Task_2

1. Создаем и активируем виртуальное окружение (Если ещё не создали):

```
python3 -m venv venv

source venv/bin/activate
```

2. Устанавливаем зависимости из requiremets.txt (Если ещё не установили):

```
pip install -r requiremetns.txt
```

3. Переходим в корневую папку проета task_2 в ней лежит manage.py:

```
cd task_2
```

4. Стартуем:

```
python manage.py runserver
```

5. Тестовую БД для джанго я оставил с проектом: login: admin, pass: admin


### tests
Добавил пару тестов

Запускаем pytest из папки task_2:

```
pytest
```

```
flake8
```


# Технологии

* Python3
* Django
* SQLalchemy
* flake8
* pytest
