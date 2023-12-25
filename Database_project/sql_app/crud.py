from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_equipment(db: Session, equipment: schemas.EquipmentCreate):
    db_equipment = models.Equipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


def get_equipment(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Equipment).offset(skip).limit(limit).all()


def get_equipment_by_id(db: Session, equipment_id: int):
    return db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()


def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def get_material(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Material).offset(skip).limit(limit).all()


def get_material_by_id(db: Session, material_id: int):
    return db.query(models.Material).filter(models.Material.id == material_id).first()


def create_product_specification(db: Session, product_specification: schemas.ProductSpecificationCreate):
    db_product_specification = models.ProductSpecification(**product_specification.dict())
    db.add(db_product_specification)
    db.commit()
    db.refresh(db_product_specification)
    return db_product_specification


def get_product_specification(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductSpecification).offset(skip).limit(limit).all()


def get_product_specification_by_id(db: Session, product_specification_id: int):
    return db.query(models.ProductSpecification).filter(models.ProductSpecification.id == product_specification_id).first()
