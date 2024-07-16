from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from .handler import decodeJWT
 
class Bearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(Bearer, self).__init__(auto_error=auto_error)
 
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(Bearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
            
    def verify_jwt(self, token: str):
        decoded_token = decodeJWT(token)
        if decoded_token:
            return True
        return False