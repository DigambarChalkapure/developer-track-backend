from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, topics, progress, analytics, studytime, flashcards, quests

app = FastAPI(title="Developer Learning Tracker API")

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://127.0.0.1:5174",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(topics.router)
app.include_router(progress.router)
app.include_router(analytics.router)
app.include_router(studytime.router)
app.include_router(flashcards.router)
app.include_router(quests.router)

@app.get("/")
def root():
    return {"message": "Developer Learning API works!"}
