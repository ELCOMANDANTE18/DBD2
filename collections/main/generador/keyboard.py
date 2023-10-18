from pymongo import MongoClient
from faker import Faker
import random

fake = Faker()

# Define una función para generar datos de teclado
def generate_keyboard_data():
    manufacturers = ["Logitech", "HyperX", "Razer", "SteelSeries", "Corsair", "Cooler Master", "OMEN", "ROCCAT", "Ducky", "ZOWIE"]
    model = fake.word()
    keyboard_type = random.choice(["Mechanical", "Membrane", "Scissor", "Ergonomic"])
    key_switch = random.choice(["Cherry MX", "Razer Green", "Logitech Romer-G"])
    price = random.randint(50, 300)

    keyboard_data = {
        "Manufacturer": random.choice(manufacturers),
        "Model": model,
        "Keyboard Type": keyboard_type,
        "Key Switch": key_switch,
        "Price": price
    }

    return keyboard_data

# Cambia estas credenciales y la URL de conexión a tu configuración
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "keyboard"

# Conecta a la base de datos
client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Generar 10 registros de datos de teclados y almacenarlos en MongoDB
for _ in range(10):
    keyboard = generate_keyboard_data()
    insert_result = collection.insert_one(keyboard)

    if insert_result.acknowledged:
        print(f"Documento insertado con el ID: {insert_result.inserted_id}")
    else:
        print("Fallo al insertar el documento.")
