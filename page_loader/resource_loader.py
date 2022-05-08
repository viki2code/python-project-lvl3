import os
from page_loader.app_logger import get_logger
from page_loader.url import get_file_name, \
    is_same_host, get_absolute_url, get_host, get_main_page_url
from page_loader.content import write_content

logger = get_logger(__name__)


def update_link(elements, path, folder_name, url):
    logger.debug('Start to update link:')
    data_to_load = []
    for element in elements:
        attribute = 'src' if element.get('src') is not None else 'href'
        link = element[attribute]
        if is_same_host(get_host(url), link):
            absolute_url = get_absolute_url(get_main_page_url(url), link)
            file_name = get_file_name(absolute_url)
            new_link = os.path.join(folder_name, file_name)
            property_resource = {'absolute_url': absolute_url,
                                 'folder_path':
                                     os.path.join(path, folder_name),
                                 'file_name': file_name
                                 }

            data_to_load.append(property_resource)
            logger.debug(f'Update: {element[attribute]} ---> {new_link}')
            element[attribute] = new_link
    return data_to_load


def download_resource(folder_path, data_to_load):
    if data_to_load is not None:
        try:
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
        except OSError as err:
            logger.error(f'Unable make dir {folder_path}')
            raise err
    for element in data_to_load:
        write_content(element['absolute_url'],
                      element['folder_path'],
                      element['file_name'])
        logger.debug(f'Loaded page {element["absolute_url"]} into '
                     f'{element["file_name"]}')
