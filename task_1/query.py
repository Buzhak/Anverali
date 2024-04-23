from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine, Name, Gender


def get_gender(some_name: str) -> str | None:
    '''
    Функция получает имя и возвращает обозначение пола ми БД
    Если имя не найдено, то возвращается None
    '''
    session = Session(engine)
    gender = session.execute(
        select(Gender.title).join(Name.gender).where(Name.title == some_name)
    ).first()
    if gender:
        gender = gender[0]
    else:
        gender = ''
    session.close()
    return gender
