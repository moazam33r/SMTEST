from faker import Faker

fake = Faker("sv_SE")

def fake_customer():
    return {
        "email": fake.email(),
        "phone": fake.phone_number(),
        "personnummer": fake.ssn(), 
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "street": fake.street_address(),
        "postcode": fake.postcode(),
    }