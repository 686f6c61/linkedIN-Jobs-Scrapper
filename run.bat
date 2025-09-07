@echo off
REM Script de ejecución rápida para Job Search LinkedIn

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Ejecutar script principal
python linkedin_job_scraper_interactive.py

REM Desactivar entorno virtual
deactivate
