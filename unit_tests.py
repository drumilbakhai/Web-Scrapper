import unittest
from SearchStringUtility import SearchStringUtility

class UnitTests:

    def test_search_string_utility(self):
        search_term = "bluetooth headphones"
        final_search_string = "st=bluetooth+headphones"
        result = SearchStringUtility.prepare_search_string(search_term)
        self.assertEqual(result, final_search_string)

if __name__ == '__main__':
    unittest.main()