from connection import create_conn, close_db
db = create_conn()

query = "SELECT clue, definition FROM clues;"
clue_list = db.run(query)

for x in clue_list:
    if x[1] not in x[0]:
        print(x)

close_db(db)
