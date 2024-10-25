# lib/models/disease.py

class Disease:
    all = {}

    def __init__(self, name, symptoms=None, id=None):
        self.id = id
        self.name = name
        self.symptoms = symptoms or []

    def __repr__(self):
        return f'<Disease {self.id}: {self.name}>'

  
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError('Name must be a non-empty string.')

    
    @property
    def symptoms(self):
        return self._symptoms

    @symptoms.setter
    def symptoms(self, symptoms):
        if isinstance(symptoms, list) and len(symptoms) > 0:
            self._symptoms = symptoms
        else:
            raise ValueError('Symptoms must be a non-empty list.')
    
    @classmethod
    def create_table(cls):
        from lib.cli import CONN, CURSOR  
        sql = '''
            CREATE TABLE IF NOT EXISTS diseases(
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            symptoms TEXT
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
        '''Insert the Disease instance into the database and save the ID.'''
        from lib.cli import CONN, CURSOR 
        sql = '''
            INSERT INTO diseases(name, symptoms)
            VALUES(?,?)
        '''
        symptoms_str = ', '.join(self.symptoms)
        CURSOR.execute(sql, (self.name, symptoms_str))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, name, symptoms=None):
        '''Create and save a new Disease instance.'''
        disease = cls(name, symptoms)
        disease.save()
        return disease
    

    def update(self):
        '''Update an existing Disease record in the database.'''
        from lib.cli import CONN, CURSOR 
        symptoms_str = ', '.join(self.symptoms)
        sql = '''
            UPDATE diseases
            SET name = ?, symptoms = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.name, symptoms_str, self.id))
        CONN.commit()

    def delete(self):
        '''Delete the Disease record from the database.'''
        from lib.cli import CONN, CURSOR  
        sql = '''
            DELETE FROM diseases
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    
    @classmethod
    def instance_from_db(cls, row):
        '''Return a Disease instance based on a database row.'''
        disease_id = row[0]
        disease = cls.all.get(disease_id)
        symptom_list = row[2].split(', ') if row[2] else []
        if disease:
            disease.name = row[1]
            disease.symptoms = symptom_list
        else:
            disease = cls(row[1], symptom_list)
            disease.id = disease_id
            cls.all[disease.id] = disease
        return disease
    
    @classmethod
    def get_all(cls):
        '''Return a list of all Disease instances from the database.'''
        from lib.cli import CURSOR  
        diseases = []
        sql = '''
            SELECT *
            FROM diseases
        '''
        rows = CURSOR.execute(sql).fetchall()
        for row in rows:
            disease = cls.instance_from_db(row)
            diseases.append(disease)
        return diseases
    

    @classmethod
    def find_by_id(cls, id):
        '''Find and return a Disease instance by ID from the diseases table.'''
        from lib.cli import CURSOR  
        sql = '''
            SELECT *
            FROM diseases
            WHERE id = ?
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
