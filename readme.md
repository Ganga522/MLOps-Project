# AI Worker Productivity Dashboard

A full-stack web application that ingests AI-generated factory events, stores them in a database, computes metrics, and displays them in a dashboard.

---

## 📦 Project Structure

```
biztech_mlops/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   ├── metrics.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ▶️ Step 1 — Run Project Locally with Docker

### 1.1 Navigate to project folder

```bash
cd biztech_mlops
```

### 1.2 Build and start backend

```bash
docker-compose up --build
```

### 1.3 Backend API URL

* Swagger UI: `http://localhost:8000/docs`
* Health Check: `http://localhost:8000/health`
* Metrics: `/workers`, `/workstations`, `/factory`

---

## ▶ Step 2 — Run Frontend

### 2.1 Navigate to frontend folder

```bash
cd frontend
```

### 2.2 Start a simple HTTP server

```bash
python -m http.server 3000
```

### 2.3 Frontend URL

```
http://localhost:3000
```

Open this in your browser to see the dashboard.

> ⚠️ Make sure the API URL in `app.js` matches your backend URL:

```javascript
const API = "http://localhost:8000";
```
