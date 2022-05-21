from datetime import datetime, timedelta

from jose import JWTError, jwt

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "8737cf18311975ea503f9565c01f5fd1e5fec7593dd9054c3d5284def77bb4c1" # TODO: Make this env var
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_jwt(access_token: str) -> bool | dict: 
    try: 
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None: 
            return False 

        return {"email": email}
    except JWTError: 
        return False
    