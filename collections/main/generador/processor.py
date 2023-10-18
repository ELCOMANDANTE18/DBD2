from pymongo import MongoClient
from faker import Faker
import random

fake = Faker()

def generate_processor_data():
    manufacturer = random.choice(["Intel", "AMD"])
    model = fake.word()
    architecture = fake.word()
    cores = random.randint(2, 16)
    frequency_ghz = round(random.uniform(1.6, 5.0), 2)
    price = random.randint(50, 500)

    processor_data = {
        "Manufacturer": manufacturer,
        "Model": model,
        "Architecture": architecture,
        "Cores": cores,
        "Frequency (GHz)": frequency_ghz,
        "Price": price
    }

    return processor_data

# Conectar a la base de datos MongoDB
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "processor"

client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Generar 10 registros de datos de procesadores y insertar en la colección
for _ in range(10):
    processor = generate_processor_data()

    # Insertar el documento en la colección
    insert_result = collection.insert_one(processor)

    if insert_result.acknowledged:
        print(f"Documento insertado con el ID: {insert_result.inserted_id}")
    else:
        print("Fallo al insertar el documento.")
