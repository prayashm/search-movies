import argparse
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def as_text(movie: dict):
    """ Keys to extract:
    .name
    .genre
    .description
    .director[].name
    .actors[].name
    """

    _text = ""

    return _text

def make_index(filename: str, search_keyword: str = "...", result_key: str = 'name'):
    with open(filename, 'r') as f:
        data = json.load(f)

    index = {}

    for movie in data:
        if movie["@type"] != "Movie":
            continue

        title = movie['name']

        logger.info(f'Processing {title}')
        index[title] = as_text(movie)

    return index

def search_movies(filename: str):
    index = make_index(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='top250.json')
    args = parser.parse_args()

    filename = args.file
    search_movies(filename)
