import fastapi
import sqlite3
from pydantic import BaseModel
import json

# Crea la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()

class Contacto(BaseModel):
    email : str
    nombres : str
    telefono : str

# Rutas para las operaciones CRUD

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    # TODO Inserta el contacto en la base de datos y responde con un mensaje
    connection = conn.cursor()
    conn.execute('INSERT INTO contacto (email, nombres, telefono) VALUES (contacto.email, contacto.nombre, contacto.telefono)')
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    # TODO Consulta todos los contactos de la base de datos y los envia en un JSON
    c = conn.cursor()
    c.execute('SELECT * FROM contactos')
    response = []
    for row in c:
        contacto = row
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    # Consulta el contacto por su email
    co = conn.cursor()
    co.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in co:
        if (row[0]) == email:
            return row


@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza un contacto."""
    # TODO Actualiza el contacto en la base de datos
    c = conn.cursor()
    c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombres, contacto.telefono, email))
    conn.commit()
    return contacto


@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    # TODO Elimina el contacto de la base de datos
    connection = conn.cursor()
    connection.execute('DELETE FROM contactos WHERE email = ?', (email))
    conn.commit()
    response = {"mensaje":"eliminado"}
    return response