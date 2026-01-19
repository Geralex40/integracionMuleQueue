from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

# Crear app
app = FastAPI()
app.title = "GSAPI"

# Configuracion, investigar mas
SECRET_KEY = "clave_secreta_para_firmar_tokens"
ALGORITHM = "HS256"
TOKEN_DURACION_HORAS = 0.5

# Modelo de entrada para autenticacion
class Credenciales(BaseModel):
    clientId:       str
    clientSecret:   str
# Modelo para la ubicacion
class Location(BaseModel):
    latitude:   float
    longitude:  float
# Modelo para los datos de lugar
class PlaceData(BaseModel):
    placeCode:          str
    shortName:          str
    type:               str
    commercialName:     str
    longName:           str
    status:             str
    location:           Location

# Base de datos simulada para autenticacion
CLIENTES_VALIDOS = {
    "cliente1": {
        "clientId": "cliente1",
        "clientSecret": "123456"
    }
}
# Base de datos simulada para alta
datos_almacenados = []
contador_datos = 0

# Funcion para crear token con JWT
def crear_access_token(client_id: str) -> str:
    """
    Crea un token JWT con fecha de expiración
    """
    # Datos que van DENTRO del token
    datos = {
        "sub": client_id,
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_DURACION_HORAS)
    }
    # Crear token JWT firmado
    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Funcion para validar tokens
security = HTTPBearer()
def validar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Valida el token
    """
    token = credentials.credentials
    try:
        # Decodificar token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        # Extraer client_id del token
        client_id = payload.get("sub")
        if client_id is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Token invalido"
            )
        # Devolver informacion del cliente
        return {"client_id": client_id}
    # Token expirado
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Token expirado"
        )
    # Cualquier otro error de token
    except jwt.JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Token invalido"
        )
    
# ENDPOINT para generar token
@app.post("/auth/token", tags = ['Autenticacion'])
def generar_token(credenciales: Credenciales):
    """
    Genera un token de acceso
    """
    # Buscar el cliente
    cliente = CLIENTES_VALIDOS.get(credenciales.clientId)
    print(cliente)
    # Si no existe, error
    if not cliente:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )
    # Verificar contraseña
    if cliente["clientSecret"] != credenciales.clientSecret:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )
    # Crear token JWT
    access_token = crear_access_token(credenciales.clientId)
    # Devolver respuesta
    return {
        "access_token": access_token,
        "expires_in": TOKEN_DURACION_HORAS * 3600,
        "token_type": "bearer"
    }

# ENDPOINT para alta de parada
@app.post("/ext/v1/place", tags = ["Alta paradas"])
def alta_parada(
    place_data: PlaceData,
    token_data: dict = Depends(validar_token)
):
    """
    Alta de una parada
    """
    global datos_almacenados, contador_datos
    # Agregar a la lista de alamacenamiento
    datos_almacenados.append(place_data)
    contador_datos += 1
    # Devolver confirmacion
    return {
        "success": True,
        "message": f"Dato almacenado con exito (ID: {contador_datos})",
        "total_places": contador_datos
    }

# ENDPOINT para ver datos almacenados
@app.get("/places", tags=["Paradas"])
def obtener_places(token_data: dict = Depends(validar_token)):
    """
    Obtiene todos los lugares almacenados
    """
    return {
        "total_places": contador_datos,
        "places": datos_almacenados
    }