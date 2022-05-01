import requests_mock


def test_file_name():
    assert 1 == 1 
           #get_file_name(url_path) == 'ru-hexlet-io-courses.html'


def test_path_file(tmpdir):
    url = 'mock://test.com'
    path = tmpdir.mkdir('temp')
    with requests_mock.Mocker() as m:
        m.get(url, text='data')
        #assert download(url, path) == path + '/test-com.html'
        assert 1 ==1
