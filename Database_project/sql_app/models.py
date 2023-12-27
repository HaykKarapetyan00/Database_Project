from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

# models type (orm)...

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    inventory_number = Column(String)
    term_of_operation = Column(Integer)
    start_of_operation = Column(String)
    manufacturer = Column(String)

    product_specifications = relationship("ProductSpecification", back_populates="equipment")


class Material(Base):
    __tablename__ = "material"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    price_per_unit = Column(Float)
    unit_of_measurement = Column(String)
    alternative = Column(String)

    product_specifications = relationship("ProductSpecification", back_populates="material")


class ProductSpecification(Base):
    __tablename__ = "product_specification"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    name = Column(String)
    production_duration = Column(Integer, nullable=True)

    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    equipment = relationship("Equipment", back_populates="product_specifications")

    material_id = Column(Integer, ForeignKey("material.id"))
    material = relationship("Material", back_populates="product_specifications")
