import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        name = os.path.basename(file_path)
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token}
        params = {"path": name, "overwrite": "true"}
        response = requests.get(url, params=params, headers=headers)
        href = response.json()['href']
        new_response = requests.put(href, data=open(name, 'rb'))
        new_response.raise_for_status()
        if new_response.status_code == 201:
            print(f'Файл {name} отправлен')

if __name__ == '__main__':
    path_to_file = r'D:\Python\Requests_test\test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)