import datetime
import logging
import random
from faker import Faker
from database import Database as db

class Generate:
    # Устанавливаем Faker для генерации имен
    fake = Faker()

    # Функция для генерации случайного telegram_id (64-битное число)
    @classmethod
    def generate_value(cls):
        return random.randint(40, 100)


    # Функция для генерации случайного telegram_name
    @classmethod
    def generate_time(cls):
        return datetime.datetime.fromtimestamp(random.uniform(datetime.datetime(year=2025, month=4, day=1, hour=0, minute=0, second=0, microsecond=0).timestamp(), datetime.datetime(year=2025, month=5, day=1, hour=0, minute=0, second=0, microsecond=0).timestamp()))

    # Функция для генерации privileges
    @classmethod
    def generate_type(cls):
        privileges_list = ['humidity', 'light', 'temperature']
        return random.choice(privileges_list)


    @classmethod
    def generate_data(cls, num_records):
        connection = db.connect()
        for _ in range(num_records):
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO sensors (type, time, value) VALUES (%s, %s, %s)", (cls.generate_type(), cls.generate_time(), cls.generate_value()))
        connection.commit()
        connection.close()


if __name__ == "__main__":
    gen = Generate()
    gen.generate_data(100)
    logging.info("Generated data")