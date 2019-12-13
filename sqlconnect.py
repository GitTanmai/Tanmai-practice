import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=admin")
cur = conn.cursor()
with open('C:\\Users\\tmehrotra\\stock_data06122019.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO COMPANY VALUES (%s, %s, %s, %s,%s,%s )",
        row
        )
        conn.commit()