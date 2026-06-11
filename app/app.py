from fastapi import FastAPI
from app.routes import members

app = FastAPI()
app.include_router(members.route)


@app.get("/health", tags=["health"])
async def health_check():
	return {"status": "ok"}

