from fastapi import APIRouter, Depends, HTTPException
from app.model import PlaceRequest
from app.auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/place", dependencies=[Depends(JWTBearer())])
def crear_place(place: PlaceRequest):
    if not place.placeCode or not place.shortName:
        raise HTTPException(status_code=400, detail="Invalid data")
    try:
        return {"message": "Place created successfully", "data": place.dict()}
    except Exception:
        raise HTTPException(status_code=500, detail="Technical error")