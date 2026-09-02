from fastapi import FastAPI

__version__ = "0.1.0"

app = FastAPI(title="mini-service", version=__version__)


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": __version__
    }

