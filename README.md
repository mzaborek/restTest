# restTest
Simple REST API implemented using Django with it's REST framework.
It uses external API to get data about movie of a given title and stores it.
It is also possible to store comments for each movie.

Install packages from `requirements.txt`
To run server execute command: `python3 manage.py runserver`

## Movies
* **URL**

  /movies/
  
* **Method:**
  
  `GET` | `POST`
  
*  **URL Params (optional)**

   `Year`<br />
   `Country`<br />
   `ordering` = `Year` | `metascore`

* **Data Params**
  
    Posting data requires one parameter: `Title`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
    "id": 60,
    "Title": "Twin Peaks",
    "Year": "1990–1991",
    "Rated": "TV-MA",
    "Released": "08 Apr 1990",
    "Runtime": "47 min",
    "Genre": "Crime, Drama, Mystery",
    "Director": "N/A",
    "Writer": "Mark Frost, David Lynch",
    "Actors": "Kyle MacLachlan, Michael Ontkean, Mädchen Amick, Dana Ashbrook",
    "Plot": "An idiosyncratic FBI agent investigates the murder of a young woman in the even more idiosyncratic town of Twin Peaks.",
    "Language": "English, Icelandic, Afrikaans, Norwegian",
    "Country": "USA",
    "Awards": "Won 3 Golden Globes. Another 12 wins & 44 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BMTExNzk2NjcxNTNeQTJeQWpwZ15BbWU4MDcxOTczOTIx._V1_SX300.jpg",
    "Ratings": "[{'Source': 'Internet Movie Database', 'Value': '8.8/10'}]",
    "Metascore": "N/A",
    "imdbRating": "8.8",
    "imdbVotes": "142,892",
    "imdbID": "tt0098936",
    "Type": "series",
    "DVD": "",
    "BoxOffice": "",
    "Production": "",
    "Website": "",
    "totalSeasons": "2"
}`
    
  * **Code:** 200 <br />
    **Content:** `[
    {
        "id": 61,
        "Title": "Twin Peaks",
        "Year": "1990–1991",
        "Rated": "TV-MA",
        "Released": "08 Apr 1990",
        "Runtime": "47 min",
        "Genre": "Crime, Drama, Mystery",
        "Director": "N/A",
        "Writer": "Mark Frost, David Lynch",
        "Actors": "Kyle MacLachlan, Michael Ontkean, Mädchen Amick, Dana Ashbrook",
        "Plot": "An idiosyncratic FBI agent investigates the murder of a young woman in the even more idiosyncratic town of Twin Peaks.",
        "Language": "English, Icelandic, Afrikaans, Norwegian",
        "Country": "USA",
        "Awards": "Won 3 Golden Globes. Another 12 wins & 44 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTExNzk2NjcxNTNeQTJeQWpwZ15BbWU4MDcxOTczOTIx._V1_SX300.jpg",
        "Ratings": "[{'Source': 'Internet Movie Database', 'Value': '8.8/10'}]",
        "Metascore": "N/A",
        "imdbRating": "8.8",
        "imdbVotes": "142,892",
        "imdbID": "tt0098936",
        "Type": "series",
        "DVD": "",
        "BoxOffice": "",
        "Production": "",
        "Website": "",
        "totalSeasons": "2"
    },
    {
        "id": 62,
        "Title": "Giant",
        "Year": "1956",
        "Rated": "G",
        "Released": "24 Nov 1956",
        "Runtime": "201 min",
        "Genre": "Drama, Western",
        "Director": "George Stevens",
        "Writer": "Edna Ferber (from the novel by), Fred Guiol (screen play), Ivan Moffat (screen play)",
        "Actors": "Elizabeth Taylor, Rock Hudson, James Dean, Carroll Baker",
        "Plot": "Sprawling epic covering the life of a Texas cattle rancher and his family and associates.",
        "Language": "English, Spanish",
        "Country": "USA",
        "Awards": "Won 1 Oscar. Another 6 wins & 15 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYWQ3ZmZhMmQtODQyMS00Y2Q0LThlOTAtM2NiMDMyNDdlYmQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SX300.jpg",
        "Ratings": "[{'Source': 'Internet Movie Database', 'Value': '7.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '95%'}]",
        "Metascore": "N/A",
        "imdbRating": "7.7",
        "imdbVotes": "29,715",
        "imdbID": "tt0049261",
        "Type": "movie",
        "DVD": "10 Jun 2003",
        "BoxOffice": "N/A",
        "Production": "Warner Bros. Pictures",
        "Website": "N/A",
        "totalSeasons": ""
    }
]`
 
* **Error Response:**

  Some possible error responses:
  
  * **Code:** 400 BAD REQUEST <br />
    Data not found in OMDB
  OR

  * **Code:** 408 REQUEST TIMEOUT <br />
    Possibly OMDB timeout


## Comments

* **URL**

  /comments/
  
* **Method:**
  
  `GET` | `POST`
  
*  **URL Params (optional)**

   `movie` - get comments for a movie with given id<br />
   
* **Data Params**
  
    `Movie` - id of a movie (foreign key)<br />
    `commentText` - body of a comment
    
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
        "movie": 61,
        "commentText": "Dd ( ͡° ͜ʖ ͡°)"
    },
    {
        "movie": 61,
        "commentText": "asdasdasd"
    }
]`
    
  * **Code:** 201 <br />
    **Content:** `
{
    "movie": 61,
    "commentText": "Dd ( ͡° ͜ʖ ͡°)"
}`
 
