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
        
        # Property for name with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('Name must be a non-empty string.')

