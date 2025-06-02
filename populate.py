from pg8000.native import literal
from connection import create_conn, close_db
import csv
import re

db = create_conn()

db.run("DROP TABLE IF EXISTS clues;")
db.run("""CREATE TABLE clues (
                  clue_id SERIAL PRIMARY KEY,
                  clue VARCHAR(120) NOT NULL,
                  clue_length INT,
                  number_of_words INT,
                  answer VARCHAR(30) NOT NULL,
                  definition VARCHAR(100) NOT NULL,
                  clue_number VARCHAR(15) NOT NULL
    );""")

with open("reduced_clues.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    start_of_query = """INSERT INTO clues (clue, clue_length, number_of_words, answer, definition, clue_number) VALUES """
    fields = next(csvreader)

    for row in csvreader:
        # Excludes rows without clue length - not 100% precise
        if "(" not in row[0] or ")" not in row[0]:
            continue

        clue_length_string = re.search("\(\d.*\)", row[0])
        clue_length_cleaned = row[0][clue_length_string.start()+1:clue_length_string.end()-1]
        pure_clue = row[0][:clue_length_string.start()].strip()
        
        cleaned_list = re.split(r"[’,-]", clue_length_cleaned)

        for i in range(len(cleaned_list)):
            cleaned_list[i] = int(cleaned_list[i])

        clue_length = sum(cleaned_list)

        # Excludes rows where (answer length) is not equal to len(given answer)
        if clue_length != len(row[1]):
            if clue_length != len(row[1]) - row[1].count(" "):
                if clue_length != len(row[1]) - row[1].count("-"):    
                    continue
        
        # Excludes rows where definition is not provided
        if row[2] not in pure_clue and "/" not in row[2]:
            continue

        # Excludes double-definition clues
        if "/" in row[2]:
            continue

        values = '(' + ', '.join([literal(pure_clue), str(clue_length), str(len(cleaned_list)), literal(row[1]), literal(row[2]), literal(row[3])]) + ')'
        query = start_of_query + values

        db.run(query)

close_db(db)
