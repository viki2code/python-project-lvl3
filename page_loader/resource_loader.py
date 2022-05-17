import os
from bs4 import BeautifulSoup
from page_loader.app_logger import get_logger
from page_loader.url import get_file_name, \
    get_absolute_url, get_main_page_url, is_same_host, \
    get_host
from page_loader.content import get_request, save_content
from progress.bar import IncrementalBar

TAG = {'img': 'src', 'script': 'src', 'link': 'href'}
logger = get_logger(__name__)


def get_new_link(resource_dir, file_name):
    return os.path.join(resource_dir, file_name)


def prepare_page(url, resource_dir):
    soup = BeautifulSoup(get_request(url).content, 'html.parser')
    tags = soup.find_all(TAG.keys())
    data_to_load = []
    for element in tags:
        attribute = TAG[element.name]
        if attribute is not None \
                and is_same_host(get_host(url),
                                 element[attribute]):
            absolute_url = get_absolute_url(get_main_page_url(url),
                                            element[attribute])
            file_name = get_file_name(absolute_url)
            new_link = get_new_link(resource_dir, file_name)
            property_resource = {'absolute_url': absolute_url,
                                 'file_name': file_name}
            data_to_load.append(property_resource)
            logger.debug(f'Update: {element[attribute]} ---> {new_link}')
            element[attribute] = new_link
    html = soup.prettify()
    return data_to_load, html


def download_resource(folder_path, data_to_load):
    if data_to_load is not None:
        try:
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
        except OSError as err:
            logger.error(f'Unable make dir {folder_path}')
            raise err
    bar_width = len(data_to_load)
    bar = IncrementalBar('Downloading:',
                         max=bar_width,
                         suffix='%(percent)d%%')
    for element in data_to_load:
        r = get_request(element['absolute_url'])
        save_content(os.path.join(folder_path, element['file_name']),
                     r.content,
                     mode='wb')
        logger.debug(f'Loaded page {element["absolute_url"]} into '
                     f'{element["file_name"]}')
        bar.next()
    bar.finish()
