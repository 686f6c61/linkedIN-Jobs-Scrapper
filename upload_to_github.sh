#!/bin/bash

# Script para subir el proyecto a GitHub
# Repositorio: https://github.com/686f6c61/linkedIN-Jobs-Scrapper

echo "📦 Preparando para subir a GitHub..."

# Inicializar git si no está inicializado
if [ ! -d ".git" ]; then
    echo "Inicializando repositorio git..."
    git init
fi

# Agregar el remote
echo "Configurando repositorio remoto..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/686f6c61/linkedIN-Jobs-Scrapper.git

# Agregar todos los archivos
echo "Agregando archivos..."
git add .

# Crear commit
echo "Creando commit..."
git commit -m "🚀 Initial commit - LinkedIn Job Scraper v1.0.0

- Script interactivo en español
- Búsquedas predefinidas para España, USA y Reino Unido  
- Exportación a CSV
- Instalación automática con setup.sh
- API Key segura en .env
- Autor: Hex686f6c61"

# Push al repositorio
echo "Subiendo a GitHub..."
echo "Se te pedirá tu usuario y contraseña/token de GitHub"
git branch -M main
git push -u origin main

echo "✅ Proyecto subido exitosamente a GitHub!"
echo "🔗 URL: https://github.com/686f6c61/linkedIN-Jobs-Scrapper"