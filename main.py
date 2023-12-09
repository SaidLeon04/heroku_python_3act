import fastapi
import sqlite3
import random
import hashlib
import datetime
from fastapi import Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBearer
from fastapi.security import  HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials

# Crea la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()
securityBearer = HTTPBearer()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contacto(BaseModel):
    email : str
    nombre : str
    telefono : str


@app.post("/contactos")
async def crear_contacto(contacto: Contacto, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Crea un nuevo contacto."""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        c = conn.cursor()

        c.execute('SELECT * FROM contactos WHERE email = ?', (contacto.email,))
        existe = c.fetchone()
        if existe is not None:
            raise fastapi.HTTPException(status_code=400, detail="Contacto ya existe")   
        else:
            c.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
                    (contacto.email, contacto.nombre, contacto.telefono))
            conn.commit()
            return contacto

@app.get("/contactos")
async def obtener_contactos(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Obtiene todos los contactos."""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        c = conn.cursor()
        c.execute('SELECT * FROM contactos;')
        response = []
        for row in c:
            contacto = {"email":row[0],"nombre":row[1], "telefono":row[2]}
            response.append(contacto)
        if response == -1: 
            raise fastapi.HTTPException(status_code=400, detail="Error al consultar los datos")
        else:
            return response


@app.get("/contactos/{email}")
async def obtener_contacto(email: str, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Obtiene un contacto por su email."""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        c = conn.cursor()
        c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
        contacto = None
        for row in c:
            contacto = {"email":row[0],"nombre":row[1],"telefono":row[2]}
        
        if contacto == None:
            raise fastapi.HTTPException(status_code=404, detail="Contacto no encontrado")
        else: 
            return contacto


@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Actualiza un contacto."""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        c = conn.cursor()

        c.execute('SELECT * FROM contactos WHERE email = ?', (contacto.email,))
        existe = c.fetchone()
        if existe is None:
            raise fastapi.HTTPException(status_code=400, detail="Contacto no existe")   
        else:
            c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
                (contacto.nombre, contacto.telefono, email))
            conn.commit()
            return contacto


@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Elimina un contacto."""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        c = conn.cursor()
        c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
        existe = c.fetchone()
        if existe is None:
            raise fastapi.HTTPException(status_code=400, detail="Contacto no existe")   
        else:
            c.execute('DELETE FROM contactos WHERE email = ?', (email,))
            conn.commit()
            return {"mensaje":"Contacto eliminado"}
    
    

@app.get("/")
def auth(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    """Autenticación"""
    connx = sqlite3.connect("usuarios.db")
    token = credentials.credentials
    c = connx.cursor()
    c.execute('SELECT token FROM usuarios WHERE token = ?', (token,))
    existe = c.fetchone()
    if existe is None:
        raise fastapi.HTTPException(status_code=401, detail="Token Innexistente")
    else:
        return {"mensaje":"Token Valido"}
        
        """
        VALIDACION DE TOKEN POR TIEMPO DE VIDA DE 1 MINUTO
        c.execute('SELECT timestamp FROM usuarios WHERE token = ?',(token,))
        for row in c:
            hora_bd = row[0]

        hora_actual = datetime.datetime.now()
        hora_hash = hora_actual.strftime("%H:%M")

        if hora_bd != hora_hash:
            raise fastapi.HTTPException(status_code=430, detail="Token Caducado")
        else:
            return {"mensaje: Bienvenido"}
        """
        
    
security = HTTPBasic()
@app.get("/token") # endpoint para obtener token
def validate_user(credentials: HTTPBasicCredentials = Depends(security)): 
    """Validación de usuario"""
    connx = sqlite3.connect("usuarios.db")
    username = credentials.username # se obtiene el username
    password = credentials.password # se obtiene el password
    hashpassword = hashlib.sha256(password.encode()).hexdigest() # se hashea el password
    c = connx.cursor() # crea un cursor

    hora_actual = datetime.datetime.now() # obtiene la hora actual
    hora_actual_formateada = hora_actual.strftime("%H:%M") # formatea la hora actual

    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()=+-*/@#$%&!?' # caracteres para generar el token
    longitud = 8 # longitud del token
    token = '' # variable para almacenar el token
    for i in range(longitud): # ciclo para generar el token
        token += random.choice(caracteres) # se agrega un caracter aleatorio al token
        
    hashtoken = hashlib.sha256(token.encode()).hexdigest() # se hashea el token
    # actualiza el token y la hora en la base de datos
    c.execute('UPDATE usuarios SET token = ?, timestamp = ? WHERE correo = ? AND password = ?', (hashtoken, hora_actual_formateada, username, hashpassword))
    connx.commit() # ejecuta la actualizacion

    c.execute('SELECT token FROM usuarios WHERE correo = ? AND password = ?', (username, hashpassword)) 
    existe = c.fetchone()
    if existe is None: 
        raise fastapi.HTTPException(status_code=401, detail="No autorizado")
    else:
        token = existe[0]
        return {"token":token}
