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
    
    @classmethod
    def create_table(cls):
        from lib.cli import CURSOR, CONN 
        '''Create the symptoms table in the database.'''
        sql = '''
            CREATE TABLE IF NOT EXISTS symptoms(
            id INTEGER PRIMARY KEY, description TEXT,
            patient_id INTEGER,
            disease_id INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patients(id),
            FOREIGN KEY (disease_id) REFERENCES diseases(id)
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()
    






    @classmethod
    def drop_table(cls):
        from lib.cli import CURSOR, CONN
        '''Drop the symptoms table from the database.'''
        sql = '''
            DROP TABLE IF EXISTS symptoms
        '''
        CURSOR.execute(sql)
        CONN.commit()



    def save(self):
        from lib.cli import CURSOR, CONN 
        '''Insert the Symptom instance into the database and save the ID.'''
        sql = '''
            INSERT INTO symptoms(description, patient_id, disease_id) 
            VALUES(?,?,?)  
        '''
        CURSOR.execute(sql, (self.description, self.patient_id, self.disease_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

