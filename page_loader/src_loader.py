import os
from page_loader.app_logger import get_logger
from page_loader.url import get_file_name, \
    is_same_host, get_absolute_url, get_host, get_main_page_url
from page_loader.content import write_content


def obj_download(elements, path, folder_name, url):
    new_folder_path = os.path.join(path, folder_name)
    logger = get_logger(__name__)
    logger.debug('Start to load resource:')
    for element in elements:
        attribute = 'src' if element.get('src') is not None else 'href'
        link = element[attribute]
        if is_same_host(get_host(url), link):
            absolute_url = get_absolute_url(get_main_page_url(url), link)
            if not os.path.isdir(new_folder_path):
                os.mkdir(new_folder_path)
            file_name = get_file_name(absolute_url)
            new_link = os.path.join(folder_name, file_name)
            write_content(absolute_url, os.path.join(path, folder_name),
                          file_name)
            logger.debug(f'Loaded {absolute_url} path file {new_link}')
            element[attribute] = new_link
