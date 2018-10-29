import os
import psycopg2
from logging import exception

find = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def begin():
    clear_screen()
    print("""
    OLD LIFE WILDLIFE CENTER!!!
        YOUR WELCOME
    """)
    input("press return to start!!")
    clear_screen()


class DatabaseConnection:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database='wildlife', user='postgres', password='P@$$w0rd', host='localhost')
            self.cursor = self.conn.cursor()
            print("opened database successfully")
        except exception(bool=False):
            print("database failure")

    def query_table(self):
        self.cursor.execute('SELECT ID,NAME,LIVES,WEIGHT,LEGS FROM CAGE')
        rows = self.cursor.fetchall()

        # have a user call input to give out result
    def quick_search(self):
        self.cursor.find = input("show me a ...").upper()
        rows = self.cursor.fetchall

        for row in rows:
            if find == rows:
                print(row)
                row = self.cursor.fetchall()
                break


begin()

if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.query_table()
    database_connection.quick_search()

begin()
clear_screen()