"""The App module contains the main FastAPI application instance and the route definitions for the API endpoints. 
It serves as the entry point for the application and includes a health check endpoint to verify that the API is running correctly."""

from fastapi import FastAPI, Request
from app.routes import members
import time
from fastapi.responses import FileResponse
import uuid

#TODO: Add CORS middleware if the API will be accessed from a frontend application hosted on a different domain.

app = FastAPI(title="GeniALE API", description="API for GeniALE application", version="1.0.0")
app.include_router(members.route, prefix="/api/v1", tags=["members"])
favicon_path = "favicon.ico"

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path, media_type="image/x-icon")

@app.get("/health", tags=["health"])
async def health_check():
	return {"status": "ok"}

@app.get("/", tags=["root"])
async def root():
    return {"message": "Bienvenue sur l'API de GeniALE!"}

#TODO: Add more middleware for logging, authentication, etc. as needed.
# Basic middleware based on the FastAPI documentation
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Request-ID"] = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-API-Version"] = app.version
    return response