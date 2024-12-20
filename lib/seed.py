
# lib/seed.py
# from lib.db import CONN, CURSOR  
from lib.models.patient import Patient
from lib.models.disease import Disease
from lib.models.symptom import SymptomEntry

def seed_database():
    # from lib.cli import CONN
    
        """Seeds the database with initial data and creates necessary tables."""
    # with CONN:
        # Drop existing tables
        Patient.drop_table()
        Disease.drop_table()
        SymptomEntry.drop_table()
        
        # Create tables
        Patient.create_table()
        Disease.create_table()
        SymptomEntry.create_table()

        # Create patients
        patient_1 = Patient.create("John", "Doe", 45)
        patient_2 = Patient.create("Jane", "Smith", 32)
        patient_3 = Patient.create("Emily", "Johnson", 28)

        # Create diseases
        disease_1 = Disease.create("Flu", ["Cough", "Fever", "Fatigue"])
        disease_2 = Disease.create("Diabetes", ["Increased thirst", "Frequent urination", "Hunger"])
        disease_3 = Disease.create("COVID-19", ["Fever", "Cough", "Loss of smell"])

        # Create symptoms linked to patients and diseases
        SymptomEntry.create("Fever", patient_id=patient_1.id, disease_id=disease_2.id)
        SymptomEntry.create("Cough", patient_id=patient_2.id, disease_id=disease_3.id)
        SymptomEntry.create("Fatigue", patient_id=patient_3.id, disease_id=disease_3.id)
        SymptomEntry.create("Increased thirst", patient_id=patient_2.id, disease_id=disease_2.id)
        SymptomEntry.create("Frequent urination", patient_id=patient_3.id, disease_id=disease_1.id)
        SymptomEntry.create("Loss of smell", patient_id=patient_1.id, disease_id=disease_1.id)

if __name__ == "__main__":
    seed_database()
    print("Seeded database")







