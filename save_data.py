import sqlalchemy
import os

from datetime import datetime


DB_NAME = 'flats_db.db'


def create_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    engine = sqlalchemy.create_engine('sqlite:///' + DB_NAME)
    engine.execute("""
         create table flats (
         id integer primary key,
         adress varchar,
         rooms float,
         floor integer,
         area integer,
         price integer,
         date_added varchar
         )
    """)


class Pipeline:
    """
    Класс принимает данные (data)
    """

    def __init__(self, data):
        self.data = data
        self.engine = sqlalchemy.create_engine('sqlite:///' + DB_NAME)

    def prepares_data(self, row):
        """
        Ф-ция (зачищает данные) подготавливает данные
        :return:
        """
        prepare_data = {}

        for key, value in row.items():
            value = value.strip()

            if key == 'adress':
                value = value.replace("'", '').split()
                value = ' '.join(value)

            elif key == 'rooms_floor_area':
                value = value.split(' ')

                prepare_data['rooms'] = float(value[0])
                prepare_data['floor'] = int(value[1][5:])
                prepare_data['area'] = int(value[2][4:])

            elif key == 'price' and value.isdigit():
                pass

            elif key == 'date_added' and '/' in value:
                value = datetime.strptime(value, '%d/%m/%Y').date()

            prepare_data[key] = value

        del prepare_data['rooms_floor_area']

        print(prepare_data)
        return prepare_data

    def save_data(self):
        for data in self.data:
            data = self.prepares_data(data)

            sql = """ insert into flats (adress,
                                        rooms,
                                        floor,
                                        area,
                                        price,
                                        date_added)
                                    values (
                                    '{adress}',
                                    {rooms},
                                    {floor},
                                    {area},
                                    '{price}',
                                    '{date_added}')
            """.format(adress=data.get('adress'),
                       rooms=data.get('rooms'),
                       floor=data.get('floor'),
                       area=data.get('area'),
                       price=data.get('price'),
                       date_added=data.get('date_added'))

            self.engine.execute(sql)