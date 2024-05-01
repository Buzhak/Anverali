from pathlib import Path

FEMALE_NAME_FILE_PATH = Path('data', 'female_names.txt')
MALE_NAME_FILE_PATH = Path('data', 'male_names.txt')
MALE = 'M'
FEMALE = 'F'
NO_CONTACT_DATA = 'Данные контакта отсутствуют'
GENDER = {MALE: 'HNR_RU_1', FEMALE: 'HNR_RU_2', '': ''}


# ID контакта заранее созданного в Bitrix24
CONTACT_ID = 11
# Параметр обращения к контакту определяющий пол человека.
UPATE_PARAM = 'HONORIFIC'
