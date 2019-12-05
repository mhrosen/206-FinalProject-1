#limit --> default is 50;
#attribute = movie
import unittest
import json
import requests
import os

def get_api_data_popular():
    # Get 20 most popular movies from TMDB
    baseurl= "https://itunes.apple.com/search?attribute={}&limit=20"
    popular_list = []

#     # Each fetch returns 20 movies on a page
#     # This iterates 5 times to return 100 movies
#     for num in range(1,6):
#         popular_url = baseurl.format(api_key, num)
#         r = requests.get(popular_url)
#         data = json.loads(r.text)
#         results = data["results"]
#         popular_list = popular_list + results
#     return popular_list

# def create_cache(pop_results):
#     # Cache was created on 12/4/19 at 9:15 PM

#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     cache_file = dir_path + '/' + "popular_movies.json"

#     movie_results = {}
#     movie_results['results'] = pop_results

#     with open (cache_file, 'w') as outfile:
#         json.dump(movie_results, outfile, indent = 2)

# class TestAllMethods(unittest.TestCase):
#     def test_get_api_data_popular(self):
#         results_dict = get_api_data_popular()
#         self.assertEqual(len(results_dict), 100) # Testing if 100 movies are added
#         self.assertFalse(results_dict[0] == results_dict[20]) # Testing if unique pages were returned

# def main():
#     results = get_api_data_popular() 
#     create_cache(results)

# if __name__ == "__main__":
#     main()
#     unittest.main(verbosity = 2)