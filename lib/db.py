import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONN = sqlite3.connect(os.path.join(BASE_DIR, 'medical_records.db'))
CURSOR = CONN.cursor()
