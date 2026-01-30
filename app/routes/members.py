from fastapi import FastAPI

app = FastAPI()



@app.get("")
def get_members():
    return {"message": "List of members"}