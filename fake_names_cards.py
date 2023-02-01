from faker import Faker

fake = Faker()

class Card:
    def __init__(self,name,surname,company,job,email):
        self.name = name
        self.surname = surname
        self.company = company
        self.job = job
        self.email = email
        self._number_of_signs = 0

    def __repr__(self):
        return (f"""Showcase(name = {self.name} surname = {self.surname},company = {self.company} job = {self.job} email = {self.email}""")

    def __str__(self):
        return f'{self.name} {self.surname},{self.email}'

    def contact (self):
        print(f'Kontaktuję się z {self.name} {self.surname}, {self.job}, {self.email}')

    @property
    def label_lenght(self):
        all_signs = len(self.name) + len(self.surname) + 1
        self._number_of_signs = all_signs
        return self._number_of_signs

class BaseContact(Card):
    def __init__(self, name, surname, telephone_number, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.telephone_number = telephone_number

    def __str__(self):
        return f'{self.name} {self.surname}, numer telefonu: {self.telephone_number}, email: {self.email}'

    def contact(self):
        print(f'Wybieram numer {self.telephone_number} i dzwonię do {self.name} {self.surname}')

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

list_of_showcases = []

for i in range (5):
    name_surname = (fake.name()).split(" ")
    name1 = name_surname[0]
    surname1 = name_surname [-1]
    person = Card(name = name1,
                      surname = surname1,
                      company = fake.company(), 
                      job = fake.job(),
                      email = fake.email())
    print(person)
    person.contact()
    list_of_showcases.append(person)

by_name = sorted(list_of_showcases, key = lambda person: person.name)
by_surname = sorted(list_of_showcases, key = lambda person: person.surname)
by_email = sorted(list_of_showcases, key = lambda person: person.email)

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

create_contact("business",6)