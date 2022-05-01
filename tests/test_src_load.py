import os
import pytest
from page_loader.page_loader import download

FIXTURES_FOLDER = 'fixtures'
MOCK_FOLDER = 'fixtures/mocks'
URL = 'https://ru.hexlet.io/courses'
URL_FILE_NAME = 'ru-hexlet-io-courses.html'
IMG_URL = 'https://ru.hexlet.io/assets/professions/nodejs.png'
IMG_FILE_NAME = 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png'
SCRIPT_URL = 'https://ru.hexlet.io/packs/js/runtime.js'
SCRIPT_FILE_NAME = 'ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js'



def read_file(path_file, mode='r'):
    with open(path_file, mode) as file:
        result = file.read()
    return result


def get_path(file_name, folder_name):
    return os.path.join(os.path.dirname(__file__), folder_name, file_name)


FILE_SITE = get_path('web_site.html', MOCK_FOLDER)
FILE_IMG = get_path('nodejs.png', MOCK_FOLDER)
FILE_SCRIPT = get_path('runtime.js', MOCK_FOLDER)
FILE_DOWNLOAD = get_path('downloaded_web_site.html', FIXTURES_FOLDER)


@pytest.mark.parametrize('received, expected', [(URL_FILE_NAME, FILE_DOWNLOAD)])
def test_src_replace(received, expected, tmpdir, requests_mock):
    text = read_file(FILE_SITE)
    img_content = read_file(FILE_IMG, 'rb')
    script_content = read_file(FILE_SCRIPT, 'rb')
    requests_mock.get(URL, text=text)
    requests_mock.get(IMG_URL, content=img_content)
    requests_mock.get(SCRIPT_URL, content=script_content)
    assert read_file(download(URL, tmpdir)) == read_file(FILE_DOWNLOAD)
