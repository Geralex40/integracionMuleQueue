from fastapi import APIRouter, HTTPException
from app.model import AuthRequest, AuthResponse
import jwt, os, time
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_EXPIRE_SECONDS = int(os.getenv("TOKEN_EXPIRE_SECONDS", 3600))

@router.post("/token", response_model=AuthResponse)
def obtener_token(auth: AuthRequest):
    if auth.clientId == CLIENT_ID and auth.clientSecret == CLIENT_SECRET:
        payload = {"clientId": auth.clientId, "exp": time.time() + TOKEN_EXPIRE_SECONDS}
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return {"access_token": token, "expires_in": TOKEN_EXPIRE_SECONDS}
    raise HTTPException(status_code=401, detail="Invalid client credentials")