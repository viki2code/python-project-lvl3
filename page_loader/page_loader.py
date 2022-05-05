import os
from page_loader.content import write_file, get_request
from page_loader.url import get_file_name, get_folder
from page_loader.resource_loader import resource_download
from bs4 import BeautifulSoup
from page_loader.app_logger import get_logger
TAG = ['img', 'script', 'link']


def download(url, path):
    logger = get_logger(__name__)
    logger.debug(f'Download page: "{url}" into dir: "{path}"')
    file_name = get_file_name(url)
    file = os.path.join(path, file_name)
    soup = BeautifulSoup(get_request(url).content, 'html.parser')
    # load src objects and replace path
    resource_download(soup.find_all(TAG), path, get_folder(file_name), url)
    write_file(file, soup.prettify())
    logger.debug(f'Page was successfully downloaded into "{file}"')
    return file
