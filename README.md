# Anverali
тестовое задание для Anverali

## Task_1 - Работа с контактами в Битрикс24
Программа получает данные контакта (ID, Имя) из Битрикс24 по Webhook проверять имя контакта на наличие его в БД (SQLite) 
Женские имена таблица names_womanМужские имена таблица names_man
Далее, если нашел имя в БД мужчин ставить пол Мужчина, если нашел имя в БД женщин ставить Женщина
Далее передаёт данные по гендеру обратно в контакт по ID

### Запуск Task_1

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


## Task_2 - Сайт на Django
Cайт с админ панелью и 2-мя кабинетами на Django.
За основу взята пародия на концепцию сайта kwork.ru.
Обращаю внимание, что это скетч, а не полноценый сайт, нужно дописать тестов и сделать рефакторинг кода. 
Визуальное оформление присутствует, но весьма условно, я, пока что, не по этой части...
На сайте есть админка более или менее "причесанная", а так же, два кабинета заказчика и исполнителя, между ними можно переключаться.
В проекте используется бд SQLite для баловства и тестирования, но есть и настройки для подключения Postgres из docker, про это [ниже можно почитать](#postgres).

### Запуск Task_2

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

<a id="postgres"></a>
## База Postgres

Если сильно хочется, то можно развенуть локальный контейнер с postgres

1. Переходим в каталог task_2/infra

2. Пишем команду в терминал (с учетом, что у вас уже установален docker-compose):

```
docker-compose up -d --build
```

3. Идём в task_2/app/settings.py комментируем настройка для работы с sqlite и раскомментируем настройка postgres

4. Далее из каталога task_2 накатываем миграции

```
python manage.py migrate
```

5. Создаём суперюзера

```
python manage.py createsuperuser
```

6. Стартуем:

```
python manage.py runserver
```


#### tests
Добавил пару тестов

Запускаем pytest из папки task_2:

```
pytest
```

```
flake8
```


## Технологии

* Python3
* Django
* SQLalchemy
* flake8
* pytest
* Docker-compose
* Postgres

![darktide-adeptus-mechanicus](https://github.com/Buzhak/Anverali/assets/47240390/3d8f3c46-9ae4-4ebf-a16a-3a209be5ae51)

