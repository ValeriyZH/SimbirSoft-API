from datetime import datetime
from data.my_data import MyData as D
from lib.my_base_api import MyBase as Base
from loguru import logger
import datetime
import os
import sys

sys.path.append(os.path.abspath('/home/gm/PycharmProjects/SimbirSoft-API-YD/'))

def __init__(self, browser):
    self.browser = browser


@logger.catch
def test_simbirsoft_api():
    global new_page
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ ПО API ДЛЯ КОМПАНИИ "SIMBIRSOFT"')

    logger.info('# создаем новую папку')
    result = Base.create_folder(D.new_folder_path)
    logger.info(result)
    logger.info(result.json())

    logger.info('# копируем исходный файл в новую папку')
    result = Base.copy_file(D.path_copy_from, D.path_copy_in)
    logger.info(result)
    logger.info(result.json())

    logger.info('# переименовываем файл')
    result = Base.move_file(D.path_copy_in, D.path_move_rename)
    logger.info(result)
    logger.info(result.json())

    logger.info('# удаляем файл со старым названием')
    result = Base.del_file(D.path_copy_in)
    logger.info(result)
   
    logger.info('# ЗАВЕРШИЛИ ТЕСТОВОЕ ЗАДАНИЕ ПО API ДЛЯ КОМПАНИИ "SIMBIRSOFT"')