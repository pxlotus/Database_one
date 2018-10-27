from logging import exception
import psycopg2

try:
    conn = psycopg2.connect(database='wildlife', user='postgres', password='P@$$w0rd', host='localhost')
    print("opened database successfully")
except exception:
    print('database failure')

cur = conn.cursor()
cur.execute('SELECT ID,NAME,LIVES,WEIGHT,LEGS,CLASS,NUMBER,CATEGORY FROM CAGE')

rows = cur.fetchone()
while True:
    for row in rows:
        print(row)
        row = cur.fetchone()


conn.commit()
conn.close()