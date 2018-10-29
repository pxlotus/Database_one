from logging import exception
import psycopg2

# must be able to call up a name
# function to be able show only list of entries available.

available = []


def connection():
    try:
        conn = psycopg2.connect(database='wildlife', user='postgres', password='P@$$w0rd',host='localhost')
        print("database connected!")
    except exception(bool=False):
        print("connection Failure!!")

conn.cursor()

# function for input
connection()

def data_of_entry():
    animal = input("your search..."). upper()

