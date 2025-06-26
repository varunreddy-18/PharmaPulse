# db.py
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Varun@9154',
    'database': 'med_agency'
}

def get_connection():
    return mysql.connector.connect(**db_config)
