# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ ./src/
# COPY data/ ./data/

# CMD ["python", "src/pipeline.py"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade Python packaging tools and fix known vulnerable packages
RUN python -m pip install --upgrade pip setuptools wheel jaraco.context \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

COPY data/ ./data/

CMD ["python", "src/pipeline.py"]