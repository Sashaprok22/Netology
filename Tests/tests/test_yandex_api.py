import pytest
import yandex_api


@pytest.mark.parametrize(
    "folder_name, ref",
    (("test_folder", 201), ("test_folder", 409))
)
def test_create_folder(folder_name, ref):
    res = yandex_api.create_yandex_folder(folder_name)
    assert res.status_code == ref
