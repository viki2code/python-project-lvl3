import os
from page_loader.url import get_file_name, is_same_host, get_absolute_url, get_host, get_main_page_url
from page_loader.file import write_file, get_page_content


def obj_download(elements, path, folder_name, url):
    new_folder_path = os.path.join(path, folder_name)
    for element in elements:
        link = element['src']
        if is_same_host(get_host(url), link):
            print(get_main_page_url(url))
            print(f'link = {link}')
            print(f'before:{element}')
            absolute_url =get_absolute_url(get_main_page_url(url), link)
            content = get_page_content(absolute_url)
            if not os.path.isdir(new_folder_path):
                os.mkdir(new_folder_path)
            new_link = os.path.join(folder_name, get_file_name(absolute_url))
            file_path = os.path.join(path, new_link)
            write_file(file_path, content)
            element['src'] = new_link
            print(f'{element["src"]}  = {new_link}')
            print(f'after:{element}')
