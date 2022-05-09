import os

import requests
from progress.bar import IncrementalBar

from page_loader.app_logger import get_logger

logger = get_logger(__name__)


def write_file(file, data):
    mode = 'wb' if isinstance(data, bytes) else 'w'

    try:
        with open(file, mode) as opened_file:
            opened_file.write(data)
    except PermissionError as permission:
        logger.error(f'Access denied to file {file}')
        raise permission
    except FileNotFoundError as nfound:
        logger.error(f'File not found: {file}')
        raise nfound
    except OSError as err:
        logger.error(f'Unable to write to file {file}')
        raise err


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


def get_content_length(request):
    if request.headers.get('Content-Length') is not None:
        return int(request.headers.get('Content-Length'))
    else:
        return len(request.content)


def write_content(url, path, file_name):
    chunk_size = 1024
    r = get_request(url)
    content_length = get_content_length(r)
    bar = IncrementalBar(f'{file_name}',
                         max=content_length,
                         suffix='%(percent)d%%')

    try:
        with open(os.path.join(path, file_name), 'wb') as opened_file:
            for chunk in r.iter_content(chunk_size=chunk_size):
                opened_file.write(chunk)
                bar.next(chunk_size)
            bar.finish()
    except PermissionError as permission:
        logger.error(f'Access denied to file {file_name}')
        raise permission
    except FileNotFoundError as nfound:
        logger.error(f'File not found: {file_name}')
        raise nfound
    except OSError as err:
        logger.error(f'Unable to write to file {file_name}')
        raise err
