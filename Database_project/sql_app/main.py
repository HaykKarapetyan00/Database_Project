from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
