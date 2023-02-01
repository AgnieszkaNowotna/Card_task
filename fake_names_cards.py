from faker import Faker

fake = Faker()

class BaseContact():
    def __init__(self, name, surname, telephone_number, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.telephone_number = telephone_number

    def __str__(self):
        return f'{self.name} {self.surname}, numer telefonu: {self.telephone_number}, email: {self.email}'

    def contact(self):
        print(f'Wybieram numer {self.telephone_number} i dzwonię do {self.name} {self.surname}')

    @property
    def label_lenght(self):
        all_signs = len(self.name) + len(self.surname) + 1
        self._number_of_signs = all_signs
        return self._number_of_signs

class BusinessContact(BaseContact):
    def __init__(self, business_number,job, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_number = business_number
        self.job = job
        self.company = company

    def __str__(self):
        return (f'{self.name} {self.surname}, {self.job}, {self.company}, numer telefonu : {self.telephone_number}, telefon służbowy :{self.business_number}, email: {self.email}')

    def contact(self):
        print(f'Wybieram numer {self.business_number} i dzwonię do {self.name} {self.surname}')

def create_contact(type, amount):
    for i in range (amount):
        name_surname = (fake.name()).split(" ")
        name1 = name_surname[0]
        surname1 = name_surname [-1]
        if type == "base":
            person = BaseContact(name = name1,
                                 surname = surname1,
                                 telephone_number = fake.phone_number(),
                                 email =fake.email())
            print(person)
            person.contact()
            print(person.label_lenght)
        elif type == "business":
            person = BusinessContact(name = name1,
                                     surname = surname1,
                                     job = fake.job(),
                                     company = fake.company(),
                                     telephone_number = fake.phone_number(),
                                     business_number = fake.phone_number(),
                                     email = fake.email())
            print(person)
            person.contact()
            print(person.label_lenght)
        else:
            print("Wprowadzono błędny rodzaj wizytówki")

create_contact("base",10)