
# lib/cli.py
import sqlite3 

from lib.db import CONN, CURSOR
from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import SymptomEntry
from lib.seed import seed_database
from lib.utils import exit_program


from lib.helpers import (
   
   
    # helper_1,
    list_patients,
    list_diseases,
    list_symptoms,
    add_new_patient,
    update_patient_by_id,
    update_patient_by_last_name,
    delete_patient_by_id,
    find_disease_by_name,
    find_disease_by_id,
    delete_disease_by_id,
    update_disease_by_id,
    add_new_disease,
    
)
# import os

# def exit_program():
#     """Closes the database connection and exits the program."""
#     try:
#         CONN.close()
#         print("Connection closed. Exiting program.")
#     except Exception as e:
#         print(f"Error while closing the connection: {e}")
#     finally:
#         os._exit(0)  # Forceful exit

def main():
    try:
        while True:
            menu()  # Call the menu first to display options
            choice = input("> ")  # Then get user input

            if choice == "0":
                exit_program()  # Exit if user chooses 0
            elif choice == "1":
                try:
                    print("Seeding the database...", flush=True)
                    seed_database()
                    print('Database seeded successfully', flush=True)
                except Exception as e:
                    print(f"An error occurred: {e}")
    
            elif choice == "2":
                list_patients()
            elif choice == "3":
                list_diseases()
            elif choice == "4":
                list_symptoms()
            elif choice == "5":
                add_new_patient()
            elif choice == "6":
                update_patient_by_id()
            elif choice == "7":
                update_patient_by_last_name()
            elif choice == "8":
                delete_patient_by_id()
            elif choice == "9":
                find_disease_by_name()
            elif choice == "10":
                find_disease_by_id()
            elif choice == "11":
                delete_disease_by_id()
            elif choice == "12":
                update_disease_by_id()
            elif choice == "13":
                add_new_disease()
            else:
                print("Invalid choice")
    finally:
      try:
        CURSOR.close()
        CONN.close()
      except Exception as e:
            print(f"Error closing resources: {e}")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Seed the database")
    print("2. List all patients")
    print("3. List all diseases")
    print("4. List all symptoms")
    print("5. Add a new patient")
    print("6. Update patient by ID")
    print("7. Update patient by last name")
    print("8. Delete patient by ID")
    print("9. Find disease by name")
    print("10. Find disease by ID")
    print("11. Delete disease by ID")
    print("12. Update disease by ID")
    print("13. Add a new disease")


if __name__ == "__main__":
    main()
