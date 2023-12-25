import requests
import random
import string

API_URL = "http://127.0.0.1:8000/"  

def generate_equipment_data():
    return {
        "name": ''.join(random.choices(string.ascii_letters, k=10)),
        "inventory_number": ''.join(random.choices(string.digits, k=5)),
        "term_of_operation": random.randint(1, 10),
        "start_of_operation": "2023-01-01",
        "manufacturer": "Manufacturer XYZ",
    }

def generate_material_data():
    return {
        "name": ''.join(random.choices(string.ascii_letters, k=8)),
        "type": "Type ABC",
        "price_per_unit": round(random.uniform(1, 100), 2),
        "unit_of_measurement": "Unit XYZ",
    }

def generate_product_specification_data(equipment_id, material_id):
    return {
        "quantity": random.randint(1, 100),
        "name": "Specification XYZ",
        "equipment_id": equipment_id,
        "material_id": material_id,
    }

def populate_database(num_records):
    for _ in range(num_records):
        equipment_data = generate_equipment_data()
        material_data = generate_material_data()

        equipment_response = requests.post(f"{API_URL}/equipment/", json=equipment_data)
        if equipment_response.status_code != 200:
            print(f"Failed to create equipment: {equipment_data}")
            continue

        equipment_id = equipment_response.json().get("id")

        material_response = requests.post(f"{API_URL}/material/", json=material_data)
        if material_response.status_code != 200:
            print(f"Failed to create material: {material_data}")
            continue

        material_id = material_response.json().get("id")

        product_specification_data = generate_product_specification_data(equipment_id, material_id)
        product_specification_response = requests.post(f"{API_URL}/product_specification/", json=product_specification_data)
        if product_specification_response.status_code != 200:
            print(f"Failed to create product specification: {product_specification_data}")
            continue

        print(f"Successfully created: Equipment - {equipment_data}, Material - {material_data}, Product Specification - {product_specification_data}")

num_records_to_add = 100  

populate_database(num_records_to_add)
