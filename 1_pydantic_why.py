from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int
    weight:float

def insert_patient_data(patient:Patient):
    if type(patient.name)==str and type(patient.age)==int:
        print(patient.name)
        print(patient.age)
        print('inserted into database')
    else:
        raise TypeError('Invalid data types')


patient_info={'name':'shreyas','age':35}

patient1=Patient(**patient_info)
insert_patient_data(patient1)