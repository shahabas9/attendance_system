# Attendance System Backend (FastAPI + PostgreSQL)

Production scaffold for CCTV-based face recognition attendance.

## Getting Started

1. **Clone repo & install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup PostgreSQL & update `DATABASE_URL` in `.env` or `core/config.py`.**

3. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Run server:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Explore modular API routes:**
   - `/auth` - login/register
   - `/users` - user management/enrollment
   - `/attendance` - logs/sessions/daily
   - `/cameras` - camera/zone CRUD, health
   - `/mobile` - mobile app endpoints
   - `/admin` - admin dashboard/reporting
   - `/fallback` - fallback/error handling
   - `/alerts` - monitoring/alerts
   - `/metrics` - Prometheus metrics
   - `/health` - health check endpoint

## License

MIT