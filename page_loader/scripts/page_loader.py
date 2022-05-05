import os
import argparse
from page_loader.page_loader import download


def main():
    parser = argparse.ArgumentParser('Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument(
        '--output', default=os.getcwd(),
        help=f'output dir (default: "{os.getcwd()}")'
    )
    args = parser.parse_args()
    file = download(args.url, args.output)
    print(f'Page was successfully downloaded into "{file}"')


if __name__ == '__main__':
    main()
