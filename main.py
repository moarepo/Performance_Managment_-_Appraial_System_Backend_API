from fastapi import FastAPI
from starlette import status 

app = FastAPI(
    title="Performance Managment & Appraial System Backend API",
    description="This application is the backend serevice for the Performance, Managment & Appraial System Backend System",
    version="0.0.1",
)

@app.get("/sataus",status_code=status.HTTP_200_OK)
def backend_api_status():
    return "API is online..."