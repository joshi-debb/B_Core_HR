
# para crear entorno virtual

python -m venv venv

# para correr entorno vitual

.\venv\Scripts\Activate


# para habilitar powershell

Set-ExecutionPolicy RemoteSigned

# para instalar librerias en el entorno vitual

pip install <nombre_de_la_libreria>

# para crear el archivo requirements.txt

pip freeze > requirements.txt

# para instalar dependencias desde requirements.txt

pip install -r requirements.txt

# para ejecutar la app

python -m src.main

# libreria para generar los .exe

pip install pyinstaller

# para generar el ejecutable

pyinstaller --onefile --windowed src/main.py

