form fastapi import FastAPI
from db import create_table
from models import vehicles, destiny, routes

app=FastAPI(lifespan=create_tables, title="Transportes Sigmotoa")

app.include_router(vehicles.router, prefix="/vehicles")
app.include_router(destiny.router, prefix="/destiny")
app.include_router(routes.router, prefix="/routes")
