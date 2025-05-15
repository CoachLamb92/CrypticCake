from connection import create_conn, close_db
from pprint import pprint
db = create_conn()

query = "SELECT * FROM clues LIMIT 10;"
pprint(db.run(query))

close_db(db)
