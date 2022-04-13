import argparse
from page_loader.page_loader import download
import os

def main():
    parser = argparse.ArgumentParser(description='Usage: page-loader [options] <url>')
    parser.add_argument('page', type=str)
    parser.add_argument(
        '--output', default=os.getcwd(),
        help='output dir (default: "/app")'
    )
    args = parser.parse_args()
    file_path = download(args.page, args.output)
    print(file_path)

if __name__ == '__main__':
    main()