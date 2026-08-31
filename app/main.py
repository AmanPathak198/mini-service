from fastapi import FastAPI

__version__ = "0.1.0"

app = FastAPI(title="mini-service", version=__version__)


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


# TODO (PROJ-101): add a /health endpoint here.
# See the ticket for the exact response shape expected.
