## search movies

## Setup
- Ensure you have `Python 3.9.7`

## Usage
- `python search_movies.py "morgan"`

### Approach
[x] Let's start with basic linear search (with python's __contains__)
    - it could be like movie_name: long text of all the thing by which one can search (actor names, categories)
    - will satisfy the current requirement
    - may not scale if filters are needed
    - assumption: split keyword search should return union of each word's results i.e. movies("morgan") + movies("freeman")
[ ] Add time tracking in index creation and search

Stretch goals:
[ ] Show progress bar when searching
[ ] Add reverse index / trie based search