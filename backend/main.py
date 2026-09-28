from fastapi import FastAPI

app = FastAPI(title="SentinelMesh")


@app.get("/health")
def health():
    return {"status": "ok"}
