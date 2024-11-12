import requests


def main():
    url_template = 'https://wttr.in/{}'

    # Список городов для получения погоды
    cities = ['Лондон', 'SVO', 'Череповец']

    # Параметры запроса
    params = {
        'M': '', # показывать скорость ветра в м/с
        'n': '', # узкая версия (только день и ночь)
        'q': '', # тихая версия (без текста "Прогноз погоды")
        'T': '', # отключить терминальные последовательности (без цветов)
        'lang': 'ru' # язык на котором выводится информация
    }

    # Цикл по каждому городу
    for city in cities:
        url = url_template.format(city) # Формируем URL
        response = requests.get(url, params=params) # Выполняем запрос

        # Проверяем ответ от сайта
        response.raise_for_status()
        print(response.text)

if __name__ == '__main__':
    main()
