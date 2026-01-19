from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt, os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials and credentials.scheme == "Bearer":
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=401, detail="Invalid or expired token")
            return credentials.credentials
        raise HTTPException(status_code=403, detail="Invalid authorization code")

    def verify_jwt(self, token: str) -> bool:
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False