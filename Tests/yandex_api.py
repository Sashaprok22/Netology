import requests

default_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "YANDEX TOKEN"
}


def create_yandex_folder(folder_name):
    params = {
        "path": folder_name
    }
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=default_headers)
    return response
