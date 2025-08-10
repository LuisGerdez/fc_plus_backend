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

python manage.py makemigrations --settings=fc_plus.settings.development
<br />
python manage.py migrate --settings=fc_plus.settings.development

Crear superusuario (opcional)
-----------------------------

Para acceder al panel de administración de Django:

python manage.py createsuperuser --settings=fc_plus.settings.development

Ejecutar el servidor
--------------------

Inicia el servidor de desarrollo:

python manage.py runserver --settings=fc_plus.settings.development

Por defecto estará disponible en:

http://127.0.0.1:8000/

Estructura del proyecto
-----------------------

COMING SOON

USO DE LOGIN JWT
-----------------------

LOGIN (Obtener access y refresh token)

curl -Method POST `
     -Uri "http://127.0.0.1:8000/auth/jwt/create/" `
     -ContentType "application/json" `
     -Body '{"username": "usuario1", "password": "Pass1234"}'

ejemplo: {"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NDg2MTQwMCwiaWF0IjoxNzU0Nzc1MDAwLCJqdGkiOiJiMDJhNTQ0NjZlYWE0M2ZkOTRjYzI1Mjc1NTI5OGUzMyIsInVzZXJfaWQiOiIxIn0.pshrbMa-IemgfYWjlBGcxQAO3AxnDXQay8Tpy5CeX1w","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0Nzc1MzAwLCJpYXQiOjE3NTQ3NzUwMDAsImp0aSI6ImIyNDdlOGU0NmJhZTRhZTc5NDc4N2I3ZTFkMzVkY2MzIiwidXNlcl9pZCI6IjEifQ.awS1m9K7ZEa0EWu96XaizUDgua_nD8UOImE-tboVjK4"}

USUARIO ACTUAL

curl -Method GET `
     -Uri "http://127.0.0.1:8000/auth/users/me/" `
     -Headers @{ "Authorization" = "JWT tokenaqui" }

REGISTRAR USUARIO

curl -Method POST `
     -Uri "http://127.0.0.1:8000/auth/users/" `
     -ContentType "application/json" `
     -Body '{"username": "usuario1", "password": "Passdsasdsdss1234", "email": "usuario1@example.com"}'