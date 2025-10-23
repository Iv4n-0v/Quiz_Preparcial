from fastapi import APIRouter, HTTPException
from db import SessionDep
from models import destiny,destinyBase

router=APIRouter(tags=["destiny"])

@router.post("/destiny/", response_model=destiny)
def create_destiny(new_destiny:destinyBase, session:SessionDep):
    destiny=destiny.model_validate(new_destiny)

@router.get("/all", response_model=list[destiny])
def get_all_methodologies(session: SessionDep):
    return session.query(destiny).all()