import pytest
from page_loader.page_loader import download

STATUS_CODE = [404, 500]
URL = 'mock://test.com'


@pytest.mark.parametrize('code', STATUS_CODE)
def test_response_error_code(requests_mock, code, tmp_path):
    requests_mock.get(URL, status_code=code)
    with pytest.raises(Exception):
        assert download(URL, tmp_path)


def test_write_content(requests_mock):
    requests_mock.get(URL, text='data')
    with pytest.raises(Exception):
        assert download(URL, 'tmp_path')
