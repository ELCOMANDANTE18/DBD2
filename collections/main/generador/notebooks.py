from faker import Faker
from pymongo import MongoClient
import random

fake = Faker()

# Función para generar datos aleatorios de notebooks
def generate_random_notebook_data():
    manufacturer = random.choice(["Apple", "HP", "Lenovo", "Dell", "Acer", "Asus", "MSI", "Razer", "Microsoft Surface", "Samsung"])
    model = fake.word()
    processor = fake.word()
    ram = random.randint(4, 64)  # Genera un valor de RAM entre 4GB y 64GB
    storage = random.choice(["HDD", "SSD", "Hybrid"])
    sistema_operativo = random.choice(["Windows 10", "MacOS", "Linux"])
    # Genera un precio múltiplo de 100 entre $300 y $2500
    price = random.randint(3, 25) * 100

    notebook_data = {
        "marca": manufacturer,
        "modelo": model,
        "precio": price,
        "procesador": processor,
        "memoria_ram": ram,
        "almacenamiento": storage,
        "sistema_operativo": sistema_operativo  # Ajusta el sistema operativo según tus necesidades
    }

    return notebook_data

# Cambia estas credenciales y la URL de conexión a tu configuración
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "notebooks"

# Conecta a la base de datos
client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Generar 10 registros de datos de notebooks y guardarlos en la base de datos
for _ in range(100):
    notebook = generate_random_notebook_data()
    insert_result = collection.insert_one(notebook)

    if insert_result.acknowledged:
        print(f"Documento insertado con el ID: {insert_result.inserted_id}")
    else:
        print("Fallo al insertar el documento.")
