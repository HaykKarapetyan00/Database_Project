from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List

# main.py run by -> uvicorn sql_app.main:app --reload from database folder

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#database population for equipments...

@app.on_event("startup")
def startup_fill_db():
    db = SessionLocal()
    num_equipment = db.query(models.Equipment).count()
    if num_equipment == 0:
        equipments = []
        for i in range(1000):
            temp_equipment = {
                'name': f"Equipment {i + 1}",
                'inventory_number': f"Inventory {i + 1}",
                'term_of_operation': 5,
                'start_of_operation': '2023-01-01',
                'manufacturer': f"Manufacturer {i + 1}"
            }
            equipments.append(temp_equipment)
        for equipment in equipments:
            crud.create_equipment(db, schemas.EquipmentCreate(**equipment))
        db.close()
        print("Equipments populated.")
    else:
        print(f"{num_equipment} equipment(s) already exist")

#decorators
        
@app.post("/equipment/", response_model=schemas.Equipment)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    return crud.create_equipment(db=db, equipment=equipment)


@app.get("/equipment/", response_model=List[schemas.Equipment])
def read_equipment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_equipment(db, skip=skip, limit=limit)


@app.get("/equipment/{equipment_id}", response_model=schemas.Equipment)
def read_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment_by_id(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment


@app.post("/material/", response_model=schemas.Material)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    return crud.create_material(db=db, material=material)


@app.get("/material/", response_model=List[schemas.Material])
def read_material(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_material(db, skip=skip, limit=limit)


@app.get("/material/{material_id}", response_model=schemas.Material)
def read_material(material_id: int, db: Session = Depends(get_db)):
    db_material = crud.get_material_by_id(db, material_id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@app.post("/product_specification/", response_model=schemas.ProductSpecification)
def create_product_specification(product_specification: schemas.ProductSpecificationCreate, db: Session = Depends(get_db)):
    return crud.create_product_specification(db=db, product_specification=product_specification)


@app.get("/product_specification/", response_model=List[schemas.ProductSpecification])
def read_product_specification(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_specification(db, skip=skip, limit=limit)


@app.get("/product_specification/{product_specification_id}", response_model=schemas.ProductSpecification)
def read_product_specification(product_specification_id: int, db: Session = Depends(get_db)):
    db_product_specification = crud.get_product_specification_by_id(db, product_specification_id=product_specification_id)
    if db_product_specification is None:
        raise HTTPException(status_code=404, detail="Product Specification not found")
    return db_product_specification

def update_decorator(type_name):
    def decorator(func):
        def wrapper(db: Session, item_id: int, item_update: type):
            db_item = func(db, item_id, item_update)
            if not db_item:
                raise HTTPException(status_code=404, detail=f"{type_name} not found")
            return db_item
        return wrapper
    return decorator

def delete_decorator(type_name):
    def decorator(func):
        def wrapper(db: Session, item_id: int):
            db_item = func(db, item_id)
            if not db_item:
                raise HTTPException(status_code=404, detail=f"{type_name} not found")
            return db_item
        return wrapper
    return decorator

@app.put("/equipment/{equipment_id}")
def update_equipment(equipment_id: int, equipment_update: schemas.EquipmentUpdate, db: Session = Depends(get_db)):
    return crud.update_equipment(db, equipment_id, equipment_update)

@app.delete("/equipment/{equipment_id}")
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    return crud.delete_equipment(db, equipment_id)

@app.put("/material/{material_id}")
def update_material(material_id: int, material_update: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    return crud.update_material(db, material_id, material_update)

@app.delete("/material/{material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db)):
    return crud.delete_material(db, material_id)


@app.put("/product-specification/{product_specification_id}")
def update_product_specification(product_specification_id: int, product_specification_update: schemas.ProductSpecificationUpdate, db: Session = Depends(get_db)):
    return crud.update_product_specification(db, product_specification_id, product_specification_update)

@app.delete("/product-specification/{product_specification_id}")
def delete_product_specification(product_specification_id: int, db: Session = Depends(get_db)):
    return crud.delete_product_specification(db, product_specification_id)
