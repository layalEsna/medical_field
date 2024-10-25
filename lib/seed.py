from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import Symptom


def seed_database():
    Patient.drop_table()
    Disease.drop_table()
    Symptom.drop_table()
    

    Patient.create_table()
    Disease.create_table()
    Symptom.create_table()

    patient_1 = Patient.create("John", "Doe", 45)
    patient_2 = Patient.create("Jane", "Smith", 32)
    patient_3 = Patient.create("Emily", "Johnson", 28)


