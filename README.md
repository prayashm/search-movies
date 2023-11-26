## search movies

## Setup
- Ensure you have `Python 3.9.7`

## Usage
- `python search_movies.py "morgan"`
```
[INFO] Indexed 250 movies
[INFO] Searching for: morgan
[INFO] Found 5 results
[INFO] {'Million Dollar Baby', 'The Shawshank Redemption', 'Se7en', 'The Wizard of Oz', 'Unforgiven'}
```

- `python search_movies.py "morgan freeman" --debug` will print debug logs
```
[INFO] Indexed 250 movies
[INFO] Searching for: morgan freeman
[DEBUG] normalised search keywords: ['morgan', 'freeman']
[DEBUG] Found: "Unforgiven" using keyword: morgan
[DEBUG] Found: "The Wizard of Oz" using keyword: morgan
[DEBUG] Found: "The Shawshank Redemption" using keyword: morgan
[DEBUG] Found: "Se7en" using keyword: morgan
[DEBUG] Found: "Million Dollar Baby" using keyword: morgan
[DEBUG] with: morgan, hits: {'Million Dollar Baby', 'The Wizard of Oz', 'Se7en', 'The Shawshank Redemption', 'Unforgiven'}
[DEBUG] Found: "Unforgiven" using keyword: freeman
[DEBUG] Found: "The Shawshank Redemption" using keyword: freeman
[DEBUG] Found: "Se7en" using keyword: freeman
[DEBUG] Found: "Raiders of the Lost Ark" using keyword: freeman
[DEBUG] Found: "Million Dollar Baby" using keyword: freeman
[DEBUG] with: freeman, hits: {'Million Dollar Baby', 'Se7en', 'The Shawshank Redemption', 'Unforgiven', 'Raiders of the Lost Ark'}
[INFO] Found 4 results
[INFO] {'Se7en', 'The Shawshank Redemption', 'Unforgiven', 'Million Dollar Baby'}
```

- `python test_search_movies.py` will run tests
```
[INFO] Indexed 250 movies
.
----------------------------------------------------------------------
Ran 1 test in 0.007s

OK
```

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