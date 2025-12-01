FROM python:3.10-slim

WORKDIR /app

# Only copy the app file (no need for tests here)
COPY app.py /app/app.py

# No dependencies needed for this simple demo
CMD ["python", "app.py"]
