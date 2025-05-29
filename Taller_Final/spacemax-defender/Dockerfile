FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-numpy \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY spacemax_defender.py .
COPY assets/ ./assets/

# Usuario no root
RUN useradd -m -u 1000 gameuser && chown -R gameuser:gameuser /app
USER gameuser

CMD ["python", "spacemax_defender.py"]
