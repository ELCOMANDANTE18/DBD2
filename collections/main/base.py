from pymongo import MongoClient
from main import generate_keyboard_data

# Cambia estas credenciales y la URL de conexión a tu configuración
uri = "mongodb+srv://admin:1234@cluster0.nktfur3.mongodb.net/?retryWrites=true&w=majority"
db_name = "Ecomerce"
collection_name = "notebooks"

# Conecta a la base de datos
client = MongoClient(uri)
db = client[db_name]
collection = db[collection_name]

# Insertar datos en la colección
data_to_insert = {
    "marca": "HP",
    "modelo": "Pavilion 15",
    "precio": 799.99,
    "pantalla": "15.6 pulgadas",
    "procesador": "Intel Core i5",
    "memoria_ram": 8,
    "almacenamiento": "256GB SSD",
    "sistema_operativo": "Windows 10"
}


# Insertar el documento en la colección
insert_result = collection.insert_one(data_to_insert)

if insert_result.acknowledged:
    print(f"Documento insertado con el ID: {insert_result.inserted_id}")
else:
    print("Fallo al insertar el documento.")

