from fastapi import FastAPI
from app.routers import auth_router, place_router

app = FastAPI(title="GSAPI")

# Registrar routers
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(place_router.router, prefix="/ext/v1", tags=["Place"])

# Para correr: uvicorn main:app --reload --port 8082