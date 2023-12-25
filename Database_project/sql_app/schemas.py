from pydantic import BaseModel
from typing import Optional


class EquipmentBase(BaseModel):
    name: str
    inventory_number: str
    term_of_operation: int
    start_of_operation: str
    manufacturer: str


class EquipmentCreate(EquipmentBase):
    pass


class Equipment(EquipmentBase):
    id: int

    class Config:
        orm_mode = True


class MaterialBase(BaseModel):
    name: str
    type: str
    price_per_unit: float
    unit_of_measurement: str
    alternative: Optional[str]


class MaterialCreate(MaterialBase):
    pass


class Material(MaterialBase):
    id: int

    class Config:
        orm_mode = True


class ProductSpecificationBase(BaseModel):
    quantity: int
    name: str
    production_duration: Optional[int]


class ProductSpecificationCreate(ProductSpecificationBase):
    pass


class ProductSpecification(ProductSpecificationBase):
    id: int
    equipment_id: int
    material_id: int

    class Config:
        orm_mode = True
