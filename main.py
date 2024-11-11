import requests


def main():
    cities = ['London', 'SVO', 'Череповец']
    url_template = 'https://wttr.in/{}?M&Tqn&lang=ru'

    for city in cities:
        url = url_template.format(city)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    main()

