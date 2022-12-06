import requests

default_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "y0_AgAAAAAkqDJkAADLWwAAAADPa0r8h6YiCq4wQ6-6L8g8l7htA--0tsg"
}


def create_yandex_folder(folder_name):
    params = {
        "path": folder_name
    }
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", params=params, headers=default_headers)
    return response
