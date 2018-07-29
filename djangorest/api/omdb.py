import requests


class MovieData():
    url = 'http://www.omdbapi.com'
    apikey = 'ad1960a5'
    # fields = ["Season", 'Runtime']

    fields = ["Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot",
              "Language", "Country", "Awards", "Poster", "Ratings", "Metascore", "imdbRating", "imdbVotes",
              "imdbID", "Type", "DVD", "BoxOffice", "Production", "Website", "Response", "totalSeasons"]

    def __init__(self):
        self.session = requests.Session()

    def request(self, title, timeout):
        params = {
            't': title,
            'apikey': self.apikey
        }
        res = self.session.get(self.url, params=params, timeout=timeout)

        res.raise_for_status()

        res = res.json()

        # init field with empty string if it's not in the response
        for field in self.fields:
            res[field] = res.get(field, "")

        res = {key: value for key, value in res.items() if key in self.fields}

        return res

    # http://www.omdbapi.com/?apikey=ad1960a5
