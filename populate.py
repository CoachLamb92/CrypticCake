from pg8000.native import literal
from connection import create_conn, close_db
import csv

db = create_conn()

db.run("DROP TABLE IF EXISTS clues;")
db.run("""CREATE TABLE clues (
                  clue_id SERIAL PRIMARY KEY,
                  clue VARCHAR(120) NOT NULL,
                  answer VARCHAR(30) NOT NULL,
                  definition VARCHAR(100) NOT NULL,
                  clue_number VARCHAR(15) NOT NULL
    );""")

with open("reduced_clues.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    start_of_query = """INSERT INTO clues (clue, answer, definition, clue_number) VALUES """
    fields = next(csvreader)

    for row in csvreader:
        values = '(' + ', '.join([literal(row[0]), literal(row[1]), literal(row[2]), literal(row[3])]) + ')'
        query = start_of_query + values
        db.run(query)

close_db(db)
