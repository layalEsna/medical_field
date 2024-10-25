# lib/helpers.py

from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import Symptom
from lib.utils import exit_program  
from lib.seed import seed_database

def helper_1():
    print("Performing useful function #1.")


def list_patients():
    '''List all patients.'''
    patients = Patient.get_all()
    if patients:
        for patient in patients:
            print(patient)
    else:
        print('No patients found.')


def list_diseases():
    '''List all diseases.'''
    diseases = Disease.get_all()
    if diseases:
        for disease in diseases:
            print(disease)
    else:
        print('No diseases found.')


def list_symptoms():
    '''List all symptoms.'''
    symptoms = Symptom.get_all()
    if symptoms:
        for symptom in symptoms:
            print(symptom)
    else:
        print('No symptoms found.')


def add_new_patient():
    try:
        name = input("Enter the patient's name: ")
        last_name = input("Enter the patient's last name: ")
        
        age_input = input(f"Enter the patient's age: ")
        age = int(age_input)  # Ensure this is being converted to an integer properly
        
        new_patient = Patient.create(name, last_name, age)
        
        print(f'Success: {new_patient} has been added.')
    except Exception as e:
        print(f'Error: {e}')

                
def update_patient_by_id():
    id_ = input("Enter patient's ID: ")
    if id_:
        patient = Patient.find_by_id(id_)
        if patient:
            name = input("Enter patient's name: ")
            last_name = input("Enter patient's last name: ")
            age = input("Enter patient's age: ")
            try:
                patient.name = name
                patient.last_name = last_name
                patient.age = int(age)
                patient.update()
                print(f'Success: {patient.name} {patient.last_name} with ID: {patient.id}, Age: {patient.age}')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Patient not found.')
    else:
        print('No ID provided.')


def update_patient_by_last_name():
    last_name = input("Enter patient's last name: ")
    patient = Patient.find_by_last_name(last_name)
    if patient:
        name = input("Update patient's name: ")
        last_name = input("Update patient's last name: ")
        age = input("Update patient's age: ")
        try:
            patient.name = name
            patient.last_name = last_name
            patient.age = int(age)
            patient.update()
            print(f'Success: {patient.name} {patient.last_name} with ID: {patient.id}, Age: {patient.age} updated.')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('No last name provided.')


