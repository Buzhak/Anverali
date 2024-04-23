import logging
from pathlib import Path
from sqlalchemy.orm import Session

from db import engine, Gender, Name
from constants import (
    FEMALE,
    MALE,
    FEMALE_NAME_FILE_PATH,
    MALE_NAME_FILE_PATH,
)


def add_data_from_file(
    file_path: Path, gender: Gender, session: Session
) -> None:
    try:
        objects = []
        # читаем файлик
        file = open(file_path, "r", encoding='utf8')
        while True:
            # считываем строку
            line = file.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            objects.append(
                Name(title=line.replace('\n', ''), gender_id=gender.id)
            )
        # добавляем данные в сессию
        session.bulk_save_objects(objects)
        # сохраняем данные в бд
        session.commit()

        logging.info(f'имена из файла {file.name}')
        # закрываем файл
        file.close
    except FileNotFoundError:
        logging.error(FileNotFoundError)


def main():
    with Session(engine) as session:
        # добавляем гендер в таблицу Gender
        male = Gender(title=MALE)
        female = Gender(title=FEMALE)
        session.add_all([male, female])
        session.commit()
        logging.info(f'Добавлены гендеры: {male.title}, {female.title}')
        # добавляем имена в таблицу Name
        add_data_from_file(MALE_NAME_FILE_PATH, male, session)
        add_data_from_file(FEMALE_NAME_FILE_PATH, female, session)
        session.close()
    logging.info('Данные загружены')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
