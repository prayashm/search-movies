from search_movies import make_index, search_index

import unittest
from search_movies import make_index, search_index

class TestSearchMovies(unittest.TestCase):
    def setUp(self):
        self.filename = 'top250.json'
        self.index = make_index(self.filename)

    def test_search_movies(self):
        test_cases = [
            ('morgan', ['Unforgiven', 'The Wizard of Oz', 'The Shawshank Redemption', 'Se7en', 'Million Dollar Baby']),
            (' morgan ', ['Unforgiven', 'The Wizard of Oz', 'The Shawshank Redemption', 'Se7en', 'Million Dollar Baby']),
            ('freeman', ['Unforgiven', 'The Shawshank Redemption', 'Se7en', 'Raiders of the Lost Ark', 'Million Dollar Baby']),
            ('morgan freeman',['Unforgiven', 'The Shawshank Redemption', 'Se7en', 'Million Dollar Baby']),
            ('MorGan FrEeMan', ['Unforgiven', 'The Shawshank Redemption', 'Se7en', 'Million Dollar Baby']),
            ('asdfasdfasdfasdf', [])
        ]

        for search_keyword, expected_results in test_cases:
            with self.subTest():
                results = search_index(self.index, search_keyword)

                self.assertEqual(len(results), len(expected_results))
                for result in results:
                    self.assertIn(result, expected_results)

if __name__ == '__main__':
    unittest.main()
