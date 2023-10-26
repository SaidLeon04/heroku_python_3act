import fastapi
import sqlite3
from pydantic import BaseModel
import mysql.connector


app = fastapi.FastAPI()

conexion = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='contactos')
cursor = conexion.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS contactos (correo VARCHAR(255) PRIMARY KEY, nombre VARCHAR(255), telefono VARCHAR(15))")
class Contacto(BaseModel):
    email : str
    nombres : str
    telefono : str

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    sql = "INSERT INTO contactos (correo, nombre, telefono) VALUES (%s, %s, %s)"
    valores = (contacto.correo, contacto.nombre, contacto.telefono)
    cursor.execute(sql, valores)
    conexion.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    # TODO Consulta todos los contactos de la base de datos y los envia en un JSON
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    response = []
    for row in contactos:
        contacto = row
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    sql = "SELECT * FROM contactos WHERE correo = %s"
    valores = (contacto.correo)
    cursor.execute(sql, valores)
    contacto = cursor.fetchone()
    if contacto:
        return Contacto(correo=contacto[0], nombre=contacto[1], telefono=contacto[2])
    else:
        return None

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto, nuevo_nombre:str,nuevo_telefono:str):
    """Actualiza un contacto."""
    sql = "UPDATE contactos SET nombre = %s, telefono = %s WHERE correo = %s"
    valores = (nuevo_nombre, nuevo_telefono, contacto.correo)
    cursor.execute(sql, valores)
    conexion.commit()
    response = {"mensaje":"actualizado"}
    return response



@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    sql = "DELETE FROM contactos WHERE correo = %s"
    valores = (email)
    cursor.execute(sql, valores)
    conexion.commit()
    response = {"mensaje":"eliminado"}
    return response
