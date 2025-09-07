#!/usr/bin/env python3
"""
LinkedIn Job Scraper Interactivo usando JSearch API de RapidAPI
Script en español con menú interactivo y ejemplos predefinidos
Autor: Hex686f6c61
Versión: 1.0.0
"""

import http.client
import json
import urllib.parse
from typing import Optional, List, Dict, Any
from datetime import datetime
import time
import csv
import os
import re
import sys

# Intentar cargar python-dotenv, si no está instalado, usar método alternativo
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  python-dotenv no está instalado. Intentando leer .env manualmente...")
    # Leer .env manualmente
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

class LinkedInJobScraper:
    """
    Clase para scrapear trabajos de LinkedIn usando JSearch API
    """
    
    def __init__(self, api_key: str):
        """
        Inicializa el scraper con la API key de RapidAPI
        
        Args:
            api_key: Tu clave de API de RapidAPI
        """
        self.api_key = api_key
        self.api_host = os.getenv('RAPIDAPI_HOST', 'jsearch.p.rapidapi.com')
        self.headers = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': self.api_host
        }
    
    def search_jobs(
        self,
        query: str,
        page: int = 1,
        num_pages: int = 1,
        country: str = "us",
        language: Optional[str] = None,
        date_posted: str = "all",
        work_from_home: bool = False,
        employment_types: Optional[str] = None,
        job_requirements: Optional[str] = None,
        radius: Optional[int] = None,
        exclude_job_publishers: Optional[str] = None,
        fields: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Busca trabajos usando la API de JSearch
        """
        
        # Construir los parámetros de la consulta
        params = {
            'query': query,
            'page': str(page),
            'num_pages': str(num_pages),
            'country': country,
            'date_posted': date_posted
        }
        
        # Agregar parámetros opcionales si están presentes
        if language:
            params['language'] = language
        if work_from_home:
            params['work_from_home'] = 'true'
        if employment_types:
            params['employment_types'] = employment_types
        if job_requirements:
            params['job_requirements'] = job_requirements
        if radius:
            params['radius'] = str(radius)
        if exclude_job_publishers:
            params['exclude_job_publishers'] = exclude_job_publishers
        if fields:
            params['fields'] = fields
        
        # Codificar los parámetros para la URL
        query_string = urllib.parse.urlencode(params)
        
        # Hacer la conexión HTTPS
        conn = http.client.HTTPSConnection(self.api_host)
        
        try:
            # Realizar la petición GET
            endpoint = f"/search?{query_string}"
            conn.request("GET", endpoint, headers=self.headers)
            
            # Obtener la respuesta
            response = conn.getresponse()
            data = response.read()
            
            # Decodificar y parsear JSON
            result = json.loads(data.decode("utf-8"))
            
            return result
            
        except Exception as e:
            print(f"❌ Error al hacer la petición: {e}")
            return {"error": str(e)}
        
        finally:
            # Cerrar la conexión
            conn.close()
    
    def parse_job_results(self, results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Parsea los resultados de la búsqueda para extraer información relevante
        """
        
        if "error" in results:
            print(f"❌ Error en los resultados: {results['error']}")
            return []
        
        jobs = []
        
        # Extraer los datos de los trabajos
        if "data" in results:
            for job in results.get("data", []):
                parsed_job = {
                    "job_id": job.get("job_id"),
                    "employer_name": job.get("employer_name"),
                    "employer_logo": job.get("employer_logo"),
                    "job_publisher": job.get("job_publisher"),
                    "job_employment_type": job.get("job_employment_type"),
                    "job_title": job.get("job_title"),
                    "job_apply_link": job.get("job_apply_link"),
                    "job_description": job.get("job_description"),
                    "job_is_remote": job.get("job_is_remote"),
                    "job_posted_at_timestamp": job.get("job_posted_at_timestamp"),
                    "job_posted_at_datetime": job.get("job_posted_at_datetime_utc"),
                    "job_city": job.get("job_city"),
                    "job_state": job.get("job_state"),
                    "job_country": job.get("job_country"),
                    "job_latitude": job.get("job_latitude"),
                    "job_longitude": job.get("job_longitude"),
                    "job_benefits": job.get("job_benefits"),
                    "job_google_link": job.get("job_google_link"),
                    "job_offer_expiration_datetime": job.get("job_offer_expiration_datetime_utc"),
                    "job_offer_expiration_timestamp": job.get("job_offer_expiration_timestamp"),
                    "job_required_experience": job.get("job_required_experience"),
                    "job_required_skills": job.get("job_required_skills"),
                    "job_required_education": job.get("job_required_education"),
                    "job_experience_in_place_of_education": job.get("job_experience_in_place_of_education"),
                    "job_min_salary": job.get("job_min_salary"),
                    "job_max_salary": job.get("job_max_salary"),
                    "job_salary_currency": job.get("job_salary_currency"),
                    "job_salary_period": job.get("job_salary_period"),
                    "job_highlights": job.get("job_highlights"),
                    "job_job_title": job.get("job_job_title")
                }
                jobs.append(parsed_job)
        
        return jobs
    
    def save_to_csv(self, jobs: List[Dict[str, Any]], query: str):
        """
        Guarda los trabajos en un archivo CSV en la carpeta output
        """
        
        # Crear carpeta output si no existe
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Limpiar el query para usarlo como nombre de archivo
        clean_query = re.sub(r'[^\w\s-]', '', query)
        clean_query = re.sub(r'[-\s]+', '_', clean_query)
        
        # Crear nombre de archivo con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/{clean_query}_{timestamp}.csv"
        
        try:
            # Definir las columnas para el CSV
            fieldnames = [
                'job_id',
                'job_title',
                'employer_name',
                'job_city',
                'job_state',
                'job_country',
                'job_is_remote',
                'job_employment_type',
                'job_min_salary',
                'job_max_salary',
                'job_salary_currency',
                'job_salary_period',
                'job_description',
                'job_apply_link',
                'job_posted_at_datetime',
                'job_publisher',
                'job_required_experience',
                'job_required_skills',
                'job_required_education',
                'job_benefits',
                'job_google_link',
                'job_offer_expiration_datetime'
            ]
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
                
                # Escribir encabezados
                writer.writeheader()
                
                # Escribir los datos de cada trabajo
                for job in jobs:
                    # Limpiar la descripción (remover saltos de línea excesivos)
                    if job.get('job_description'):
                        job['job_description'] = ' '.join(job['job_description'].split())[:500] + '...'
                    
                    # Convertir listas a strings
                    if job.get('job_required_skills') and isinstance(job['job_required_skills'], list):
                        job['job_required_skills'] = ', '.join(job['job_required_skills'])
                    
                    if job.get('job_benefits') and isinstance(job['job_benefits'], list):
                        job['job_benefits'] = ', '.join(job['job_benefits'])
                    
                    writer.writerow(job)
            
            print(f"\n✅ Trabajos guardados en CSV: {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ Error al guardar archivo CSV: {e}")
            return None
    
    def print_job_summary(self, jobs: List[Dict[str, Any]]):
        """
        Imprime un resumen de los trabajos encontrados
        """
        
        print(f"\n{'='*80}")
        print(f"📊 RESUMEN DE BÚSQUEDA - {len(jobs)} trabajos encontrados")
        print(f"{'='*80}\n")
        
        for i, job in enumerate(jobs, 1):
            print(f"🔹 Trabajo #{i}")
            print(f"   Título: {job.get('job_title', 'N/A')}")
            print(f"   Empresa: {job.get('employer_name', 'N/A')}")
            print(f"   Ubicación: {job.get('job_city', 'N/A')}, {job.get('job_state', 'N/A')}, {job.get('job_country', 'N/A')}")
            print(f"   Remoto: {'Sí' if job.get('job_is_remote') else 'No'}")
            print(f"   Tipo: {job.get('job_employment_type', 'N/A')}")
            
            # Mostrar salario si está disponible
            if job.get('job_min_salary') or job.get('job_max_salary'):
                salary_currency = job.get('job_salary_currency', 'USD')
                salary_period = job.get('job_salary_period', 'YEAR')
                min_sal = job.get('job_min_salary', 'N/A')
                max_sal = job.get('job_max_salary', 'N/A')
                print(f"   Salario: {min_sal} - {max_sal} {salary_currency}/{salary_period}")
            
            print(f"   Link: {job.get('job_apply_link', 'N/A')}")
            print(f"   Publicado: {job.get('job_posted_at_datetime', 'N/A')}")
            print("-" * 40)
        
        print(f"\n{'='*80}\n")


def mostrar_menu():
    """
    Muestra el menú principal en español
    """
    print("\n" + "="*80)
    print("🔍 LINKEDIN JOB SCRAPER - MENÚ PRINCIPAL")
    print("="*80)
    print("\n📋 OPCIONES DISPONIBLES:\n")
    print("1. 🔎 Búsqueda personalizada")
    print("2. 💼 Software Engineer - España")
    print("3. 📊 Data Scientist - España")
    print("4. 🎨 Frontend Developer - España")
    print("5. 📱 Backend Developer - USA")
    print("6. 🤖 Machine Learning Engineer - USA")
    print("7. 🌐 Full Stack Developer - USA")
    print("8. 📈 DevOps Engineer - Reino Unido")
    print("9. ☁️  Cloud Architect - Reino Unido")
    print("10. 🏗️ Senior Software Engineer - Remoto Global")
    print("\n0. ❌ Salir")
    print("\n" + "="*80)


def obtener_parametros_personalizados():
    """
    Obtiene los parámetros de búsqueda del usuario
    """
    print("\n🔧 CONFIGURACIÓN DE BÚSQUEDA PERSONALIZADA")
    print("-" * 50)
    
    query = input("\n📝 Ingresa tu búsqueda (ej: 'python developer madrid'): ").strip()
    if not query:
        print("❌ La búsqueda no puede estar vacía")
        return None
    
    print("\n🌍 Código de país (deja vacío para USA):")
    print("   Ejemplos: mx=México, es=España, ar=Argentina, co=Colombia, cl=Chile")
    country = input("   País: ").strip() or "us"
    
    print("\n📅 Período de publicación:")
    print("   1. Todos")
    print("   2. Hoy")
    print("   3. Últimos 3 días")
    print("   4. Última semana")
    print("   5. Último mes")
    periodo_opcion = input("   Selecciona (1-5): ").strip()
    
    periodos = {
        "1": "all",
        "2": "today",
        "3": "3days",
        "4": "week",
        "5": "month"
    }
    date_posted = periodos.get(periodo_opcion, "all")
    
    remote = input("\n🏠 ¿Solo trabajos remotos? (s/n): ").strip().lower() == 's'
    
    print("\n💼 Tipo de empleo (deja vacío para todos):")
    print("   Opciones: FULLTIME, CONTRACTOR, PARTTIME, INTERN")
    print("   Puedes combinar varios separados por comas")
    employment_types = input("   Tipo: ").strip() or None
    
    num_pages = input("\n📄 Número de páginas a buscar (1-10, default=1): ").strip()
    try:
        num_pages = int(num_pages) if num_pages else 1
        num_pages = min(max(num_pages, 1), 10)
    except:
        num_pages = 1
    
    return {
        "query": query,
        "country": country,
        "date_posted": date_posted,
        "work_from_home": remote,
        "employment_types": employment_types,
        "num_pages": num_pages
    }


def ejecutar_busqueda_predefinida(scraper, opcion):
    """
    Ejecuta una búsqueda predefinida según la opción seleccionada
    """
    busquedas = {
        "2": {
            "query": "software engineer",
            "country": "es",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Software Engineer en España"
        },
        "3": {
            "query": "data scientist python machine learning",
            "country": "es",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Data Scientist en España"
        },
        "4": {
            "query": "frontend developer react javascript",
            "country": "es",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Frontend Developer en España"
        },
        "5": {
            "query": "backend developer python java",
            "country": "us",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Backend Developer en USA"
        },
        "6": {
            "query": "machine learning engineer tensorflow pytorch",
            "country": "us",
            "employment_types": "FULLTIME",
            "date_posted": "3days",
            "titulo": "Machine Learning Engineer en USA"
        },
        "7": {
            "query": "full stack developer node react python",
            "country": "us",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Full Stack Developer en USA"
        },
        "8": {
            "query": "devops engineer kubernetes docker aws",
            "country": "gb",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "DevOps Engineer en Reino Unido"
        },
        "9": {
            "query": "cloud architect aws azure gcp",
            "country": "gb",
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Cloud Architect en Reino Unido"
        },
        "10": {
            "query": "senior software engineer remote",
            "work_from_home": True,
            "employment_types": "FULLTIME",
            "date_posted": "week",
            "titulo": "Senior Software Engineer - Remoto Global"
        }
    }
    
    if opcion not in busquedas:
        return False
    
    params = busquedas[opcion]
    titulo = params.pop("titulo")
    
    print(f"\n🔍 Ejecutando búsqueda: {titulo}")
    print("⏳ Por favor espera...")
    
    # Ejecutar búsqueda
    results = scraper.search_jobs(
        query=params.get("query"),
        country=params.get("country", "us"),
        date_posted=params.get("date_posted", "all"),
        work_from_home=params.get("work_from_home", False),
        employment_types=params.get("employment_types"),
        num_pages=1
    )
    
    # Parsear y mostrar resultados
    jobs = scraper.parse_job_results(results)
    
    if jobs:
        scraper.print_job_summary(jobs)
        scraper.save_to_csv(jobs, params.get("query"))
        print(f"\n✅ Se encontraron {len(jobs)} trabajos")
    else:
        print("\n⚠️  No se encontraron trabajos con estos criterios")
    
    return True


def main():
    """
    Función principal del programa interactivo
    """
    
    print("\n" + "="*80)
    print("🚀 LINKEDIN JOB SCRAPER - VERSIÓN INTERACTIVA")
    print("="*80)
    
    # Verificar y cargar API key
    api_key = os.getenv('RAPIDAPI_KEY')
    
    if not api_key or api_key == 'TU_API_KEY_AQUI':
        print("\n❌ ERROR: No se encontró la API Key")
        print("\n📝 INSTRUCCIONES:")
        print("1. Copia el archivo .env.example y renómbralo a .env")
        print("2. Abre el archivo .env y reemplaza 'TU_API_KEY_AQUI' con tu clave real")
        print("3. Obtén tu API key en: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch")
        print("4. Vuelve a ejecutar este script")
        return
    
    # Crear instancia del scraper
    scraper = LinkedInJobScraper(api_key)
    
    print("\n✅ API Key cargada correctamente")
    print(f"🔗 Conectado a: {scraper.api_host}")
    
    while True:
        mostrar_menu()
        
        opcion = input("\n👉 Selecciona una opción (0-10): ").strip()
        
        if opcion == "0":
            print("\n👋 ¡Hasta luego! Gracias por usar LinkedIn Job Scraper")
            break
        
        elif opcion == "1":
            # Búsqueda personalizada
            params = obtener_parametros_personalizados()
            if params:
                print("\n⏳ Ejecutando búsqueda personalizada...")
                
                results = scraper.search_jobs(**params)
                jobs = scraper.parse_job_results(results)
                
                if jobs:
                    scraper.print_job_summary(jobs)
                    scraper.save_to_csv(jobs, params['query'])
                    print(f"\n✅ Se encontraron {len(jobs)} trabajos")
                else:
                    print("\n⚠️  No se encontraron trabajos con estos criterios")
        
        elif opcion in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            # Búsquedas predefinidas
            ejecutar_busqueda_predefinida(scraper, opcion)
        
        else:
            print("\n❌ Opción no válida. Por favor selecciona entre 0 y 10")
        
        input("\n🔄 Presiona ENTER para continuar...")


if __name__ == "__main__":
    """
    Punto de entrada del script
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
        print("👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor verifica tu conexión a internet y tu API key")