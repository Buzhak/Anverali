import os
import logging
from dotenv import load_dotenv

from bitrix24 import Bitrix24
from bitrix24.exceptions import BitrixError

from constants import GENDER
from query import get_gender


# Получаю данные контакта из Bitrix24 по ID
def get_contact_by_id(contact_id: int | str) -> dict | None:

    bx24 = Bitrix24(
        f'{os.getenv("BITRIX_URL")}{os.getenv("GET_CONTACT_TOKEN")}'
    )

    try:
        resporce = bx24.callMethod(
            'crm.contact.get',
            {
                'ID': contact_id
            }
        )
        logging.info(
            'Данные пользователя получены'
            f'{resporce.get("ID")} - '
            f'{resporce.get("NAME")} - '
            f'{resporce.get(UPATE_PARAM)}'
        )
    except BitrixError as e:
        logging.error(e.message)
        resporce = None
    return resporce


# Обновление данных контакта из Bitrix24 по ID
def update_contaxt_by_id(contact_id: int, data: dict):

    bx24 = Bitrix24(
        f'{os.getenv("BITRIX_URL")}{os.getenv("UPDATE_CONTACT_TOKEN")}'
    )

    try:
        resporce = bx24.callMethod(
            'crm.contact.update',
            {
                "id": contact_id,
                'fields': data,
                'params': {'REGISTER_SONET_EVENT': 'N'}
            }
        )
        logging.info(f'Данные пользователя с ID: {contact_id} обновлены')
    except BitrixError as e:
        logging.error(e.message)
        resporce = None

    return resporce


def main():
    # Берем данные о контакте из Bitrix24
    contact = get_contact_by_id(CONTACT_ID)
    # Если двнные есть
    if contact:
        # Получаем данные о гендере из БД
        gender = get_gender(contact.get('NAME'))
        # Формируем данные для обновления записи контакта
        update_data = {UPATE_PARAM: GENDER[gender]}
        # Обновляем данные о контакте из Bitrix24
        update_contaxt_by_id(contact.get('ID'), update_data)
        # Вызываем контакт снова, чтобы проверить данные
        contact = get_contact_by_id(CONTACT_ID)


if __name__ == '__main__':
    # ID контакта заранее созданного в Bitrix24
    CONTACT_ID = 11
    # Параметр обращения к контакту определяющий пол человека.
    UPATE_PARAM = 'HONORIFIC'
    # Параметры логирования
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    main()
