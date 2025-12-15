# 🗳️ Sistema de Votación Distribuido (Kubernetes & Python)

Este proyecto implementa un sistema de votación **Cliente-Servidor** contenerizado con Docker y orquestado mediante Kubernetes.

El sistema permite registrar votos en tiempo real, visualizar el conteo y **evita fraudes** impidiendo que un mismo usuario (identificado por su nombre) vote más de una vez en la misma sesión.

**Asignatura:** Sistemas distribuidos  
**Autores:**
* Francisco Hernandez
* Camilo Lovera

---

## 📂 Estructura del Proyecto

```text
sistema-votacion/
│
├── app/
│   ├── server.py       # Lógica del servidor
│   ├── client.py       # Interfaz de votación
│   └── requirements.txt
│
├── k8s/
│   ├── deployment.yaml # Configuración de Pods y Réplicas
│
├── Dockerfile          # Instrucciones de empaquetado para Docker
└── README.md           # Documentación del proyecto

```

# ⚙️ Prerrequisitos


Para ejecutar este proyecto necesitas:

    Docker Desktop (con Kubernetes habilitado en la configuración).

    Git (para control de versiones).

    Ngrok

#   Instrucciones para el Servidor
## 1. Construcción y Publicación de la Imagen

    # Iniciar sesión en Docker Hub
    docker login

    # Construir la imagen
    # Reemplaza 'tu_usuario' con tu ID real de Docker Hub
    docker build -t tu_usuario/voto-server:v1 .

    # Subir la imagen a la nube
    docker push tu_usuario/voto-server:v1


## 2. Despliegue en Kubernetes

    minikube start

    kubectl apply -f k8s/

    # Verificacion de que esta funcionando
    kubectl get pods

## 3. Habilitar Acceso (Port Forwarding)

    # Redirige el puerto 8080 local al puerto 80 del servicio
    kubectl port-forward service/voto-service 8080:80

## 4. Acceso Remoto con Ngrok
    # En consola
    ngrok http 8080

# Instrucciones para el Cliente (Votantes)

## 1. Ejecutar el 
    # Reemplaza 'tu_usuario' (kmiloo)
    docker run -it --network host tu_usuario/voto-server:v1 python client.py

    #Se debera ingresar la direccion dada por ngrok al realizar el voto


# Visualización de Resultados

## 1. Logs de Kubernetes
    kubectl logs -f deployment/voto-server-deployment

## 2. Contador de votos
    # Entrar por comando o directamente por el navegador la direccion ip dependera de la dada por ngrok
    watch -n 2 "curl -s http://localhost:8080/"
