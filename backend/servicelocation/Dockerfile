# Utiliser une image officielle de Python comme image de base
FROM python:3.9-slim

# Définir des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer les dépendances système
RUN apt-get update && apt-get install -y apt-utils
	
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    gdal-bin \
    python3-venv \
    build-essential \
    python3-dev \
    libgdal-dev
# Créer et définir le répertoire de travail
WORKDIR /app

# Créer un environnement virtuel Python
RUN python3 -m venv /venv

# Activer l'environnement virtuel
ENV PATH="/venv/bin:$PATH"

# Copier les fichiers de l'application
COPY . /app/

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Commande pour démarrer l'application avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "annonce.wsgi:application"]

