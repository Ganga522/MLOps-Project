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

---

## ▶ Step 3 — Push Project to GitHub

```bash
git init
git add .
git commit -m "Initial commit - AI Worker Productivity Dashboard"
git branch -M main
git remote add origin https://github.com/<your-username>/biztech_mlops.git
git push -u origin main
```

---

## ▶ Step 4 — Deploy Backend on Render

1. Go to [Render.com](https://render.com) and login.
2. Click **New → Web Service**
3. Connect your GitHub repo (`biztech_mlops`) and select **main** branch
4. Set **Root Directory** to `backend`
5. Build Command:

```bash
pip install -r requirements.txt
```

6. Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

7. Select **Free Instance**
8. Click **Create Web Service**

* Your public backend URL will be generated, e.g. `https://ai-worker-dashboard-t5yl.onrender.com`

---

## ▶ Step 5 — Connect Frontend to Deployed Backend

In `frontend/app.js`, update the API URL:

```javascript
const API = "https://ai-worker-dashboard-t5yl.onrender.com";
```

Then redeploy frontend using Render Static Site, Netlify, or similar.

---

## ▶ Step 6 — Test Deployment

Test these endpoints:

* `https://ai-worker-dashboard-t5yl.onrender.com/health`
* `https://ai-worker-dashboard-t5yl.onrender.com/workers`
* `https://ai-worker-dashboard-t5yl.onrender.com/workstations`
* `https://ai-worker-dashboard-t5yl.onrender.com/factory`

Open frontend in browser and verify metrics are visible.

---

## Notes

* Render Free tier sleeps when idle; first request may take 30–50s.
* Ensure API URL in frontend matches deployed backend.
* All commands above assume Python 3 and Docker installed locally.
