import os
from page_loader.content import write_file, get_request
from page_loader.url import get_file_name, get_folder
from page_loader.src_loader import obj_download
from bs4 import BeautifulSoup

TAG = ['img', 'script', 'link']


def download(url, path):
    file_name = get_file_name(url)
    file = os.path.join(path, file_name)
    soup = BeautifulSoup(get_request(url).content, 'html.parser')
    # load src objects and replace path
    obj_download(soup.find_all(TAG), path, get_folder(file_name), url)
    write_file(file, soup.prettify())
    return file
