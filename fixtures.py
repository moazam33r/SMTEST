from faker import Faker
import random

fake = Faker("sv_SE")

def fake_customer():
    return {
        "email": fake.email(),
        "personnummer": fake.ssn(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "street": fake.street_address(),
        "postcode": fake.postcode(),
        "city": fake.city()
    }