import requests

from page_loader.app_logger import get_logger

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


def get_content_length(request):
    if request.headers.get('Content-Length') is not None:
        return int(request.headers.get('Content-Length'))
    else:
        return len(request.content)


def save_content(file_path, data, mode='w'):
    try:
        with open(file_path, mode) as opened_file:
            opened_file.write(data)
    except PermissionError as permission:
        logger.error(f'Access denied to file {file_path}')
        raise permission
    except OSError as err:
        logger.error(f'Unable to write to file {file_path}')
        raise err
