from datetime import datetime


def send_sms(msg, phone):
    """Sends a given message to a given phone via SMS.

    You don't have to implement this function.
    """
    ...


def send_email(msg, email):
    """Sends a given message to a given address as email.

    You don't have to implement this function.
    """
    ...

# Solution goes here

class Patient:
    def __init__(self,name,family_name,sex,birthday,email,tel,tel2) :
        self.name = name
        self.family_name = family_name
        self.sex = sex
        self.birthday = birthday
        self.email = email
        self.tel = tel
        self.tel2 = tel2
    
    def greeting(self):
        return f'Hello {self.sex} {self.name} {self.family_name} '
        

    def send_appointment_reminder(self,app_time):
        age = app_time.year - self.birthday.year 
        print('age: '+str(age)+" years")
        send_email(self.tel,self.email)
        send_sms(self.tel,self.tel2)

patient1 = Patient(
    'John',
    'Doe',
    'mr.',
    datetime(1990, 2, 28),
    'john.doe@gmail.com',
    '+3345451555',
    '+6693932030',
)

print(patient1.greeting())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
