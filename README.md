# 🗳️ Sistema de Votación Distribuido (Kubernetes & Python)

Este proyecto implementa un sistema de votación **Cliente-Servidor** contenerizado con Docker y orquestado mediante Kubernetes.

El sistema permite registrar votos en tiempo real, visualizar el conteo y **evita fraudes** impidiendo que un mismo usuario (identificado por su nombre) vote más de una vez en la misma sesión.

**Asignatura:** [Nombre de la Asignatura]  
**Autores:**
* [Tu Nombre]
* [Nombre de tu Pareja]

---

## 📂 Estructura del Proyecto

```text
sistema-votacion/
│
├── app/
│   ├── server.py       # Lógica del servidor (API REST con Flask)
│   ├── client.py       # Interfaz de votación (Script interactivo)
│   └── requirements.txt
│
├── k8s/
│   ├── deployment.yaml # Configuración de Pods y Réplicas
│   ├── service.yaml    # Configuración de Red (LoadBalancer)
│   └── ingress.yaml    # Reglas de enrutamiento (Punto Extra)
│
├── Dockerfile          # Instrucciones de empaquetado para Docker
└── README.md           # Documentación del proyecto

⚙️ Prerrequisitos

Para ejecutar este proyecto necesitas:

    Docker Desktop (con Kubernetes habilitado en la configuración).

    Git (para control de versiones).

    Ngrok (Opcional: Recomendado para exponer el servidor durante la presentación en clase).

🚀 1. Instrucciones para el Servidor (Expositor)

Estos pasos debe realizarlos la persona que proyectará el servidor en clase.
A. Construcción y Publicación de la Imagen

Asegúrate de estar en la carpeta raíz del proyecto.
Bash

# 1. Iniciar sesión en Docker Hub
docker login

# 2. Construir la imagen
# IMPORTANTE: Reemplaza 'tu_usuario' con tu ID real de Docker Hub
docker build -t tu_usuario/voto-server:v1 .

# 3. Subir la imagen a la nube
docker push tu_usuario/voto-server:v1

    ⚠️ NOTA CRÍTICA: Antes de desplegar, abre el archivo k8s/deployment.yaml y asegúrate de que la línea image: coincida exactamente con el nombre de la imagen que acabas de subir (ej. tu_usuario/voto-server:v1).

B. Despliegue en Kubernetes

Levanta la infraestructura completa (Deployment, Service e Ingress).
Bash

kubectl apply -f k8s/

Verifica que el sistema esté corriendo:
Bash

kubectl get pods
# El estado debe ser 'Running'

C. Habilitar Acceso (Port Forwarding)

Para conectar nuestra máquina local al cluster de Kubernetes, abriremos un túnel. Mantén esta terminal abierta durante toda la presentación.
Bash

# Redirige el puerto 8080 local al puerto 80 del servicio
kubectl port-forward service/voto-service 8080:80

📱 2. Instrucciones para el Cliente (Votantes)

El resto de la clase actuará como clientes. Para cumplir con el requisito de "Cliente Contenerizado", deben usar Docker.
Ejecutar el Cliente

Los compañeros deben ejecutar el siguiente comando en su terminal:
Bash

# Reemplaza 'tu_usuario' con el usuario del expositor
docker run -it --network host tu_usuario/voto-server:v1 python client.py

Flujo de Votación

El programa interactivo solicitará:

    URL del Servidor:

        Si están en la misma PC: http://localhost:8080/vote

        Si es presentación remota: La URL de Ngrok (ver sección abajo).

    Nombre: Deben ingresar su nombre o apodo.

    Voto: Escribir una de las opciones (OpcionA, OpcionB, OpcionC).

    Seguridad: Si intentan votar nuevamente con el mismo nombre, el sistema rechazará el voto.

🌐 3. Exposición en Clase (Acceso Remoto con Ngrok)

Para que los compañeros puedan votar desde sus propios equipos sin estar en la red local del expositor:

    Asegúrate de tener corriendo el kubectl port-forward ... 8080:80.

    En una nueva terminal, ejecuta Ngrok:
    Bash

    ngrok http 8080

    Copia la URL HTTPS que genera (ejemplo: https://random-id.ngrok-free.app).

    Instrucción para la clase: "Chicos, en la parte que pide URL, peguen esta dirección".

📊 4. Visualización de Resultados

El servidor permite ver el escrutinio en tiempo real de tres formas:

    Dashboard Web: Abre tu navegador en http://localhost:8080 (o la URL de Ngrok).

    Logs de Kubernetes:
    Bash

kubectl logs -f deployment/voto-server-deployment

Monitor en Terminal (Recomendado para proyectar):
Bash

    watch -n 2 "curl -s http://localhost:8080/"

🏆 5. Punto Extra: Ingress

Se ha incluido el archivo k8s/ingress.yaml para demostrar el manejo de rutas. Aunque en la presentación usamos port-forward y ngrok por simplicidad de red, el Ingress está configurado para responder al host votacion.clase.local.
🧹 Limpieza y Mantenimiento
Eliminar el despliegue

Al finalizar la clase, elimina los recursos para liberar memoria:
Bash

kubectl delete -f k8s/

💡 Tip Extra: Gestión de Git

Si por error subiste archivos innecesarios al repositorio (como carpetas venv, __pycache__ o archivos .DS_Store), usa estos comandos para eliminarlos de GitHub sin borrarlos de tu computadora local:
Bash

# 1. Dejar de rastrear el archivo/carpeta
git rm --cached nombre_del_archivo
# O si es una carpeta: git rm -r --cached nombre_carpeta

# 2. Confirmar el cambio
git commit -m "Eliminado archivo innecesario del repo"

# 3. Actualizar GitHub
git push

