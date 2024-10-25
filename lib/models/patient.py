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
            DROP TABLE IF EXISTS diseases
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        from lib.cli import CURSOR, CONN 
        '''Insert the Patient instance into the database and save the ID.'''
        sql = '''
            INSERT INTO patients(name, last_name, age)
            VALUES(?,?,?)
        '''
        CURSOR.execute(sql, (self.name, self.last_name, self.age))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, last_name, age):
        '''Create and save a new Patient instance.'''
        patient = cls(name, last_name, age)
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





