import requests
from api import api_run


def main():
    print('lets get it going on: host = \"127.0.0.100\", port = 8000')
    api_run("127.0.0.100", 8000)
    print('did we get it going?')


if __name__ == "__main__":
    main()
