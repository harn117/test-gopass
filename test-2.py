import tarfile
import datetime
import os

def crear_backup_tgz(directorio_origen, directorio_destino):
    ahora = datetime.datetime.now()
    fecha_str = ahora.strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"usuario1_backup_{fecha_str}.tar.gz"
    ruta_archivo_destino = os.path.join(directorio_destino, nombre_archivo)

    try:
        with tarfile.open(ruta_archivo_destino, "w:gz") as archivo_tar:
            archivo_tar.add(directorio_origen, arcname=os.path.basename(directorio_origen))
        print(f"Backup creado exitosamente en: {ruta_archivo_destino}")
    except Exception as e:
        print(f"Ocurrió un error al crear el backup: {e}")

if __name__ == "__main__":
    directorio_respaldar = "/home/user/test"
    directorio_backup = "/home/user/test/backups"

    # Asegurarse de que el directorio de destino exista
    os.makedirs(directorio_backup, exist_ok=True)

    crear_backup_tgz(directorio_respaldar, directorio_backup)