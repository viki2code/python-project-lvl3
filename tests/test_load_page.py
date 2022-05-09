import os

import pytest

from page_loader.page_loader import download
from page_loader.url import get_file_name

STATUS_CODE = [404, 500]
FIXTURES_FOLDER = 'fixtures'
MOCK_FOLDER = 'fixtures/mocks'
URL = 'https://ru.hexlet.io/courses'
URL_FILE_NAME = 'ru-hexlet-io-courses.html'
IMG_URL = 'https://ru.hexlet.io/assets/professions/nodejs.png'
IMG_FILE_NAME = 'ru-hexlet-io-assets-professions-nodejs.png'
SCRIPT_URL = 'https://ru.hexlet.io/packs/js/runtime.js'
SCRIPT_FILE_NAME = 'ru-hexlet-io-packs-js-runtime.js'
LINK_URL = 'https://ru.hexlet.io/assets/application.css'
LINK_FILE_NAME = 'ru-hexlet-io-assets-application.css'


def read_file(path_file, mode='r'):
    with open(path_file, mode) as file:
        result = file.read()
    return result


def get_path(file_name, folder_name):
    return os.path.join(os.path.dirname(__file__), folder_name, file_name)


FILE_SITE = get_path('web_site.html', MOCK_FOLDER)
FILE_IMG = get_path('nodejs.png', MOCK_FOLDER)
FILE_SCRIPT = get_path('runtime.js', MOCK_FOLDER)
FILE_LINK = get_path('application.css', MOCK_FOLDER)
FILE_DOWNLOAD = get_path('downloaded_web_site.html', FIXTURES_FOLDER)


@pytest.mark.parametrize('url, file_name', [(URL, URL_FILE_NAME),
                                            (IMG_URL, IMG_FILE_NAME),
                                            (SCRIPT_URL, SCRIPT_FILE_NAME),
                                            (LINK_URL, LINK_FILE_NAME)])
def test_file_name(url, file_name):
    assert get_file_name(url) == file_name


def test_path_file(requests_mock, tmpdir):
    requests_mock.get(URL, text='data')
    assert download(URL, tmpdir) == os.path.join(tmpdir, URL_FILE_NAME)


def test_src_replace(tmpdir, requests_mock):
    content = read_file(FILE_SITE, 'rb')
    # headers_html = {'content-length': str(len(content))}
    img_content = read_file(FILE_IMG, 'rb')
    # headers_img = {'content-length': str(len(img_content))}
    script_content = read_file(FILE_SCRIPT, 'rb')
    # headers_script = {'content-length': str(len(script_content))}
    link_content = read_file(FILE_LINK, 'rb')
    # headers_link = {'content-length': str(len(link_content))}
    # requests_mock.get(URL, content=content, headers=headers_html)
    requests_mock.get(URL, content=content)
    requests_mock.get(IMG_URL, content=img_content)
    requests_mock.get(SCRIPT_URL, content=script_content)
    requests_mock.get(LINK_URL, content=link_content)
    assert read_file(download(URL, tmpdir)) == read_file(FILE_DOWNLOAD)


@pytest.mark.parametrize('code', STATUS_CODE)
def test_response_error_code(requests_mock, code, tmp_path):
    requests_mock.get(URL, status_code=code)
    with pytest.raises(Exception):
        assert download(URL, tmp_path)


def test_write_content(requests_mock):
    requests_mock.get(URL, text='data')
    with pytest.raises(Exception):
        assert download(URL, 'tmp_path')


def test_exception_load(requests_mock, tmpdir):
    requests_mock.get(IMG_URL, text='data')
    with pytest.raises(Exception):
        assert download(IMG_URL, tmpdir) == 1
