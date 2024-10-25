
# lib/cli.py
import sqlite3
from lib.db import CONN, CURSOR
from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import Symptom
from lib.seed import seed_database

from lib.helpers import(
    exit_program,
   
    # helper_1,
)

def main():
    try:
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                seed_database()
            else:
                print("Invalid choice")
    finally:
        CURSOR.close()
        CONN.close()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Seed the database")


if __name__ == "__main__":
    main()

