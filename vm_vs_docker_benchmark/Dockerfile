# Imagen base completa (no slim)
FROM python:3.10

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libfreetype6-dev libavformat-dev libswscale-dev \
    libjpeg-dev libpng-dev libx11-6 x11-utils x11-xserver-utils xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia tu juego al contenedor
WORKDIR /app
COPY pacman_game.py .

# Instala dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install pygame psutil

# Ejecuta el juego usando entorno gráfico virtual
CMD ["xvfb-run", "-a", "python", "pacman_game.py"]
