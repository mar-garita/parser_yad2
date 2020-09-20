# parser_yad2

parser_yad2 parses apartments for rent in Tel-Aviv according to the specified parameters on the Israeli ad site https://www.yad2.co.il/ and writes to the database.

## Installation

Create a clone of the repository:

```
git clone https://github.com/mar-garita/parser_yad2
```

Install dependencies:

```
pip install -r requirments.txt
```

## Setting

In file settings.py the apartment search parameters are specified, which you can change:

```
ROOMS = 3     - specifies the maximum number of rooms (from 1 to 3)
PRICE = 4000  - specifies the maximum price range (from 0 to 4000 shekels)
FLOOR = 2     - specifies the minimum floor (from 2 and higher)
DB_NAME       - database name
```

## Program start

Run the parser in the console:

```
python main.py
```

## Информация

При многократном запуске парсера сайт https://www.yad2.co.il/ выдаёт капчу и блокирует ваш IP на несколько часов. 




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

## Настройка параметров

В файле settings.py указаны параметры поиска квартиры, которые вы можете изменить:

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









