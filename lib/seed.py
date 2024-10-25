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


    disease_1 = Disease.create("Flu", ["Cough", "Fever", "Fatigue"])
    disease_2 = Disease.create("Diabetes", ["Increased thirst", "Frequent urination", "Hunger"])
    disease_3 = Disease.create("COVID-19", ["Fever", "Cough", "Loss of smell"])

    Symptom.create("Fever", patient_id=patient_1.id, disease_id=disease_2.id)
    Symptom.create("Cough", patient_id=patient_2.id, disease_id=disease_3.id)
    Symptom.create("Fatigue", patient_id=patient_3.id, disease_id=disease_3.id)
    Symptom.create("Increased thirst", patient_id=patient_2.id, disease_id=disease_2.id)
    Symptom.create("Frequent urination", patient_id=patient_3.id, disease_id=disease_1.id)
    Symptom.create("Loss of smell", patient_id=patient_1.id, disease_id=disease_1.id)




