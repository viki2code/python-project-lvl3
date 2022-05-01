import requests


def write_file(file, data):
    mode = 'wb' if isinstance(data, bytes) else 'w'
    with open(file, mode) as opened_file:
        opened_file.write(data)


def get_page_content(url):
    r = requests.get(url, allow_redirects=True)
    return r.content


def get_page_text(url):
    r = requests.get(url, allow_redirects=True)
    return r.text
