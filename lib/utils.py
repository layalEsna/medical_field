# def exit_program():
#     print('Exiting program...')

# # lib/utils.py
# import sys
# from lib.db import CONN
# def exit_program():
#     # from lib.cli import CONN 
#     """Closes the database connection and exits the program."""
#     try:
#         CONN.close()
#         print("Connection closed. Exiting program.")
#     except Exception as e:
#         print(f"Error while closing the connection: {e}")
#     finally:
#       sys.exit()  

# lib/utils.py
# import sys
# from lib.db import CONN

# def exit_program():
#     """Closes the database connection and exits the program."""
#     try:
#         CONN.close()
#         print("Connection closed. Exiting program.")
#     except Exception as e:
#         print(f"Error while closing the connection: {e}")
#     finally:
#         sys.exit()  # Ensure the program terminates
# utils.py
import sys

def exit_program():
    print("Exiting program...")
    sys.exit()

# while True:
#     choice = input("Enter 0 to exit: ")
#     if choice == "0":
#         exit_program()