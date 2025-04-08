import logging
from os import environ

import mysql.connector
from mysql.connector import Error
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME


class Database:
    @classmethod
    def connect(cls):
        try:
            connection = mysql.connector.connect(
                host=DATABASE_HOST,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD,
                database=DATABASE_NAME
            )
            if connection.is_connected():
                logging.info("Connected to MySQL database")
                return connection
        except Error as e:
            logging.error(f"Error connecting to MySQL database: {e}")
            return None

    @classmethod
    def get_sensors(cls, sensor: str = ""):
        connection = cls.connect()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM sensors")
            info = cursor.fetchall()
            if sensor == "":
                return info
            else:
                return [sen for sen in info if sen[0] == sensor]

