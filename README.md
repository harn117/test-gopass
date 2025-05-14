# test-gopass
Prueba tecnica para goopass

# Python 
Intalacion y puesta en marcha (test-1.py)

  Linux
  - python3 --version
  - python3 /carpeta_contenedora/archivo.py
  - El resultado se vera por consola

# Postgres

  - Para la instalacion de postgres se utilizo docker para generar un contenedor y la instancia de postgres.
          - comando para doceker -- docker-compose up -d --
  - Se deja el scrip en el archivo postgres.sql con los comandos para la creacion y consultas definidas.
  - Se deja el archivo test-pg.py con el codigo para la creacion de usuario y listado de los mismos.

# Linux Terminal

  Comando para revisar los 5 procesos que mas memoria consumen 
  - top -b -n 1 | head -n 12  | tail -n 5
  - watch "ps aux | sort -nrk 3,3 | head -n 5"

  Crear usuario y asignar password
  - sudo useradd -m nuevo_usuario
  - sudo passwd nuevo_usuario

  Cambiar permisos para que solo se pueda leer y escribir por el porpietario
  - chmod 600 /carpeta_contenedora/nombre del archivo

  Ver el estdo del protocolo ssh
  - sudo systemctl status sshd
