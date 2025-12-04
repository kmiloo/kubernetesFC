# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Primero copiamos los requisitos e instalamos (para aprovechar la caché de Docker)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copiamos el resto del código
COPY app/ .

# Por defecto, al arrancar el contenedor, ejecutará el servidor
CMD ["python", "server.py"]