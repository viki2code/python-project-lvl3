import re
import os
from urllib.parse import urlparse


def get_url_path(url):
    url_parse = urlparse(url)
    path_split = os.path.splitext(url_parse.path)
    result = f'{url_parse.netloc}{path_split[0]}'
    if path_split[1] != '.html':
        result += path_split[1]
    return result


def get_file_name(url):
    pattern_for_change = r'\W|\_'
    result = re.sub(pattern_for_change, '-', url) + '.html'
    return result
