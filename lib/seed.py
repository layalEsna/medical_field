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

