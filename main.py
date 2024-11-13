import requests


def main():
    url_template = 'https://wttr.in/{}'
    cities = ['Лондон', 'SVO', 'Череповец']

    params = {
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }

    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=params)

        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
