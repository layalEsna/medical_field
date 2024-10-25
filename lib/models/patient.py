# lib/models/patient.py

class Patient:
    all = {}
    all_patients = []

    def __init__(self, name, last_name, age, id=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        
        self.age = age
        def __repr__(self):
            return f'<Patient {self.id}: {self.name}, {self.last_name}, {self.age}>'
