import os
import pytest
from page_loader.content import save_content, \
    get_content_length, get_request

STATUS_CODE = [404, 500]
URL = 'https://ru.hexlet.io/courses'

FIXTURES_FOLDER = 'fixtures'
MOCK_FOLDER = 'fixtures/mocks'


def read_file(path_file, mode='r'):
    with open(path_file, mode) as file:
        result = file.read()
    return result


def get_path(file_name, folder_name):
    return os.path.join(os.path.dirname(__file__), folder_name, file_name)


FILE_SITE = get_path('web_site.html', MOCK_FOLDER)
FILE_IMG = get_path('nodejs.png', MOCK_FOLDER)


@pytest.mark.parametrize('code', STATUS_CODE)
def test_response_error_code(requests_mock, code, tmp_path):
    requests_mock.get(URL, status_code=code)
    with pytest.raises(Exception):
        assert get_request(URL)


def test_content_length(requests_mock):
    content = read_file(FILE_SITE, 'rb')
    headers_html = {'content-length': str(len(content))}
    requests_mock.get(URL, content=content, headers=headers_html)
    assert get_content_length(get_request(URL)) == len(content)


def test_save_content(tmp_path):
    content = read_file(FILE_SITE, 'r')
    file_path = os.path.join(tmp_path, '1.html')
    save_content(file_path, content)
    assert read_file(file_path, 'r') == content


def test_save_content_exception():
    content = read_file(FILE_SITE, 'r')
    file_path = os.path.join('tmp_path', '1.html')
    with pytest.raises(Exception):
        assert save_content(file_path, content)
