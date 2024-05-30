import requests
# from api import api_run

HOST = '127.0.0.100'
PORT = 8000
BASE_URL = f'http://{HOST}:{PORT}'


def check_response(response):
    if response.status_code == 200:
        if response.json():
            print('Received status code:')
            return response.json()
        else:
            print('No status code received.')
    else:
        if response.text:
            print('Received text:')
            return response.text
        else:
            print('No text received.')


def get_all_movies():
    try:
        response = requests.get(f'{BASE_URL}/movies')
        return check_response(response)
    except Exception as e:
        print(f'Error: {e}')


def get_movies_by_year(year):
    try:
        response = requests.get(f'{BASE_URL}/movies/{year}')
        return check_response(response)
    except Exception as e:
        print(f'Error: {e}')

def add_movies_by_year(year):
    try:
        response = requests.post(f'{BASE_URL}/movies/{year}')
        return check_response(response)
    except Exception as e:
        print(f'Error: {e}')


def update_movies_by_year(year):
    try:
        response = requests.put(f'{BASE_URL}/movies/{year}')
        return check_response(response)
    except Exception as e:
        print(f'Error: {e}')


def delete_movie_by_year_and_name(year, name):
    try:
        response = requests.delete(f'{BASE_URL}/movies/{year}/{name}')
        return check_response(response)
    except Exception as e:
        print(f'Error: {e}')


def main():
    # api_run(HOST, PORT)  # Has to have its own thread?

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
                if len(option) > 1:
                    print('Too many parameters.')
                else:
                    print(get_all_movies())

            elif option[0] == '2':
                if len(option) == 2:
                    print(get_movies_by_year(option[1]))
                elif len(option) > 2:
                    print('Too many parameters.')
                else:
                    print('No year specified.')

            elif option[0] == '3':
                if len(option) == 2:
                    print(add_movies_by_year(option[1]))
                elif len(option) > 2:
                    print('Too many parameters.')
                else:
                    print('No year specified.')

            elif option[0] == '4':
                if len(option) == 2:
                    print(update_movies_by_year(option[1]))
                elif len(option) > 2:
                    print('Too many parameters.')
                else:
                    print('No year specified.')

            elif option[0] == '5':
                if len(option) == 3:
                    print(delete_movie_by_year_and_name(option[1], option[2]))
                else:
                    print('No year and/or name specified.')

            elif option[0] == '0':
                print('Exiting.')
                break

            else:
                print('Unknown option.')


if __name__ == "__main__":
    main()
