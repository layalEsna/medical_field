# lib/models/symptom.py
class Symptom:
    all = {}

    def __init__(self, description, patient_id = None, disease_id = None, id=None):
        self.id = id
        self.description = description
        self.patient_id = patient_id
        self.disease_id = disease_id

    def __repr__(self):
        return (
            f'<Symptom {self.id}: {self.description}, ' +
            f'Patient ID: {self.patient_id}, Disease ID: {self.disease_id}>'
        )

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and 3 <= len(description) <= 50:
            self._description = description
        else:
            raise ValueError('Description must be string between 3 and 50 characters inclusive.')
    