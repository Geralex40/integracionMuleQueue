from pydantic import BaseModel

# Esquema de autenticación
class AuthRequest(BaseModel):
    clientId: str
    clientSecret: str

class AuthResponse(BaseModel):
    access_token: str
    expires_in: int

# Esquema de Place
class Location(BaseModel):
    latitude: float
    longitude: float

class PlaceRequest(BaseModel):
    placeCode: str
    shortName: str
    type: str
    commercialName: str
    longName: str
    status: str
    location: Location