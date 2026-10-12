from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db, SessionLocal
from app.seed import seed_data

app = FastAPI(title="KaushalSetu AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()
    seed_data()


@app.get("/health")
def health():
    return {"status": "ok", "message": "KaushalSetu AI backend is running"}


from app.routes import auth, worker, assessor, admin, reports, qualifications

app.include_router(auth.router, prefix="/api")
app.include_router(worker.router, prefix="/api")
app.include_router(assessor.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(reports.router, prefix="/api")
app.include_router(qualifications.router, prefix="/api")
