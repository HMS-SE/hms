from fastapi import FastAPI

app = FastAPI()


@app.get("/__status__")
def status():
    return {"status": "OK"}
