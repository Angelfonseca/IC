import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
import subprocess
import bcrypt

# Conectar a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['python']
collection = db['usuarios']

# Función para verificar el login
def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showwarning("Advertencia", "Por favor, ingrese usuario y contraseña.")
        return

    # Buscar el usuario en la base de datos
    usuario_encontrado = collection.find_one({"usuario": usuario})

    if usuario_encontrado and bcrypt.checkpw(contrasena.encode('utf-8'), usuario_encontrado['contrasena']):
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        root.destroy()  # Cierra la ventana de login
        abrir_preguntas()  # Llama a la función que abre preguntas.py
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showwarning("Advertencia", "Por favor, ingrese usuario y contraseña.")
        return

    # Verificar si el usuario ya existe
    usuario_existente = collection.find_one({"usuario": usuario})
    if usuario_existente:
        messagebox.showerror("Error", "El nombre de usuario ya está en uso.")
        return

    # Encriptar la contraseña
    hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    # Insertar el nuevo usuario en la base de datos
    collection.insert_one({"usuario": usuario, "contrasena": hashed})
    messagebox.showinfo("Éxito", "Registro exitoso.")

# Función para abrir preguntas.py
def abrir_preguntas():
    # Aquí puedes ejecutar preguntas.py
    subprocess.run(["python", "preguntas.py"])

# Creación de la interfaz gráfica
root = tk.Tk()
root.title("Login con MongoDB")

# Campos de entrada
ttk.Label(root, text="Usuario:").grid(column=0, row=0, padx=10, pady=10)
entry_usuario = ttk.Entry(root)
entry_usuario.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Contraseña:").grid(column=0, row=1, padx=10, pady=10)
entry_contrasena = ttk.Entry(root, show="*")
entry_contrasena.grid(column=1, row=1, padx=10, pady=10)

# Botones para login y registro
login_button = ttk.Button(root, text="Login", command=verificar_login)
login_button.grid(column=0, row=2, padx=10, pady=10)

register_button = ttk.Button(root, text="Registrar", command=registrar_usuario)
register_button.grid(column=1, row=2, padx=10, pady=10)

root.mainloop()