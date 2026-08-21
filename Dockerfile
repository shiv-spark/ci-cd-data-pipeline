# FROM python:3.11-slim

# WORKDIR /app

# # Update Debian packages to receive security fixes
# RUN apt-get update \
#     && apt-get upgrade -y \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .

# # Upgrade Python packaging tools and vulnerable dependencies
# RUN python -m pip install --no-cache-dir --upgrade \
#         pip \
#         setuptools>=78.1.1 \
#         wheel \
#         jaraco.context \
#         msgpack>=1.2.1 \
#     && python -m pip install --no-cache-dir -r requirements.txt

# COPY src/ ./src/
# COPY data/ ./data/

# CMD ["python", "src/pipeline.py"]



# ---- Builder stage ----
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt \
    && pip install --no-cache-dir --prefix=/install --upgrade --ignore-installed \
       setuptools wheel jaraco.context msgpack


# ---- Runtime stage ----
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

COPY src/ ./src/
COPY data/ ./data/

CMD ["python", "src/pipeline.py"]