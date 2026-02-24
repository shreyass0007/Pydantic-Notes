from pydantic import BaseModel, EmailStr , AnyUrl , Field
from typing import List , Dict, Optional

class Patient(BaseModel):
    name:str=Field(max_length=50)
    age:int
    email:EmailStr='abc@gmail.com'
    linkedin_url:Optional[AnyUrl]=None
    weight:float=Field(gt=0)
    married:bool
    allergies:Optional[list[str]]=None
    contact_info:dict[str,str] 

def insert_patient_data(patient:Patient):
    if type(patient.name)==str and type(patient.age)==int:
        print(patient.name)
        print(patient.age)
        print(patient.email)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_info)
        print('inserted into database')
    else:
        raise TypeError('Invalid data types')

def updated_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)
    print('Updated patient data in database')

patient_info={'name':'shreyas','age':35,'email':'shreyas@example.com','linkedin_url':'https://www.linkedin.com/in/shreyas','weight':70.5, 'married':True, 'contact_info':{'phone':'1234567890','email':'shreyas@example.com'}}  

patient1=Patient(**patient_info)
# insert_patient_data(patient1)
updated_patient_data(patient1)