from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router # Import the router

app = FastAPI(
    title="FastAPI Application",
    description="FastAPIを使用したWebアプリケーション",
    version="1.0.0"
)

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPIへようこそ！"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(api_router, prefix="/api/v1") # Include the router with a prefix