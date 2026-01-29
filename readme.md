# AI Worker Productivity Dashboard

A full-stack web application that ingests AI-generated factory events, stores them in a database, computes metrics, and displays them in a professional dashboard.

---

## 📦 Project Structure

```
biztech_mlops/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
   ├── schemas.py
   ├── seed.py
   ├── metrics.py
   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ▶ Step 0 — Clone the Repository

```bash
git clone https://github.com/Ganga522/MLOps-Project.git
cd MLOps-Project
```

---

## ▶ Step 1 — Backend Setup (FastAPI + Docker)

### 1.1 Build and start the backend using Docker

```bash
docker-compose up --build
```

### 1.2 Backend API URLs

* Swagger UI: `http://localhost:8000/docs`
* Health Check: `http://localhost:8000/health`
* Worker Metrics: `http://localhost:8000/metrics/workers`
* Workstation Metrics: `http://localhost:8000/metrics/workstations`
* Factory Metrics: `http://localhost:8000/metrics/factory`
* Reseed Dummy Data: `http://localhost:8000/seed`

> ✅ Make sure the backend container is running before accessing these endpoints.

---

## ▶ Step 2 — Frontend Setup

### 2.1 Navigate to frontend folder

```bash
cd frontend
```

### 2.2 Start a simple HTTP server

```bash
python -m http.server 3000
```

### 2.3 Frontend Dashboard URL

```
http://localhost:3000
```

Open this URL in your browser to view the dashboard.



## ✅ Key Notes

* Ensure Docker is installed and running for backend.
* Frontend must point to the correct backend URL.
* Dummy data is auto-seeded at backend startup.
* Use `/seed` API to refresh dummy data anytime.

---

**Author:** K. Gangadhar

**Role Applied:** Full-Stack MLOps Engineer
