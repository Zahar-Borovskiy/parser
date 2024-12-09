import requests
from bs4 import BeautifulSoup as BS

def weather_parser(city):
    urls = {
        'Санкт-Петербург': 'https://rp5.ru/Погода_в_Санкт-Петербурге',
        'Буэнос-Айрес': 'https://rp5.ru/Погода_в_Буэнос-Айресе'
    }

    if city not in urls:
        print(f'Город {city} не поддерживается.')
        return

    url = urls[city]
    class_ = 'ArchiveTemp'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')

    try:
        t = html.find(class_=class_).find(class_='t_0').text
        print(f'Погода в {city}: {t}')
    except AttributeError:
        print(f'Не удалось получить данные о погоде для {city}.')

# Примеры вызова функции
weather_parser('Санкт-Петербург')
weather_parser('Буэнос-Айрес')
weather_parser('Москва')