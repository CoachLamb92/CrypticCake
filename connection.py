from pg8000.native import Connection
from dotenv import load_dotenv
import os


load_dotenv()

def create_conn():
    db = Connection(os.environ['PGUSER'],
                    password=os.environ['PGPASSWORD'],
                    database=os.environ['PGDATABASE'])
    return db

def close_db(db):
    db.close()

db = create_conn()
close_db(db)