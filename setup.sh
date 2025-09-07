#!/bin/bash

#############################################################################
#                                                                           #
#                    🔍 Job Search LinkedIn - Setup Script                 #
#                                                                           #
#   Script de instalación automática para LinkedIn Job Scraper             #
#   Autor: Hex686f6c61                                                     #
#   Versión: 1.0.0                                                        #
#                                                                           #
#############################################################################

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner de inicio
print_banner() {
    echo
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                                                            ║${NC}"
    echo -e "${CYAN}║${MAGENTA}        🔍 Job Search LinkedIn - Instalador${CYAN}                ║${NC}"
    echo -e "${CYAN}║${NC}        Busca trabajos en LinkedIn fácilmente${CYAN}              ║${NC}"
    echo -e "${CYAN}║                                                            ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo
}

# Función para imprimir mensajes con formato
print_step() {
    echo -e "${BLUE}[→]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Verificar sistema operativo
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
}

# Verificar Python
check_python() {
    print_step "Verificando instalación de Python..."
    
    # Intentar con python3 primero
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Python $PYTHON_VERSION encontrado"
    # Luego con python
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        
        # Verificar que sea Python 3
        if [[ $PYTHON_VERSION == 3.* ]]; then
            print_success "Python $PYTHON_VERSION encontrado"
        else
            print_error "Python 2 detectado. Se requiere Python 3.6+"
            echo -e "${YELLOW}Instala Python 3 desde: https://www.python.org/downloads/${NC}"
            exit 1
        fi
    else
        print_error "Python no está instalado"
        echo -e "${YELLOW}Instala Python desde: https://www.python.org/downloads/${NC}"
        exit 1
    fi
}

# Verificar pip
check_pip() {
    print_step "Verificando pip..."
    
    if ! $PYTHON_CMD -m pip --version &> /dev/null; then
        print_warning "pip no encontrado. Intentando instalar..."
        
        if [[ "$OS" == "macos" ]]; then
            $PYTHON_CMD -m ensurepip --default-pip
        elif [[ "$OS" == "linux" ]]; then
            sudo apt-get update && sudo apt-get install python3-pip -y 2>/dev/null || \
            sudo yum install python3-pip -y 2>/dev/null || \
            print_error "No se pudo instalar pip automáticamente"
        fi
    else
        print_success "pip está instalado"
    fi
}

# Crear entorno virtual
create_venv() {
    print_step "Creando entorno virtual..."
    
    if [ -d "venv" ]; then
        print_warning "El entorno virtual ya existe"
        read -p "¿Deseas recrearlo? (s/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
            rm -rf venv
            $PYTHON_CMD -m venv venv
            print_success "Entorno virtual recreado"
        else
            print_success "Usando entorno virtual existente"
        fi
    else
        $PYTHON_CMD -m venv venv
        print_success "Entorno virtual creado"
    fi
}

# Activar entorno virtual e instalar dependencias
install_dependencies() {
    print_step "Instalando dependencias..."
    
    # Activar venv según el OS
    if [[ "$OS" == "windows" ]]; then
        source venv/Scripts/activate 2>/dev/null || venv\\Scripts\\activate.bat
    else
        source venv/bin/activate
    fi
    
    # Actualizar pip
    pip install --upgrade pip --quiet
    
    # Instalar dependencias
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt --quiet
        print_success "Dependencias instaladas"
    else
        print_warning "requirements.txt no encontrado. Instalando python-dotenv manualmente..."
        pip install python-dotenv --quiet
        print_success "python-dotenv instalado"
    fi
}

# Configurar archivo .env
setup_env() {
    print_step "Configurando archivo .env..."
    
    if [ -f ".env" ]; then
        print_warning "El archivo .env ya existe"
        read -p "¿Deseas reconfigurarlo? (s/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Ss]$ ]]; then
            print_success "Manteniendo configuración existente"
            return
        fi
    fi
    
    # Copiar desde .env.example si existe
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_success "Archivo .env creado desde plantilla"
    else
        # Crear .env básico
        cat > .env << EOF
# Configuración de API para LinkedIn Job Scraper
# IMPORTANTE: Mantén este archivo seguro y no lo subas a Git

# Tu API Key de RapidAPI para JSearch
RAPIDAPI_KEY=TU_API_KEY_AQUI

# Host de la API (no cambiar)
RAPIDAPI_HOST=jsearch.p.rapidapi.com
EOF
        print_success "Archivo .env creado"
    fi
    
    echo
    print_warning "IMPORTANTE: Necesitas configurar tu API Key"
    echo -e "${YELLOW}1. Ve a: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch${NC}"
    echo -e "${YELLOW}2. Regístrate/Inicia sesión y suscríbete al plan gratuito${NC}"
    echo -e "${YELLOW}3. Copia tu API Key${NC}"
    echo
    
    read -p "¿Tienes tu API Key lista? (s/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        read -p "Ingresa tu API Key: " api_key
        
        if [ ! -z "$api_key" ]; then
            # Reemplazar en el archivo .env
            if [[ "$OS" == "macos" ]]; then
                sed -i '' "s/TU_API_KEY_AQUI/$api_key/g" .env
            else
                sed -i "s/TU_API_KEY_AQUI/$api_key/g" .env
            fi
            print_success "API Key configurada"
        else
            print_warning "No se ingresó API Key. Configúrala manualmente en .env"
        fi
    else
        print_warning "Recuerda configurar tu API Key en el archivo .env antes de usar el script"
    fi
}

