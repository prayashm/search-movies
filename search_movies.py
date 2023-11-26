import argparse
import json

def make_index(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)

    index = {}
    return index

def search_movies(filename: str):
    index = make_index(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='top250.json')
    args = parser.parse_args()

    filename = args.file
