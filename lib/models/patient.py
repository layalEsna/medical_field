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
        return f'Patient {self.id}: {self.name} {self.last_name},age: {self.age}'
        

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
        
        
    @classmethod
    def create_table(cls):
        from lib.cli import CURSOR, CONN 
        sql = '''
          CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            age INTEGER
            )
    '''
        CURSOR.execute(sql)
        CONN.commit()

    
    @classmethod
    def drop_table(cls):
        from lib.cli import CONN, CURSOR  
        '''Drop the diseases table from the database.'''
        sql = '''
            DROP TABLE IF EXISTS patients
        '''
        CURSOR.execute(sql)
        CONN.commit()

    # def save(self):
    #     from lib.cli import CURSOR, CONN 
    #     '''Insert the Patient instance into the database and save the ID.'''
    #     sql = '''
    #         INSERT INTO patients(name, last_name, age)
    #         VALUES(?,?,?)
    #     '''
    #     CURSOR.execute(sql, (self.name, self.last_name, self.age))
    #     CONN.commit()
    #     self.id = CURSOR.lastrowid
    #     type(self).all[self.id] = self

    def save(self):
        from lib.cli import CURSOR, CONN 
        '''Insert the Patient instance into the database and save the ID.'''
        sql = '''
        INSERT INTO patients(name, last_name, age)
        VALUES(?,?,?)
        '''
        try:
          CURSOR.execute(sql, (self.name, self.last_name, self.age))
          CONN.commit()
          self.id = CURSOR.lastrowid  # Set the ID of the instance
          type(self).all[self.id] = self  # Store instance in the class-level dictionary
        except Exception as e:
          print(f"Error saving patient: {e}")


    @classmethod
    def create(cls, name, last_name, age):
        '''Create and save a new Patient instance.'''
        # patient = cls(name, last_name, age)
        patient = cls(name=name, last_name=last_name, age=age)
        patient.save()
        return patient
    

    def update(self):
        from lib.cli import CURSOR, CONN 
        '''Update an existing Patient record in the database.'''
        sql = '''
            UPDATE patients
            SET name = ?, last_name = ?, age = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.name, self.last_name, self.age, self.id))
        CONN.commit()

    
    def delete(self):
        from lib.cli import CURSOR, CONN 
        '''Delete the Patient record from the database.'''
        sql = '''
            DELETE FROM patients
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        '''Return a Patient instance based on a database row.'''
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.last_name = row[2]
            patient.age = row[3]
        else:
            patient = cls(row[1], row[2], row[3])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod
    def get_all(cls):
        from lib.cli import CURSOR, CONN 
        '''Return a list of all Patient instances from the database.'''
        patients = []
        sql = '''
            SELECT *
            FROM patients
        '''
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            patient = cls.instance_from_db(row)
            patients.append(patient)
        return patients
    
    @classmethod
    def find_by_id(cls, id):
        from lib.cli import CURSOR, CONN 
        '''Find and return a Patient instance by ID from the patients table.'''
        sql = '''
            SELECT *
            FROM patients
            WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_last_name(cls, last_name):
        from lib.cli import CURSOR, CONN 
        '''Find and return a Patient instance by last name from the patients table.'''
        sql = '''
            SELECT *
            FROM patients
            WHERE last_name = ?
        '''
        row = CURSOR.execute(sql, (last_name,)).fetchone()
        return cls.instance_from_db(row) if row else None



    def get_patient_symptoms(self):
        from lib.cli import CURSOR, CONN 
        '''Retrieve a list of all symptoms associated with this patient.'''
        symptoms_list = []
        sql = '''
            SELECT *
            FROM symptoms
            WHERE patient_id = ?
        '''
        from lib.models.symptom import Symptom  # Moved import statement inside the function
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        for row in rows:
            symptom = Symptom.instance_from_db(row)
            symptoms_list.append(symptom)
        return symptoms_list if symptoms_list else []





