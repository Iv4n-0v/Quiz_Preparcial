from fastapi import APIRouter, HTTPException
from db import SessionDep
from models import vehicles,vehiclesBase
import traceback

router = APIRouter(tags=["vehicles"])

@router.post("/", response_model=vehicles)
def create_vehicle(new_user: vehiclesBase, session: SessionDep):
    try:
        vehicle =vehicles(**new_user.model_dump())
        session.add(vehicle)
        session.commit()
        session.refresh(vehicle)
        return vehicle
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")
