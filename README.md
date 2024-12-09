# Парсер Погоды

Этот проект — простой парсер погоды, который извлекает данные о погоде для определенных городов с использованием веб-скрапинга на Python. Он построен с использованием библиотек `requests` и `BeautifulSoup`.

## Начало работы

Следуйте приведенным ниже инструкциям, чтобы клонировать проект, настроить виртуальное окружение и запустить скрипт.

### Предварительные требования

Убедитесь, что у вас установлена версия Python 3.x на вашем устройстве.

### Клонирование проекта

1. Откройте терминал (или командную строку) и клонируйте репозиторий:
   ```bash
   git clone https://github.com/Zahar-Borovskiy/parser.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd parser
   ```

### Настройка виртуального окружения

Создайте виртуальное окружение (необязательно, но рекомендуется):
```bash
python -m venv venv
```
Активируйте виртуальное окружение:

- На Windows:
   ```bash
   venv\Scripts\activate
   ```
- На macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

### Установка зависимостей

Установите необходимые зависимости, указанные в файле `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Запуск проекта

Вы можете запустить скрипт парсера погоды, выполнив следующую команду:
```bash
python weather_parser.py
```

### Пример вывода

Скрипт выведет информацию о погоде для указанных городов:
```
Погода в Санкт-Петербурге: <температура>
Погода в Буэнос-Айрес: <температура>
```

### Поддерживаемые города

В данный момент парсер поддерживает следующие города:

- Санкт-Петербург
- Буэнос-Айрес

Если вы хотите добавить больше городов, обновите словарь `urls` в файле `weather_parser.py`.
```
