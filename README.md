## search movies

## Setup
- Ensure you have `Python 3.9.7`

## Usage
- `python search_movies.py "morgan"`
- `python search_movies.py "morgan freeman" --debug` will print debug logs

### Approach
- [x] Let's start with basic linear search (with python's `__contains__`)
    - it could be like movie_name: long text of all the thing by which one can search (actor names, categories)
    - will satisfy the current requirement
    - may not scale if filters are needed
    - assumption: split keyword search should return union of each word's results i.e. movies("morgan") UNION movies("freeman")
    - searching for "morgan freeman" yields results from all morgans + freemans
    - this contradicts the requirement: _For e.g. query can be “morgan freeman” which will return a list of movies which has that actor in it._
    - let's change our assumption for combine search results to be an intersection i.e. movies("morgan") intersect movies("freeman")
    - bug: morgan,:The Wizard of Oz is indexed, fix: do not surround with extra chars in index
- [ ] Add time tracking in index creation and search

Stretch goals:
- ~~[ ] Show progress bar when searching~~, it's super quick
- [x] Add reverse index 
- [ ] Add Typo tolerance with regex
- [ ] Trie based search
- [ ] Expose intersection / union of results via `morgan+freeman` vs `morgan freeman`