import requests
from api import api_run

HOST = '127.0.0.100'
PORT = 8000
BASE_URL = f'http://{HOST}:{PORT}'


def get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def get_movies_by_year(year):
    response = requests.get(f"{BASE_URL}/movies/{year}")
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def add_movies_by_year(year):
    response = requests.post(f"{BASE_URL}/movies/{year}")
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def update_movies_by_year(year):
    response = requests.put(f"{BASE_URL}/movies/{year}")
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def delete_movie_by_year_and_name(year, name):
    response = requests.delete(f"{BASE_URL}/movies/{year}/{name}")
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def main():
    api_run(HOST, PORT)

    while True:
        print('\nOptions menu:')
        print('1 - Show all movies.')
        print('2 - Get all movies by year.')
        print('3 - Add all movies by year.')
        print('4 - Update all movies by year.')
        print('5 - Delete movies by year and name.')
        print('0 - Exit.')
        option = input('Option: ')

        if option == '1':
            get_all_movies()

        elif option == '2':
            get_movies_by_year(2024)

        elif option == '3':
            add_movies_by_year(2024)

        elif option == '4':
            update_movies_by_year(2024)

        elif option == '5':
            delete_movie_by_year_and_name(2024, 'Dune: Part Two')

        elif option == '0':
            break


if __name__ == "__main__":
    main()
