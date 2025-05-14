import os
from datetime import datetime

# 1. Crear carpeta reportes/ si no existe
if not os.path.exists('reportes'):
    os.makedirs('reportes')

# 2. Generar nombre de archivo con fecha
fecha_actual = datetime.now().strftime('%Y%m%d')
nombre_reporte = f'reportes/reporte_{fecha_actual}.txt'

# 3. Obtener lista de archivos .txt en la carpeta actual
archivos_txt = [archivo for archivo in os.listdir() if archivo.endswith('.txt') and archivo != os.path.basename(nombre_reporte)]

# 4. Procesar los archivos y generar el reporte
with open(nombre_reporte, 'w') as reporte:
    if not archivos_txt:
        reporte.write("No se encontraron archivos de texto.\n")
    else:
        total_archivos = 0
        total_lineas = 0
        
        for archivo in archivos_txt:
            # Contar líneas en cada archivo
            with open(archivo, 'r') as f:
                num_lineas = sum(1 for linea in f)
            
            # Escribir en el reporte
            reporte.write(f"{archivo} - {num_lineas} líneas\n")
            total_archivos += 1
            total_lineas += num_lineas
        
        # Escribir totales
        reporte.write(f"\nTotal de archivos procesados: {total_archivos}\n")
        reporte.write(f"Total de líneas procesadas: {total_lineas}\n")

print(f"Reporte generado: {nombre_reporte}")