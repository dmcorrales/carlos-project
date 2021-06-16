from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.entry_points import rules
import uvicorn

app = FastAPI()

app.include_router(rules.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
