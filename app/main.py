from fastapi import FastAPI, status, HTTPException
from redis_huey import get_key, delete_key, add_key
from models.key_value_model import KeyValueModel


app = FastAPI()


@app.post("/api/v1/add", status_code=status.HTTP_201_CREATED)
async def add_value(data: KeyValueModel):
    try:
        response = add_key(data.key, data.value)
        value = response.get(True)
        return {
            "message": "Value added successfully"
        }
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.get("/api/v1/get/{key}", status_code=status.HTTP_200_OK)
async def read_value(key):
    try:
        response = get_key(key)
        value = response.get(True)
        return {
            "message": "Value retrieved successfully", "value": value
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@app.delete("/api/v1/delete/{key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_value(key):
    try:
        response = delete_key(key)
        value = response.get(True)
        return {
            "message": "Value deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
