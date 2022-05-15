import os
from page_loader.app_logger import get_logger
from page_loader.url import get_file_name, \
    get_absolute_url, get_main_page_url, is_same_host, \
    get_host
from page_loader.content import get_request, get_attribute, \
    get_content_length, save_content, CHUNK_SIZE
from progress.bar import IncrementalBar

logger = get_logger(__name__)


def get_new_link(resource_dir, file_name):
    return os.path.join(resource_dir, file_name)


def prepare_page(url, tags, resource_dir):
    data_to_load = []
    for element in tags:
        attribute = get_attribute(element)
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
        r = get_request(element['absolute_url'])
        content_length = get_content_length(r)
        bar = IncrementalBar(f'{element["file_name"]}',
                             max=content_length,
                             suffix='%(percent)d%%')
        save_content(os.path.join(folder_path, element['file_name']),
                     r.iter_content(chunk_size=CHUNK_SIZE),
                     mode='wb',
                     iter_param=bar)
        logger.debug(f'Loaded page {element["absolute_url"]} into '
                     f'{element["file_name"]}')
        bar.finish()
