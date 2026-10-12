# KaushalSetu AI

AI-assisted skill assessment and recognition platform for Recognition of Prior Learning (RPL) for Smart India Hackathon 2026.

## Features

- Worker portal with guided profile and evidence collection
- AI-assisted qualification mapping with deterministic fallback
- Assessor dashboard with rubric-based scoring
- Admin dashboard with analytics and audit trends
- Offline-first status page and sync-ready architecture
- SQLite persistence and demo seed data
- Gemini-ready configuration via environment variables

## Tech stack

- Frontend: React + TypeScript + Vite
- Backend: Python FastAPI
- Persistence: SQLite (configurable for PostgreSQL later)
- AI: Gemini API with deterministic fallback when the key is not configured

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

### 3) Environment

Copy `.env.example` to `.env` and set your values.

## Demo credentials

- Worker: `worker@demo.local` / `demo123`
- Assessor: `assessor@demo.local` / `demo123`
- Admin: `admin@demo.local` / `demo123`

This application intentionally uses demonstration data and must be reviewed by authorised human assessors before any certification decision.
