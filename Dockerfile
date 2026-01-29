FROM python:3.10

WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic

# Render uses the $PORT environment variable, we'll default to 8000
EXPOSE 8000

# This command runs the backend AND a simple python server for the frontend 
# in the background so they both exist on the same 'service'.
CMD python -m http.server 3000 --directory frontend & \
    uvicorn backend.main:app --host 0.0.0.0 --port 8000
