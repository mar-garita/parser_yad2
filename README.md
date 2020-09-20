# parser_yad2

parser_yad2 парсит квартиры в аренду в Тель-Авиве по заданным параметрам на Израильском сайте объявлений https://www.yad2.co.il/ и записывает в базу данных. 

## Установка

Создайте клон репозитория:

```
git clone https://github.com/mar-garita/parser_yad2
```

Установите зависимости:

```
pip install -r requirments.txt
```

## Настройка 

В фйле settings.py указаны параметры поиска квартиры, которые вы можете изменить:

```
ROOMS = 3     - указывает максимальное количество комнат (от 1 до 3)
PRICE = 4000  - указывает максимальный ценовой диапазон (от 0 до 4000 шекелей)
FLOOR = 2     - указывает минимальный этаж (от 2 и выше)
DB_NAME       - имя базы данных
```

## Запуск

Запустите парсер в консоле:

```
python main.py
```

## Информация

При многократном запуске парсера сайт https://www.yad2.co.il/ выдаёт капчу и блокирует ваш IP на несколько часов. 








