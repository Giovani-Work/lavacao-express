from fastapi import FastAPI
from routers import appointment, auth, service, user

app = FastAPI()
app.include_router(appointment.router, prefix="/api/v1/appointment")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(service.router, prefix="/api/v1/service")
app.include_router(user.router, prefix="/api/v1/user")
