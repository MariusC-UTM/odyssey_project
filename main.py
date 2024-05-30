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
        print('    - Input:>2 *year*<')
        print('3 - Add all movies by year.')
        print('    - Input:>3 *year*<')
        print('4 - Update all movies by year.')
        print('    - Input:>4 *year*<')
        print('5 - Delete movies by year and name.')
        print('    - Input:>5 *year* *name*<')
        print('0 - Exit.')
        option = input('Option:> ')

        if option:
            option = option.split(' ', 2)

            if option[0] == '1':
                get_all_movies()

            elif option[0] == '2':
                if len(option) == 2:
                    get_movies_by_year(option[1])
                else:
                    print('No year specified.')

            elif option[0] == '3':
                if len(option) == 2:
                    add_movies_by_year(option[1])
                else:
                    print('No year specified.')

            elif option[0] == '4':
                if len(option) == 2:
                    update_movies_by_year(option[1])
                else:
                    print('No year specified.')

            elif option[0] == '5':
                if len(option) == 3:
                    delete_movie_by_year_and_name(option[1], option[2])
                else:
                    print('No year and/or name specified.')

            elif option[0] == '0':
                print('Exiting.')
                break

            else:
                print('Unknown option.')


if __name__ == "__main__":
    main()
