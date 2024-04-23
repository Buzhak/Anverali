from pathlib import Path
from ..constants import MALE_NAME_FILE_PATH, FEMALE_NAME_FILE_PATH


def open_file(file_path: Path) -> None:
    try:
        with open(file_path, 'r') as _:
            assert True
    except FileNotFoundError:
        assert False, f'File {file_path} not found'
    except Exception as e:
        assert False, f'Failed to open file: {e}'


def test_files_in_directory() -> None:
    '''
    Проверяем файлы с данными
    '''
    file_path = MALE_NAME_FILE_PATH
    open_file(file_path)
    file_path = FEMALE_NAME_FILE_PATH
    open_file(file_path)
