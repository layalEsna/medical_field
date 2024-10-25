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
