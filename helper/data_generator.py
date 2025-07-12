from faker import Faker
fake = Faker(locale="ru_RU")

class DataGenerator:
    @staticmethod
    def name_generator():
        name = fake.first_name()
        return name

    @staticmethod
    def email_generator():
        email = fake.email()
        return email

    @staticmethod
    def password_generator():
        password = fake.password()
        return password