# Crear carpeta output
create_output_folder() {
    print_step "Creando carpeta para resultados..."
    
    if [ ! -d "output" ]; then
        mkdir -p output
        print_success "Carpeta 'output' creada"
    else
        print_success "Carpeta 'output' ya existe"
    fi
}

# Verificar instalación
verify_installation() {
    print_step "Verificando instalación..."
    
    # Activar venv
    if [[ "$OS" == "windows" ]]; then
        source venv/Scripts/activate 2>/dev/null || venv\\Scripts\\activate.bat
    else
        source venv/bin/activate
    fi
    
    # Verificar si el script principal existe
    if [ -f "linkedin_job_scraper_interactive.py" ]; then
        print_success "Script principal encontrado"
    else
        print_error "Script principal no encontrado"
        exit 1
    fi
    
    # Verificar importación de módulos
    $PYTHON_CMD -c "import http.client, json, csv, os" 2>/dev/null
    if [ $? -eq 0 ]; then
        print_success "Módulos estándar verificados"
    else
        print_error "Error al verificar módulos"
        exit 1
    fi
    
    # Verificar .env
    if [ -f ".env" ]; then
        if grep -q "TU_API_KEY_AQUI" .env; then
            print_warning "API Key aún no configurada en .env"
        else
            print_success "Configuración completa"
        fi
    fi
}

# Crear script de ejecución
create_run_script() {
    print_step "Creando script de ejecución rápida..."
    
    # Script para Unix
    cat > run.sh << 'EOF'
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
EOF
    
    chmod +x run.sh
    
    # Script para Windows
    cat > run.bat << 'EOF'
@echo off
REM Script de ejecución rápida para Job Search LinkedIn

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Ejecutar script principal
python linkedin_job_scraper_interactive.py

REM Desactivar entorno virtual
deactivate
EOF
    
    print_success "Scripts de ejecución creados (run.sh y run.bat)"
}

# Mostrar instrucciones finales
show_instructions() {
    echo
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║            🎉 ¡Instalación Completada!                     ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo
    echo -e "${CYAN}Para usar Job Search LinkedIn:${NC}"
    echo
    echo -e "${YELLOW}Opción 1: Usar script de ejecución rápida${NC}"
    echo -e "  ${GREEN}./run.sh${NC}           (Linux/macOS)"
    echo -e "  ${GREEN}run.bat${NC}            (Windows)"
    echo
    echo -e "${YELLOW}Opción 2: Ejecutar manualmente${NC}"
    echo -e "  ${GREEN}source venv/bin/activate${NC}    (Linux/macOS)"
    echo -e "  ${GREEN}venv\\Scripts\\activate.bat${NC}   (Windows)"
    echo -e "  ${GREEN}python linkedin_job_scraper_interactive.py${NC}"
    echo
    
    if grep -q "TU_API_KEY_AQUI" .env 2>/dev/null; then
        echo -e "${RED}⚠️  IMPORTANTE: No olvides configurar tu API Key en .env${NC}"
        echo -e "${YELLOW}   Edita el archivo .env y reemplaza TU_API_KEY_AQUI${NC}"
    fi
    
    echo
    echo -e "${CYAN}Documentación completa en README.md${NC}"
    echo -e "${CYAN}¡Feliz búsqueda de empleo! 🚀${NC}"
    echo
}

# Función principal
main() {
    clear
    print_banner
    
    # Detectar OS
    detect_os
    print_success "Sistema operativo: $OS"
    
    # Verificaciones
    check_python
    check_pip
    
    # Instalación
    create_venv
    install_dependencies
    setup_env
    create_output_folder
    create_run_script
    
    # Verificación final
    verify_installation
    
    # Mostrar instrucciones
    show_instructions
}

# Manejo de errores
trap 'print_error "Error durante la instalación. Verifica los mensajes anteriores."; exit 1' ERR

# Ejecutar
main