FROM python:3.11-slim

# Instala Java (requerido por H2O)
RUN apt-get update && apt-get install -y default-jre

# Crea directorio de trabajo
WORKDIR /app

# Copia el código
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8080

# Ejecuta la API
CMD ["python", "app.py"]
