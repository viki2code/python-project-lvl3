import pytest

from page_loader.url import get_file_name, \
    get_dir_name, get_host, get_absolute_url, \
    get_main_page_url

URL = 'https://ru.hexlet.io/courses'
URL_FILE_NAME = 'ru-hexlet-io-courses.html'
URL_DIR_NAME = 'ru-hexlet-io-courses_files'
IMG_URL = 'https://ru.hexlet.io/assets/professions/nodejs.png'
IMG_URL_SHORT = '/assets/professions/nodejs.png'
IMG_FILE_NAME = 'ru-hexlet-io-assets-professions-nodejs.png'
IMG_DIR_NAME = 'ru-hexlet-io-assets-professions-nodejs_files'
SCRIPT_URL = 'https://ru.hexlet.io/packs/js/runtime.js'
SCRIPT_URL_SHORT = '/packs/js/runtime.js'
SCRIPT_FILE_NAME = 'ru-hexlet-io-packs-js-runtime.js'
LINK_URL = 'https://ru.hexlet.io/assets/application.css'
LINK_FILE_NAME = 'ru-hexlet-io-assets-application.css'
HOST = 'ru.hexlet.io'
MAIN_PAGE = 'https://ru.hexlet.io'

@pytest.mark.parametrize('url, file_name', [(URL, URL_FILE_NAME),
                                            (IMG_URL, IMG_FILE_NAME),
                                            (SCRIPT_URL, SCRIPT_FILE_NAME),
                                            (LINK_URL, LINK_FILE_NAME)])
def test_file_name(url, file_name):
    assert get_file_name(url) == file_name


@pytest.mark.parametrize('file_name, dir_name', [(URL_FILE_NAME,
                                                  URL_DIR_NAME),
                                                 (IMG_FILE_NAME,
                                                  IMG_DIR_NAME)])
def test_dir_name(file_name, dir_name):
    assert get_dir_name(file_name) == dir_name


@pytest.mark.parametrize('url, host', [(URL, HOST),
                                       (IMG_URL, HOST)])
def test_get_host(url, host):
    assert get_host(url) == host


@pytest.mark.parametrize('main_page, short_url, absolute_url',
                         [(MAIN_PAGE, IMG_URL_SHORT, IMG_URL),
                          (MAIN_PAGE, SCRIPT_URL_SHORT, SCRIPT_URL)])
def test_get_absolute_url(main_page, short_url, absolute_url):
    assert get_absolute_url(main_page, short_url) == absolute_url


def test_get_main_page():
    assert get_main_page_url(URL) == 'https://ru.hexlet.io'
