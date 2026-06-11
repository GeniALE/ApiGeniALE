from fastapi import FastAPI
from app.routes import members

app = FastAPI()
app.include_router(members.route)


@app.get("/health", tags=["health"])
async def health_check():
	return {"status": "ok"}

@app.get("/", tags=["root"])
async def root():
    return {"message": "Bienvenue sur l'API de GeniALE!"}

