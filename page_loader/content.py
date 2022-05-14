import requests
from bs4 import BeautifulSoup

from page_loader.app_logger import get_logger

TAG = ['img', 'script', 'link']
logger = get_logger(__name__)
CHUNK_SIZE = 1024


def get_request(url):
    try:
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logger.error(f'Http Error: {errh}')
        raise errh
    except requests.exceptions.ConnectionError as errc:
        logger.error(f'Error Connecting: {errc}')
        raise errc
    except requests.exceptions.RequestException as err:
        logger.error(f'Request exception: {err}')
        raise err
    return r


def parse(url):
    soup = BeautifulSoup(get_request(url).content, 'html.parser')
    all_tags = soup.find_all(TAG)
    return all_tags, soup


def get_content_length(request):
    if request.headers.get('Content-Length') is not None:
        return int(request.headers.get('Content-Length'))
    else:
        return len(request.content)


def get_attribute(element):
    if element.get('src') is not None:
        return 'src'
    elif element.get('href'):
        return 'href'
    else:
        return None


def save_content(file_path, data, iter_param=None, mode='w'):
    try:
        with open(file_path, mode) as opened_file:
            for chunk in data:
                opened_file.write(chunk)
                if iter_param is not None:
                    iter_param.next(CHUNK_SIZE)
    except PermissionError as permission:
        logger.error(f'Access denied to file {file_path}')
        raise permission
    except OSError as err:
        logger.error(f'Unable to write to file {file_path}')
        raise err
