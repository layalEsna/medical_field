# lib/helpers.py

from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import SymptomEntry
 
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
    symptoms = SymptomEntry.get_all()
    if symptoms:
        for symptom in symptoms:
            print(symptom)
    else:
        print('No symptoms found.')


# def add_new_patient():
#     # print("add_new_patient called", flush=True)
#     try:
#         name = input("Enter the patient's name: ")
#         last_name = input("Enter the patient's last name: ")
        
#         age_input = input("Enter the patient's age: ")
#         age = int(age_input)  
#         new_patient = Patient.create(name, last_name, age)
#         # new_patient.save()
#         print(f'Success: {new_patient} has been added.')
#     except Exception as e:
#         print(f'Error: {e}')


def add_new_patient():
    try:
        name = input("Enter the patient's name: ")
        last_name = input("Enter the patient's last name: ")
        
        age_input = input("Enter the patient's age: ")
        age = int(age_input)  
        new_patient = Patient.create(name, last_name, age)  # Create new patient
        print(f'<<<Success: {new_patient} has been added.>>>')  # Will call __repr__ of Patient
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
                print(f'<<<Success: {patient.name} {patient.last_name} with ID: {patient.id}, Age: {patient.age} updated.>>>')
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
            print(f'<<<<Success: {patient.name} {patient.last_name} with ID: {patient.id}, Age: {patient.age} updated.>>>>')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('No last name provided.')


def delete_patient_by_id():
    id_ = input("Enter patient's ID: ")
    if id_:
        patient = Patient.find_by_id(id_)
        if patient:
            confirm = input(f'Are you sure you want to delete patient {patient.name} {patient.last_name} with ID {patient.id}? (yes/no): ')
            if confirm.lower() == 'yes':
               
                try:
                    patient.delete()
                    print(f'<<<<Success: Patient with ID {id_} has been deleted.>>>>')
                except Exception as e:
                    print(f'Error: {e}')
            else:
                print('Deletion canceled.')
        else:
            print(f'Patient with ID {id_} not found.')
    else:
        print('No ID provided.')



def find_disease_by_name():
    name = input("Enter disease's name: ")
    disease = Disease.find_by_name(name)
    if disease:
        print(f'Found disease: {disease}')
    else:
        print(f'{name} not found.')

def find_disease_by_id():
    id_ = input("Enter disease's ID: ")
    disease = Disease.find_by_id(id_)
    if disease:
        print(f'Disease by ID {id_} found: {disease}')
    else:
        print(f'Disease by ID {id_} not found.')


def delete_disease_by_id():
    id_ = input("Enter disease's ID: ")
    disease = Disease.find_by_id(id_)
    if disease:
        confirm = input(f'Are you sure you want to delete disease {disease.name} with ID {disease.id}? (yes/no): ')
        if confirm.lower() == 'yes':
            try:
                disease.delete()
                print(f'Success: Disease {disease.name} with ID {id_} deleted.')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Deletion canceled.')
    else:
        print(f'Disease with ID {id_} not found.')


def update_disease_by_id():
    id_ = input("Enter disease's ID: ")
    if id_:
        disease = Disease.find_by_id(id_)
        if disease:
            name = input("Enter disease's name: ")
            symptoms = input("Enter disease's symptoms (comma-separated): ")
            symptom_list = symptoms.split(', ') if symptoms else disease.symptoms
            try:
                disease.name = name
                disease.symptoms = symptom_list
                disease.update()
                print(f'<<<<Success: Disease with ID {id_} updated.>>>>')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print(f'Disease with ID {id_} not found.')
    else:
        print('No ID provided.')


def add_new_disease():
    name = input("Enter disease's name: ")
    symptoms = input("Enter disease's symptoms (comma-seprated): ")
    symptom_list = symptoms.split(', ')
    
    try:
            new_disease = Disease.create(name, symptom_list)
            if new_disease:
                print(f'Success<Disease {new_disease.name} added.>')
            else:
                print(f'Failed to add {name}')
   
    except Exception as e:
             print(f'Error: {e}')


            #  PYTHONPATH=. python lib/cli.py 
            # or  python -m lib.cli



    #     #    
    #         #  python -m lib.seed

             
    #         #  sqlite3 lib/db.sqlite
             
    #         #  sqlite3 lib/medical_records.db
    #         #  .tables
    #         #  .schema tablename
    #         #  .schema patients
    #         #  SELECT * FROM patients;
    #         #  SELECT * FROM diseases;
    #         # SELECT * FROM symptoms;
             



