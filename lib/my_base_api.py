import requests
from data.my_data import MyData as D
from loguru import logger

class MyBase:

    def logging_file(log_file):
        logger.remove()
        logger.add(log_file, level='INFO', format="<lvl>[</lvl><c>{time:DD.MM.YYYY HH:mm:ss.SSS}</c><lvl>]</lvl> <lvl>{message}</lvl>", catch='True')

    def create_folder(path):
        try:
            result = requests.put(f'{D.put_url}?path={path}', headers=D.headers)
            return result
        except KeyError:
            return result

    def copy_file(path1, path2):
        try:
            result = requests.post(f'{D.post_url}?from={path1}&path={path2}', headers=D.headers)
            return result
        except KeyError:
            return result

    def move_file(path1, path2):
        try:
            result = requests.post(f'{D.post_url}?from={path1}&path={path2}', headers=D.headers)
            return result
        except KeyError:
            return result

    def del_file(path):
        try:
            result = requests.delete(f'{D.put_url}?path={path}', headers=D.headers)
            return result
        except KeyError:
            return result

