# 🔍 LinkedIn Job Scraper con RapidAPI

Script interactivo en español para buscar trabajos de LinkedIn usando la API JSearch de RapidAPI. Permite búsquedas personalizadas y predefinidas con exportación a CSV.

**Autor:** Hex686f6c61  
**Versión:** 1.0.0

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Opciones de Búsqueda](#-opciones-de-búsqueda)
- [Ejemplos de Queries](#-ejemplos-de-queries)
- [Parámetros Disponibles](#-parámetros-disponibles)
- [Estructura de Archivos](#-estructura-de-archivos)
- [Solución de Problemas](#-solución-de-problemas)

## 🚀 Características

- ✅ **Menú interactivo en español** con 10 búsquedas predefinidas
- 🔐 **API Key segura** almacenada en archivo `.env`
- 📊 **Exportación a CSV** con nombres descriptivos
- 🌍 **Búsquedas por país** (México, España, Argentina, etc.)
- 🏠 **Filtro de trabajos remotos**
- 💼 **Filtros por tipo de empleo** (Tiempo completo, parcial, contratista, etc.)
- 📅 **Filtros por fecha de publicación**
- 📁 **Organización automática** en carpeta `output/`

## 📋 Requisitos

- **Python 3.6** o superior
- **Cuenta en RapidAPI** (gratuita o de pago)
- **API Key de JSearch** ([Obtener aquí](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch))

## 🔧 Instalación

### Instalación Automática (Recomendado)

Usa el script de instalación automática:

```bash
# Linux/macOS
chmod +x setup.sh
./setup.sh

# Windows (Git Bash)
bash setup.sh
```

El script automáticamente:
- ✅ Verifica Python y pip
- ✅ Crea el entorno virtual
- ✅ Instala dependencias
- ✅ Configura el archivo .env
- ✅ Crea scripts de ejecución rápida
- ✅ Verifica la instalación

### Instalación Manual

Si prefieres instalar manualmente:

#### 1. Clonar o descargar el proyecto

```bash
# Opción A: Clonar con git
git clone <tu-repositorio>
cd "SCRAPPER Jobs"

# Opción B: Descargar ZIP
# Descarga los archivos y descomprime en una carpeta
```

### 2. Crear entorno virtual (recomendado)

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto:

#### En macOS/Linux:

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Verificar que está activado (deberías ver (venv) en tu terminal)
which python
# Debería mostrar: /tu/ruta/SCRAPPER Jobs/venv/bin/python
```

#### En Windows:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Command Prompt:
venv\Scripts\activate.bat

# En PowerShell:
venv\Scripts\Activate.ps1

# Si hay error en PowerShell, ejecuta primero:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Instalar dependencias

Con el entorno virtual activado:

```bash
# Instalar desde requirements.txt
python -m pip install -r requirements.txt

# O instalar manualmente
python -m pip install python-dotenv

# Verificar instalación
pip list
```

**Nota:** El script puede funcionar sin `python-dotenv` ya que incluye un método alternativo para leer el archivo `.env`, pero se recomienda instalarlo.

### 4. Configurar la API Key

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# En Windows:
copy .env.example .env

# Editar .env con tu editor favorito
# macOS/Linux:
nano .env
# o
vim .env

# Windows:
notepad .env
```

Reemplaza `TU_API_KEY_AQUI` con tu clave real de RapidAPI:

```env
# Tu API Key de RapidAPI para JSearch
RAPIDAPI_KEY=TU_API_KEY_AQUI

# Host de la API (no cambiar)
RAPIDAPI_HOST=jsearch.p.rapidapi.com
```

### 5. Obtener API Key de RapidAPI

1. Ve a [RapidAPI JSearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)
2. Haz clic en "Subscribe to Test" o "Pricing"
3. Selecciona un plan (hay plan gratuito con 500 búsquedas/mes)
4. Crea una cuenta o inicia sesión
5. Copia tu API Key desde el dashboard
6. Pégala en tu archivo `.env`

### 6. Verificar instalación

```bash
# Ejecutar script de prueba
python test_script.py

# Si todo está bien, verás:
# ✅ API Key cargada correctamente
# 🔍 Ejecutando búsqueda de prueba...
```

### Desactivar entorno virtual

Cuando termines de usar el script:

```bash
# Desactivar el entorno virtual
deactivate
```

### Estructura después de la instalación

```
SCRAPPER Jobs/
├── venv/                                # Entorno virtual (no subir a git)
├── output/                              # Carpeta para CSVs (se crea automáticamente)
├── .env                                 # Tu API key (no subir a git)
├── .env.example                         # Plantilla de configuración
├── .gitignore                          # Ignora venv y .env
├── linkedin_job_scraper_interactive.py # Script principal
├── setup.sh                            # Script de instalación automática
├── run.sh                              # Script de ejecución rápida (creado por setup.sh)
├── run.bat                             # Script de ejecución Windows (creado por setup.sh)
├── requirements.txt                    # Dependencias
├── test_script.py                      # Script de prueba
└── README.md                           # Este archivo
```

## 💻 Uso

### Opción 1: Usar los scripts de ejecución rápida (Más fácil)

Si usaste `setup.sh`, se crearon scripts de ejecución:

```bash
# Linux/macOS
./run.sh

# Windows
run.bat
```

Estos scripts automáticamente activan el entorno virtual, ejecutan el programa y lo desactivan al finalizar.

### Opción 2: Ejecutar manualmente

Con el entorno virtual activado:

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows

# Ejecutar el script principal
python linkedin_job_scraper_interactive.py

# Desactivar al terminar
deactivate
```

### Menú Principal

Al ejecutar el script verás:

```
================================================================================
🔍 LINKEDIN JOB SCRAPER - MENÚ PRINCIPAL
================================================================================

📋 OPCIONES DISPONIBLES:

1. 🔎 Búsqueda personalizada
2. 💼 Software Engineer - España
3. 📊 Data Scientist - España
4. 🎨 Frontend Developer - España
5. 📱 Backend Developer - USA
6. 🤖 Machine Learning Engineer - USA
7. 🌐 Full Stack Developer - USA
8. 📈 DevOps Engineer - Reino Unido
9. ☁️  Cloud Architect - Reino Unido
10. 🏗️ Senior Software Engineer - Remoto Global

0. ❌ Salir
```

### Opción 1: Búsqueda Personalizada

Al seleccionar la opción 1, podrás configurar:

- **Query de búsqueda**: Tu consulta personalizada
- **País**: Código de país (mx, es, ar, co, cl, etc.)
- **Período**: Todos, hoy, 3 días, semana, mes
- **Solo remotos**: Sí/No
- **Tipo de empleo**: FULLTIME, CONTRACTOR, PARTTIME, INTERN
- **Número de páginas**: 1-10 (más páginas = más resultados)

### Opciones 2-10: Búsquedas Predefinidas

Búsquedas optimizadas para España, USA y Reino Unido con los roles más demandados en tech.

## 🔍 Ejemplos de Queries

### Cómo Escribir Búsquedas Efectivas

#### Para España 🇪🇸

```python
# Búsquedas básicas
"software engineer madrid"
"desarrollador python barcelona"
"frontend developer valencia"

# Con tecnologías específicas
"backend developer java spring madrid"
"react developer typescript barcelona"
"python django developer spain remote"

# Con nivel de experiencia
"senior software engineer madrid"
"junior developer barcelona"
"lead engineer spain"

# Empresas específicas
"software engineer at inditex"
"developer at banco santander"
"data scientist at telefonica"
```

#### Para USA 🇺🇸

```python
# Ciudades principales
"software engineer san francisco"
"python developer new york"
"full stack developer seattle"
"backend engineer austin"

# Tecnologías populares
"react native developer silicon valley"
"machine learning engineer python tensorflow"
"devops engineer aws kubernetes"
"blockchain developer solidity"

# Empresas FAANG y unicornios
"software engineer at google"
"developer at meta facebook"
"engineer at apple"
"developer at stripe"
"software engineer at uber"
```

#### Para Reino Unido 🇬🇧

```python
# Ubicaciones principales
"software developer london"
"python engineer manchester"
"data scientist edinburgh"
"full stack developer cambridge"

# Sector financiero (muy demandado)
"python developer fintech london"
"quantitative developer city of london"
"java developer investment banking"

# Startups y scale-ups
"senior engineer at revolut"
"developer at monzo"
"software engineer at deliveroo"
```

### Queries Avanzadas y Combinaciones

```python
# Trabajo remoto con tecnologías específicas
"remote python developer django rest framework"
"work from home react typescript developer"
"telecommute senior backend engineer"

# Múltiples tecnologías (aumenta resultados)
"python OR java backend developer"
"react OR angular OR vue frontend"
"aws OR azure OR gcp cloud engineer"

# Excluir términos (usar con cuidado)
"software engineer NOT junior"
"developer NOT intern"

# Combinaciones complejas para España
"senior fullstack developer node react madrid remote"
"machine learning engineer python pytorch barcelona hybrid"

# Combinaciones para USA
"staff engineer distributed systems san francisco"
"principal software engineer golang kubernetes seattle"

# Combinaciones para UK
"lead developer python django fintech london"
"senior cloud architect aws terraform manchester remote"
```

### Tips para Mejores Búsquedas

1. **En español vs inglés**:
   - España: Prueba ambos idiomas ("desarrollador" y "developer")
   - USA/UK: Siempre en inglés

2. **Incluye tecnologías clave**:
   - Aumenta la precisión de resultados
   - Ejemplo: "python developer" vs "python django postgresql developer"

3. **Ubicación específica vs país**:
   - Ciudad específica: "software engineer barcelona"
   - Todo el país: "software engineer spain"
   - Remoto: añade "remote" o "work from home"

4. **Nivel de experiencia**:
   - Junior / Entry level / Graduate
   - Mid-level / Intermediate
   - Senior / Lead / Principal / Staff

5. **Tipo de empresa**:
   - Startup / Scale-up
   - Enterprise / Corporate
   - Fintech / Healthtech / Edtech
   - FAANG / Big Tech

## 🎯 Parámetros Disponibles

### Países Soportados (Principales)

| Código | País | Notas |
|--------|------|-------|
| `es` | 🇪🇸 España | Búsquedas en español e inglés |
| `us` | 🇺🇸 Estados Unidos | Mayor volumen de ofertas |
| `gb` | 🇬🇧 Reino Unido | Muchas ofertas en fintech |
| `de` | 🇩🇪 Alemania | Tech hubs: Berlín, Múnich |
| `fr` | 🇫🇷 Francia | París principal hub tech |
| `nl` | 🇳🇱 Países Bajos | Amsterdam hub de startups |
| `ie` | 🇮🇪 Irlanda | Sede europea de big tech |
| `ca` | 🇨🇦 Canadá | Toronto, Vancouver tech hubs |
| `au` | 🇦🇺 Australia | Sydney, Melbourne |
| `ch` | 🇨🇭 Suiza | Salarios muy altos |
| `se` | 🇸🇪 Suecia | Estocolmo: gaming y fintech |
| `no` | 🇳🇴 Noruega | Sector tech en crecimiento |

#### Países Latinoamericanos

| Código | País |
|--------|------|
| `mx` | 🇲🇽 México |
| `ar` | 🇦🇷 Argentina |
| `co` | 🇨🇴 Colombia |
| `cl` | 🇨🇱 Chile |
| `br` | 🇧🇷 Brasil |
| `pe` | 🇵🇪 Perú |
| `uy` | 🇺🇾 Uruguay |

[Ver lista completa de códigos ISO](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

### Tipos de Empleo

- `FULLTIME` - Tiempo completo
- `CONTRACTOR` - Contratista/Freelance
- `PARTTIME` - Tiempo parcial
- `INTERN` - Prácticas/Pasantías

**Nota:** Puedes combinar varios tipos separados por comas: `"FULLTIME,CONTRACTOR"`

### Períodos de Publicación

- `all` - Todos los trabajos
- `today` - Publicados hoy
- `3days` - Últimos 3 días
- `week` - Última semana
- `month` - Último mes

### Requisitos de Experiencia

- `under_3_years_experience` - Menos de 3 años
- `more_than_3_years_experience` - Más de 3 años
- `no_experience` - Sin experiencia
- `no_degree` - Sin título universitario

## 📁 Estructura de Archivos

```
SCRAPPER Jobs/
├── linkedin_job_scraper_interactive.py  # Script principal
├── .env                                  # Tu API key (no subir a Git)
├── .env.example                         # Plantilla de configuración
├── .gitignore                          # Ignora archivos sensibles
├── requirements.txt                    # Dependencias Python
├── README.md                          # Este archivo
├── test_script.py                     # Script de prueba rápida
└── output/                           # Carpeta con resultados CSV
    ├── python_developer_mexico_*.csv
    ├── data_scientist_españa_*.csv
    └── ...
```

## 📊 Estructura del CSV de Salida

Los archivos CSV incluyen las siguientes columnas:

- `job_id` - ID único del trabajo
- `job_title` - Título del puesto
- `employer_name` - Nombre de la empresa
- `job_city` - Ciudad
- `job_state` - Estado/Provincia
- `job_country` - País
- `job_is_remote` - Si es remoto (True/False)
- `job_employment_type` - Tipo de empleo
- `job_min_salary` - Salario mínimo
- `job_max_salary` - Salario máximo
- `job_salary_currency` - Moneda
- `job_salary_period` - Período (YEAR/MONTH/HOUR)
- `job_description` - Descripción (truncada a 500 caracteres)
- `job_apply_link` - Link para aplicar
- `job_posted_at_datetime` - Fecha de publicación
- Y más campos disponibles...

## 🚀 Guía Rápida (Quick Start)

Para usuarios con experiencia que quieren empezar rápido:

```bash
# 1. Clonar y entrar al directorio
git clone <repo> && cd "SCRAPPER Jobs"

# 2. Crear y activar entorno virtual
python3 -m venv venv && source venv/bin/activate  # macOS/Linux
python -m venv venv && venv\Scripts\activate.bat   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar API key
cp .env.example .env
# Editar .env y añadir tu API key de RapidAPI

# 5. Ejecutar
python linkedin_job_scraper_interactive.py
```

## 🛠 Solución de Problemas

### Error: "API Key no configurada"

```bash
# Verificar que .env existe
ls -la .env

# Ver contenido (cuidado de no compartir la key)
cat .env

# Asegurarse de que no hay espacios extras
# Correcto: RAPIDAPI_KEY=abc123
# Incorrecto: RAPIDAPI_KEY = abc123
```

### Error: "ModuleNotFoundError: No module named 'dotenv'"

```bash
# Asegúrate de tener el entorno virtual activado
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat  # Windows

# Reinstalar dependencias
pip install python-dotenv
```

### Error: "No se encontraron trabajos"

- Prueba con una búsqueda más general
- Verifica el código del país (es, us, gb)
- Intenta con un período de tiempo más amplio (month en vez de week)
- Algunos países tienen menos ofertas publicadas

### Error: "Permission denied" al activar venv en macOS/Linux

```bash
# Dar permisos de ejecución
chmod +x venv/bin/activate

# Luego activar
source venv/bin/activate
```

### Error en Windows PowerShell

```powershell
# Si no puedes ejecutar el script de activación:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego intenta de nuevo
venv\Scripts\Activate.ps1
```

### Error de conexión o timeout

- Verifica tu conexión a internet
- Confirma que tu API key es válida en RapidAPI
- Revisa si no has excedido el límite de tu plan
- Intenta con menos páginas (num_pages=1)

### Límites de la API

- **Plan gratuito**: 500 peticiones/mes
- **Múltiples páginas**: Búsquedas >1 página cuestan créditos extra
- **Rate limiting**: Espera 2 segundos entre búsquedas
- **Verificar uso**: Revisa tu dashboard en RapidAPI

## 💡 Tips para Mejores Resultados

1. **Sé específico**: "python backend developer django" > "developer"
2. **Incluye ubicación**: Ayuda a filtrar resultados relevantes
3. **Usa inglés para búsquedas globales**: Más resultados en empresas internacionales
4. **Combina filtros**: Remoto + Tipo de empleo + Fecha = resultados precisos
5. **Revisa diferentes períodos**: Los trabajos nuevos aparecen constantemente

## 🔒 Seguridad

- **Nunca** subas tu archivo `.env` a Git
- **No compartas** tu API key públicamente
- El `.gitignore` está configurado para proteger archivos sensibles

## 📝 Notas Importantes

- Los resultados dependen de lo que Google Jobs indexa
- No todos los trabajos muestran información salarial
- La información de "remoto" puede no ser 100% precisa
- Algunos trabajos pueden aparecer en múltiples búsquedas

## 🤝 Contribuciones

Si encuentras bugs o tienes sugerencias, siéntete libre de:
1. Abrir un issue
2. Enviar un pull request
3. Sugerir nuevas búsquedas predefinidas

## 👨‍💻 Autor

**Hex686f6c61**

## 📄 Licencia

Uso libre con fines educativos y personales.

---

**¿Necesitas ayuda?** Revisa primero la sección de [Solución de Problemas](#-solución-de-problemas) o abre un issue.