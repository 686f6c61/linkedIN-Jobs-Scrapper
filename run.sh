#!/bin/bash
# Script de ejecución rápida para Job Search LinkedIn

# Activar entorno virtual
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate 2>/dev/null || venv\\Scripts\\activate.bat
else
    source venv/bin/activate
fi

# Ejecutar script principal
python linkedin_job_scraper_interactive.py

# Desactivar entorno virtual
deactivate
