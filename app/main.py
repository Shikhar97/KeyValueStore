from fastapi import FastAPI, status
from redis_huey import get_key, delete_key, add_key
from models.key_value_model import KeyValueModel
from fastapi.responses import JSONResponse

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.post("/api/v1/add")
async def add_value(data: KeyValueModel):
    try:
        response = add_key(data.key, data.value)
        value = response.get(True)
        return JSONResponse(content={
            "message": "Value added successfully"
        }, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content={
            "error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/api/v1/get/{key}")
async def read_value(key):
    try:
        response = get_key(key)
        value = response.get(True)
        return JSONResponse(content={
            "value": value
        }, status_code=status.HTTP_200_OK)
    except Exception as e:
        if "not found" in str(e):
            return JSONResponse(content={
                "error": str(e)}, status_code=status.HTTP_404_NOT_FOUND)
        return JSONResponse(content={
            "error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


@app.delete("/api/v1/delete/{key}")
async def delete_value(key):
    try:
        response = delete_key(key)
        value = response.get(True)
        return JSONResponse(content={
            "message": "Value deleted successfully"
        }, status_code=status.HTTP_200_OK)
    except Exception as e:
        if "not found" in str(e):
            return JSONResponse(content={
                "error": str(e)}, status_code=status.HTTP_404_NOT_FOUND)
        return JSONResponse(content={
            "error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)
