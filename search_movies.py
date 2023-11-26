import argparse
import json
import logging

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def as_text(movie: dict):
    """ Keys to extract:
    .name
    .genre
    .description
    .director[].name
    .actors[].name
    """

    _text = movie['name'] + "\n"
    _text += str(movie['genre']) + "\n"
    _text += movie['description'] + "\n"
    _text += "Director: " + ", ".join([d['name'] for d in movie['director']]) + "\n"
    _text += "Actors: " + ", ".join([a['name'] for a in movie['actor']]) + "\n"

    return _text

def make_index(filename: str, search_keyword: str = "...", result_key: str = 'name'):
    with open(filename, 'r') as f:
        data = json.load(f)

    index = {}

    for i, movie in enumerate(data):
        if movie["@type"] != "Movie":
            continue

        title = movie[result_key]
        logger.debug(f'Processing {title}')

        movie_text = as_text(movie)
        for word in movie_text.split():
            word = word.lower()
            if word not in index:
                index[word] = []
            index[word].append(title)

    logger.info(f'Indexed {i+1} movies')
    return index

def search_index(index: dict, search_keyword: str = "..."):
    search_keyword = search_keyword.lower()
    if search_keyword not in index:
        logger.info(f'No results for "{search_keyword}"')
        return

    for title in index[search_keyword]:
        logger.info(f'Found: {title}')

def search_movies(filename: str, search_keyword: str = "..."):
    index = make_index(filename)

    logger.info(f'Searching for "{search_keyword}"')
    search_index(index, search_keyword)

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='top250.json')
    parser.add_argument('search_keyword')
    args = parser.parse_args()

    filename = args.file
    search_keyword = args.search_keyword
    search_movies(filename, search_keyword)
