FROM python:3.14.6-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ ./src/
COPY pyproject.toml .

CMD ["fastapi", "run"]
