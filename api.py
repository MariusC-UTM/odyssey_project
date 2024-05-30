from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre
from scraper import extract_movie_data_for_year  # Import the scraping function and Movie model
import socket


app = FastAPI()


def load_movies() -> Dict[int, List[Dict]]:
    """Load the movie data from a JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    try:
        with open('data_storage/movies.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def fetch_movie_data_for_year(year: int) -> List[Dict]:
    """Fetch the most popular movies for a given year and extract detailed information.

    Args:
        year (int): The year for which to fetch the most popular movies.

    Returns:
        List[Dict]: A list of dictionaries containing detailed movie information.
    """
    response_movies = fetch_movie_data_for_year(year)
    movies = []
    for movie in response_movies:
        movie_type = extract_movie_type(movie)
        duration_period = extract_duration_period(movie)
        name = extract_name(movie, movie_type)
        genre = extract_genre(movie)
        movies.append(
            {
                'name': name,
                'type': movie_type,
                'duration': duration_period,
                'genre': genre
            }
        )
    return movies


def save_movies(movies: Dict[int, List[Dict]]):
    """Save the movie data to a JSON file.

    Args:
        movies (Dict[int, List[Dict]]): The movie data to save.
    """
    with open('data_storage/movies.json', 'w') as file:
        json.dump(movies, file, indent=4)


@app.get("/movies", response_model=Dict[int, List[Dict]])
def get_movies() -> Dict[int, List[Dict]]:
    """Retrieve all movies from the JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    return load_movies()


@app.get("/movies/{year}", response_model=List[Dict])
def get_movies_by_year(year: int) -> List[Dict]:
    """Retrieve movies for a specific year from the JSON file.

    Args:
        year (int): The year for which to retrieve movies.

    Returns:
        List[Dict]: A list of movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year are not found.
    """
    movies = load_movies()
    if str(year) in movies:
        return movies[str(year)]
    raise HTTPException(status_code=404, detail="Movies not found for this year")


@app.post("/movies/{year}", response_model=List[Dict])
def add_movies_by_year(year: int) -> List[Dict]:
    """Fetch and add movies for a specific year to the JSON file.

    Args:
        year (int): The year for which to fetch and add movies.

    Returns:
        List[Dict]: A list of newly added movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year already exist.
    """
    movies = load_movies()
    if str(year) in movies:
        raise HTTPException(status_code=400, detail="Movies for this year already exist")
    
    new_movies = fetch_movie_data_for_year(year)
    movies[str(year)] = new_movies
    save_movies(movies)
    return new_movies


@app.put("/movies/{year}", response_model=List[Dict])
def update_movie(year: int) -> List[Dict]:
    """Update movies for a specific year in the JSON file.

    Args:
        year (int): The year for which to update movies.

    Returns:
        List[Dict]: A list of updated movies for the specified year.
    """
    movies = load_movies()
    new_movies = fetch_movie_data_for_year(year)
    movies[str(year)] = new_movies
    save_movies(movies)
    return new_movies


@app.delete("/movies/{year}/{name}", response_model=Dict)
def delete_movie(year: int, name: str) -> Dict:
    """Delete a movie for a specific year from the JSON file.

    Args:
        year (int): The year of the movie to delete.
        name (str): The name of the movie to delete.

    Returns:
        Dict: The deleted movie's details.

    Raises:
        HTTPException: If the movie for the specified year and name is not found.
    """
    movies = load_movies()
    year_str = str(year)
    if year_str not in movies:
        raise HTTPException(status_code=404, detail="Movies not found for this year")

    for i, movie in enumerate(movies[year_str]):
        if movie['name'].lower() == name.lower():
            deleted_movie = movies[year_str].pop(i)
            save_movies(movies)
            return deleted_movie
    
    raise HTTPException(status_code=404, detail="Movie not found")


def api_run(host: str, port: int):
    """Run the API server if it is not already running.

        Args:
            host (str): The host address to run the server.
            port (int): The port to run the server.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except socket.error as e:
        print('Error:', e)
        print(f'Info: Uvicorn is already running on {host}:{port}')
        return
    else:
        s.close()

        import uvicorn
        uvicorn.run(app, host = host, port = port)


if __name__ == "__main__":
    api_run("127.0.0.100", 8000)
