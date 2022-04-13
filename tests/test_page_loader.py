import requests
import requests_mock
from page_loader.page_loader import download
from page_loader.url import get_file_name, get_url_path


def test_file_name():
    url = 'https://ru.hexlet.io/courses'
    url_path = get_url_path(url)
    assert url_path == 'ru.hexlet.io/courses'
    assert get_file_name(url_path) == 'ru-hexlet-io-courses.html'




def test_path_file(tmpdir):
    url = 'mock://test.com'
    path = tmpdir.mkdir('temp')
    with requests_mock.Mocker() as m:
        m.get(url, text='data')
        assert download(url, path) == path +'/test-com.html'
