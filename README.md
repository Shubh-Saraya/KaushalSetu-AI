# KaushalSetu AI

AI-assisted skill assessment and Recognition of Prior Learning (RPL) demo platform built for the Smart India Hackathon 2026 challenge.

## Project overview

KaushalSetu AI is a role-based RPL application for workers, assessors, and administrators. It includes a guided worker profile flow, AI-assisted qualification matching, assessor Rubric evaluation, admin analytics, and a synthetic demo dataset clearly labeled as demonstration-only and requiring official verification.

## Stack

- Frontend: React + TypeScript + Vite
- Backend: Python FastAPI
- Database: SQLite (ready to move to PostgreSQL)
- AI: Gemini-ready integration with deterministic fallback when the key is absent
- Security: role-based demo access, audit trail, privacy disclaimers

## Demo login credentials

- Worker: `worker@demo.local` / `demo123`
- Assessor: `assessor@demo.local` / `demo123`
- Admin: `admin@demo.local` / `demo123`

## Run locally

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## Environment variables

Copy `.env.example` and configure values before production use.

## Important notes

- All AI-generated outputs are clearly treated as suggestions and not certificates.
- Synthetic qualification data and demo records are intentionally marked as requiring official verification.
- Human assessor review remains mandatory before final certification decisions.
