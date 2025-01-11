from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #This the route or URL from which fastapi will fetch the token

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,     #all the four lines are exceptions it has created
        detail="Could not validate credentials",    
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception)
    
    