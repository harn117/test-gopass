import psycopg2

# Datos de la conexión a PostgreSQL
DB_HOST = "localhost"
DB_NAME = "test-1"
DB_USER = "admin"
DB_PASSWORD = "secret-"

def user_insert(nombre, email):
    """Inserta un nuevo usuario en la tabla 'usuario'."""
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()
        sql = "INSERT INTO usuario (nombre, email) VALUES (%s, %s)"
        cur.execute(sql, (nombre, email))
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error al insertar usuario: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cur.close()
            conn.close()

def user_list():
    """Lista todos los usuarios'."""
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()
        cur.execute("SELECT *")
        usuarios = cur.fetchall()
        if usuarios:
            print("\nLista de Usuarios:")
            for id, nombre, email in usuarios:
                print(f"ID: {id}, Nombre: {nombre}, Email: {email}")
        else:
            print("No hay usuarios.")
    except psycopg2.Error as e:
        print(f"Error al listar usuarios: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()
