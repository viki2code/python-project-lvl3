# !usr/bin/env python3

import os
import logging
import argparse
import sys
from page_loader.page_loader import download


def main():
    parser = argparse.ArgumentParser('Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument(
        '-o', '--output', default=os.getcwd(),
        help=f'output dir (default: "{os.getcwd()}")'
    )
    args = parser.parse_args()
    try:
        filepath = download(args.url, args.output)
    except Exception as unknown_error:
        logging.error(unknown_error)
        sys.exit(1)
    else:
        print(f'Page was successfully downloaded into "{filepath}"')
        sys.exit(0)


if __name__ == '__main__':
    main()
