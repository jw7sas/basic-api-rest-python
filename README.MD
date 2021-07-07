# Instalar el ambiente virtual
pip install virtualenv==20.2.2
virtualenv venv

# Activar el entorno virtual en Windows
-- cd venv/Scripts
activate

# Agregamos las dependencias al archivo de requerimientos y ejecutamos el comandos - archivo en la raíz del proyecto 
-- cd ../../
pip install -r requirements.txt

# Correr al app en desarrollo
set FLASK_ENV=development
py main.py

# Links de ayuda donde me base para el proyecto
https://parzibyte.me/blog/2020/11/10/api-rest-python-flask-sqlite3/