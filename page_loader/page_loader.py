import requests
import os
from page_loader.file import write_file
from page_loader.url import get_file_name, get_url_path


def download(url, path):
    r = requests.get(url, allow_redirects=True)
    #content_type = str.split(r.headers['content-type'], ';')[0]
    #file = ''
    #if content_type == 'text/html':
    file = os.path.join(path, get_file_name(get_url_path(url)))
    write_file(file, r.text)
    return file
