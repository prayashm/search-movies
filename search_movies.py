import argparse
import json
import logging

DEBUG = False

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
    _text += " ".join([d['name'] for d in movie['director']]) + "\n"
    _text += " ".join([a['name'] for a in movie['actor']]) + "\n"

    return _text

def make_index(filename: str, search_keyword: str = "...", result_key: str = 'name'):
    with open(filename, 'r') as f:
        data = json.load(f)

    index = {}

    for i, movie in enumerate(data):
        if movie["@type"] != "Movie":
            continue

        title = movie[result_key]

        movie_text = as_text(movie)
        for word in movie_text.split():
            word = word.lower()
            if word not in index:
                index[word] = []
            index[word].append(title)

    logger.info(f'Indexed {i+1} movies')
    return index

def search_each_keyword(index: dict, keyword: str):
    hits = set()

    if keyword not in index:
        logger.debug(f'No results for keyword: {keyword}')
        return None

    for title in index[keyword]:
        logger.debug(f'Found: "{title}" using keyword: {keyword}')

        hits.add(title)

    return hits

def search_index(index: dict, search_keyword: str = "..."):
    search_keyword = search_keyword.lower()
    search_keywords = [keyword.strip() for keyword in search_keyword.split()]
    logger.debug(f'normalised search keywords: {search_keywords}')

    results = set()

    for keyword in search_keywords:
        hits = search_each_keyword(index, keyword)
        logger.debug(f'with: {keyword}, hits: {hits}')

        if hits is None:
            return []

        if len(results) == 0:
            results.update(hits)
        else:
            results.intersection_update(hits)

    return results


def search_movies(filename: str, search_keyword: str = "..."):
    index = make_index(filename)

    # for keyword, results in index.items():
    #     print(f'{keyword}: {results}')

    logger.info(f'Searching for: {search_keyword}')
    results = search_index(index, search_keyword)
    logger.info(f'Found {len(results)} results')
    logger.info(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='top250.json')
    parser.add_argument('search_keyword')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    filename = args.file
    search_keyword = args.search_keyword
    DEBUG = args.debug

    if DEBUG:
        logger.setLevel(logging.DEBUG)

    search_movies(filename, search_keyword)
