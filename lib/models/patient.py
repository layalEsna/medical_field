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
        
        # Property for last name with validation
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name):
            self._last_name = last_name
        else:
            raise ValueError('Lastname must be a non-empty string.')
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
       
        if isinstance(age, int) and 18 <= age <= 100:
            self._age = age
        else:
            raise ValueError('Age must be an integer between 18 and 100 inclusive.')



