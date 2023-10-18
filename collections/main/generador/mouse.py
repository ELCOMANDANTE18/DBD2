from faker import Faker
import random
from pymongo import MongoClient

fake = Faker()

def generate_mouse_data():
    manufacturers = ["Logitech", "HyperX", "Razer", "SteelSeries", "Corsair", "Cooler Master", "OMEN", "ROCCAT", "Ducky", "ZOWIE"]
    model = fake.word()
    mouse_type = random.choice(["Wired", "Wireless"])
    dpi = random.randint(800, 16000)
    price = random.randint(10, 100)

    mouse_data = {
        "Manufacturer": random.choice(manufacturers), 
        "Model": model,
        "Mouse Type": mouse_type,
        "DPI": dpi,
        "Price": price
    }

    return mouse_data

# Conexión a la base de datos MongoDB
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "mouse"  # Cambiar a "mouse" para datos de mouse

client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Generar 10 registros de datos de mouse y almacenarlos en la colección
for _ in range(100):
    mouse = generate_mouse_data()
    insert_result = collection.insert_one(mouse)
    if insert_result.acknowledged:
        print(f"Documento insertado con el ID: {insert_result.inserted_id}")
    else:
        print("Fallo al insertar el documento.")
