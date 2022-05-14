import re
import os
from urllib.parse import urlparse


def get_file_name(url):
    url_parse = urlparse(url)
    pattern_for_change = r'\W|\_'
    path_split = os.path.splitext(url_parse.path)
    ext = '.html' if path_split[1] == '' else path_split[1]
    result = re.sub(pattern_for_change, '-',
                    url_parse.netloc + path_split[0]) + ext
    return result


def get_dir_name(file_name):
    return os.path.splitext(file_name)[0] + '_files'


def get_main_page_url(url):
    url_parse = urlparse(url)
    return f'{url_parse.scheme}://{url_parse.netloc}'


def get_absolute_url(main_page_url, url):
    url_parse = urlparse(url)
    return f'{main_page_url}{url}' if url_parse.netloc == '' else url


def get_host(url):
    url_parse = urlparse(url)
    return url_parse.netloc


def is_same_host(resource_host, url):
    return resource_host == get_host(url) or get_host(url) == ''
