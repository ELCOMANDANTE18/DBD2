from faker import Faker
from pymongo import MongoClient
import random

fake = Faker()

# Generar 10 registros de datos de usuarios
user_data_list = []
for _ in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    # Generar un número de teléfono aleatorio de 10 dígitos
    phone_number = f"{random.randint(1000000000, 9999999999):010d}"
    address = fake.address()
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')  # Convierte la fecha a cadena

    user_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
        "Phone Number": phone_number,
        "Address": address,
        "Birthdate": birthdate
    }
    user_data_list.append(user_data)

# Conexión a la base de datos MongoDB
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "users"  # Cambia el nombre de la colección a "users"

client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Insertar datos de usuarios en la colección
insert_results = collection.insert_many(user_data_list)

if insert_results.acknowledged:
    for inserted_id in insert_results.inserted_ids:
        print(f"Documento insertado con el ID: {inserted_id}")
else:
    print("Fallo al insertar documentos de usuario.")
