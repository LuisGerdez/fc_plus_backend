Requisitos previos
------------------

Antes de comenzar, asegúrate de tener instalado:

- Python 3.10+
- pip
- virtualenv

Instalación
-----------

1. Clonar el repositorio

   git clone https://github.com/LuisGerdez/football-management
   cd football-management

2. Crear y activar un entorno virtual

   # En Windows
   python -m venv venv
   venv\\Scripts\\activate

   # En Mac / Linux
   python3 -m venv venv
   source venv/bin/activate

3. Instalar dependencias

   pip install -r requirements.txt

Migraciones de base de datos
----------------------------

Ejecuta las migraciones para preparar la base de datos:

python manage.py makemigrations --settings=football_management.settings.development
python manage.py migrate --settings=football_management.settings.development

Crear superusuario (opcional)
-----------------------------

Para acceder al panel de administración de Django:

python manage.py createsuperuser --settings=football_management.settings.development

Ejecutar el servidor
--------------------

Inicia el servidor de desarrollo:

python manage.py runserver --settings=football_management.settings.development

Por defecto estará disponible en:

http://127.0.0.1:8000/

Estructura del proyecto
-----------------------

COMING SOON