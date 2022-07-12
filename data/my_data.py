import datetime

class MyData:
   # Репозитарии
   Rep1 = "/home/gm/PycharmProjects/SimbirSoft/"
   # полный путь и имя файла логирования выполнения автотестов
   log_file_name = 'Autotesting_log' + str(datetime.datetime.today()) + '.txt'

   put_url = 'https://cloud-api.yandex.net/v1/disk/resources'
   post_url = 'https://cloud-api.yandex.net/v1/disk/resources/copy'
   move_url = 'https://cloud-api.yandex.net/v1/disk/resources/move'

   token = 'AQAAAABiysq8AAgNqT66X5useU1jiFBXb3G7xmA'
   headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

   new_folder_path = 'SimbirSoft-API'
   path_copy_from = '/Файл для копирования'
   path_copy_in = '/SimbirSoft-API/Файл для копирования'
   path_move_rename = '/SimbirSoft-API/Файл переименован'
