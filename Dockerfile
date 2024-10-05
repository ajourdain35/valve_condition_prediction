FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY README.md .
COPY tests/ ./tests
COPY src/ ./src
COPY templates/ ./templates
COPY notebooks/ ./notebooks
COPY data_subset/ ./data_subset

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]