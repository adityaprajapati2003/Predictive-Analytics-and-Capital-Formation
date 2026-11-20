"""FastAPI entrypoint."""
from fastapi import FastAPI

from app.api.routes import (auth, chatbot, founders, investors, matches,
                            notifications, scores, startups)

app = FastAPI(title="Fundability Platform", version="0.1.0")

for module in (auth, founders, investors, startups, scores, matches, chatbot, notifications):
    app.include_router(module.router)


@app.get("/health")
def health():
    return {"status": "ok"}
