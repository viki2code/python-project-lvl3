import os
from page_loader.content import write_file, get_request
from page_loader.url import get_file_name, get_folder
from page_loader.resource_loader import update_link, download_resource
from bs4 import BeautifulSoup
from page_loader.app_logger import get_logger
TAG = ['img', 'script', 'link']


def download(url, path):
    logger = get_logger(__name__)
    logger.debug(f'Download page: "{url}" into dir: "{path}"')
    file_name = get_file_name(url)
    folder_for_resource = get_folder(file_name)
    file = os.path.join(path, file_name)
    soup = BeautifulSoup(get_request(url).content, 'html.parser')
    data_to_load = update_link(soup.find_all(TAG), path,
                               folder_for_resource, url)
    logger.debug('Start to load resource:')
    download_resource(os.path.join(path, folder_for_resource),
                      data_to_load)
    write_file(file, soup.prettify())
    logger.debug(f'Page was successfully downloaded into "{file}"')
    return file
