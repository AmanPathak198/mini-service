# mini-service

A deliberately tiny FastAPI service, built to practice the full software delivery
process (tickets → branching → PR review → CI → CD → environments → approvals)
without spending time on the programming itself.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000 and http://127.0.0.1:8000/docs

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t mini-service .
docker run -p 8000:8000 mini-service
```
