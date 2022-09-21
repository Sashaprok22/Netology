import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Authorization": "OAuth " + self.token,
            "Accept": "application/json",
        }

    def get_upload_link(self, file_path):
        response = requests.get(url="https://cloud-api.yandex.net/v1/disk/resources/upload", headers=self.get_headers(), params={
            "path": os.path.basename(file_path),
            "overwrite": True
        })
        return response.json().get("href")

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        requests.put(url=self.get_upload_link(file_path), data=open(file_path, "rb"))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь к вашему бесполезному файлу: ")
    token = "YA-TOKEN"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)