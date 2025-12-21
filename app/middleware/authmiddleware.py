from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import Response
from typing import Callable, Awaitable,Any
from jose import jwt, JWTError
from app.utils.configs import config

class AuthMiddlware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]])->Response:
        # 
        if request.url.path.startswith("/auth"):
            return await call_next(request)
        auth = request.headers.get("Authorization")
        
        if not auth or auth.startswith("Bearer "):
            return JSONResponse({"detail":"missing token"},status_code=401)
        token = auth.split(" ")[1]
        
        try:
            payload:dict[str,Any]=jwt.decode(token,key=config.SECRET,algorithms=[config.ALGO],options={"verify_exp":True})
        
        except JWTError:
            return JSONResponse({"detail": "Invalid or expired token"}, status_code=401)
        
        request.state.user={
            "user_id"   :payload["sub"],
            "role"      :payload["role"],
            "tenant_id" :payload["tenant_id"],
            "device_id" :payload["device_id"]
        }
        return await call_next(request)