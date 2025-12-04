import requests
import sys

# Configuración de conexión
print("--- SISTEMA DE VOTACIÓN ---")
# Permitimos ingresar la URL o usar la default
url_input = input("Introduce la URL del servidor (Enter para http://localhost:8080/vote): ")

if url_input.strip() == "":
    url = "http://localhost:8080/vote" 
else:
    url = url_input

# Asegurarse de que la URL termine en /vote
if not url.endswith("/vote"):
    url += "/vote"

# --- CAMBIO IMPORTANTE AQUÍ ---
# En lugar de generar un ID aleatorio, pedimos el nombre
usuario_nombre = ""
while not usuario_nombre:
    usuario_nombre = input("\n👤 Por favor, ingresa tu NOMBRE (ej. JuanPerez): ").strip()

print(f"\nHola, {usuario_nombre}. Preparando tu boleta...")
print("Candidatos disponibles: OpcionA, OpcionB, OpcionC")

while True:
    seleccion = input(f"{usuario_nombre}, escribe tu voto: ")
    
    # Enviamos el nombre como 'id'
    payload = {"id": usuario_nombre, "voto": seleccion}
    
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        
        print(f"🗳️ Servidor dice: {data.get('mensaje')}")
        
        # Si el voto fue exitoso (código 200), salimos.
        # Si falló (ej. ya votó), el usuario puede intentar otra cosa o salir manualmente.
        if response.status_code == 200:
            print("¡Gracias por participar!")
            break 
        elif response.status_code == 403:
            print("⛔ Error: Ya existe un voto registrado con este nombre.")
            break
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor. Verifica la URL.")
        break