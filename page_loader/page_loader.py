import os

from page_loader.url import get_file_name, get_dir_name
from page_loader.app_logger import get_logger
from page_loader.content import save_content
from page_loader.resource_loader import prepare_page, download_resource

logger = get_logger(__name__)


def download(url, path):
    logger.debug(f'Download page: "{url}" into dir: "{path}"')
    file_name = get_file_name(url)
    dir_for_resource = get_dir_name(file_name)
    file_path = os.path.join(path, file_name)
    data_to_load, html = prepare_page(url, dir_for_resource)
    save_content(file_path, html)
    dir_path = os.path.join(path, dir_for_resource)
    download_resource(dir_path, data_to_load)
    logger.debug(f'Page was successfully downloaded into "{file_path}"')
    return file_path
