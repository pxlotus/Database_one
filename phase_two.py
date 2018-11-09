import psycopg2.extensions
import logging


class DatabaseConnection:
    logging.info('connecting to Database...')
    # initialising the connection to self

    def __init__(self, flash, conn, rows):
        self.flash = flash
        self.conn = conn
        self.rows = rows

# function set to connect the code to the database
        try:
            self.flash = psycopg2.connect(database='wildlife', user='postgres', password='P@$$w0rd', port='5432', host='localhost')
            self.conn = self.flash.cursor()
            print("Database Connected")

        except ValueError:
            print("Database No connection")


# this function requests the table i database to release the info/records
    def query_table(self):
        self.conn.execute("SELECT ID,NAME,LIVES,WEIGHT,LEGS,CLASS,NUMBER,CATEGORY FROM CAGE")
        rows = self.conn.fetchall()

    def quick_search(self):
        self.rows = self.conn.fetchall()
        while True:
            for row in self.rows:
                row = self.conn.fetchall()
                print(row)
                break


if __name__ == '__main__':
    database_connection = DatabaseConnection(flash='wildlife', conn='first_phase',rows=[2])
    database_connection.query_table()
    database_connection.quick_search()
