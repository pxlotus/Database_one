import os
import psycopg2.extensions


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def begin():
    clear_screen()
    print("""
    OLD LIFE WILDLIFE CENTER!!!
        YOUR WELCOME
    """)
    input("press Enter/return to start£")
    clear_screen()


begin()


def quick_search():
    animal = input("keyWord search:.").lower()


class DatabaseConnection:
    def __init__(self):
        self.flash_db = psycopg2.connect(database='wildlife', user='postgres', password='P@$$w0rd', host='localhost')
        self.cur = self.flash_db.cursor()
        print("Database connected")

    def query_table(self):
        self.cur = self.flash_db.cursor()
        self.cur.execute('SELECT '
                         'ID,NAME,LIVES,WEIGHT,LEGS,CLASS,NUMBER,CATEGORY '
                         'FROM CAGE')

        rows = self.cur.fetchall()
        for row in rows:
            print([row[0], row[1], row[2], row[4], row[5], row[6], row[7]])


quick_search()


if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.query_table()

clear_screen()