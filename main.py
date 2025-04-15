from typing import Union
from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/db-check")
def check_db() -> dict[str, Union[str, int]]:
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).scalar()
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
