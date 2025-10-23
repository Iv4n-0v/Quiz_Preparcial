from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class vehiclesDestinyLink(SQLModel,table=True):
    vehicles_id: Optional[int]=Field(default=None,foreign_key="vehicles.id",primary_key=True)
    destiny_id: Optional[int]=Field(default=None,foreign_key="destiny.id",primary_key=True)

class vehiclesBase(SQLModel):
 type : str

class vehicles(vehiclesBase, table=True):
 id: Optional[int]=Field(default=None,primary_key=True)
 destiny: List["destiny"]=Relationship(back_populates="vehicles",link_model=vehiclesDestinyLink)

class destinyBase(SQLModel):
  starting_point: str

class destiny(destinyBase, table=True):
    id: Optional[int]=Field(default=None,primary_key=True)
    vehicles: List["vehicles"]=Relationship(back_populates="destiny",link_model=vehiclesDestinyLink)
