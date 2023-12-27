from pydantic import BaseModel
from typing import Optional

# schemas for crud types...

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

class EquipmentUpdate(BaseModel):
    name: Optional[str]
    inventory_number: Optional[str]
    term_of_operation: Optional[int]
    start_of_operation: Optional[str]
    manufacturer: Optional[str]

class EquipmentDelete(BaseModel):
    id: int

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

class MaterialUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    price_per_unit: Optional[float]
    unit_of_measurement: Optional[str]
    alternative: Optional[str]

class MaterialDelete(BaseModel):
    id: int

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


class ProductSpecificationUpdate(BaseModel):
    quantity: Optional[int]
    name: Optional[str]
    production_duration: Optional[int]

class ProductSpecificationDelete(BaseModel):
    id: int