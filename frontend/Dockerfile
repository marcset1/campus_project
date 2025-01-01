# frontend/Dockerfile

FROM nginx:latest

# Copier les fichiers de configuration Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copier les fichiers statiques dans le répertoire de Nginx
COPY monbailleur /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

