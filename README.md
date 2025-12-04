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

```

# ⚙️ Prerrequisitos


Para ejecutar este proyecto necesitas:

    Docker Desktop (con Kubernetes habilitado en la configuración).

    Git (para control de versiones).

    Ngrok

#   Instrucciones para el Servidor
## 1. Construcción y Publicación de la Imagen

    # a. Iniciar sesión en Docker Hub
    docker login

    # b. Construir la imagen
    # IMPORTANTE: Reemplaza 'tu_usuario' con tu ID real de Docker Hub
    docker build -t tu_usuario/voto-server:v1 .

    # c. Subir la imagen a la nube
    docker push tu_usuario/voto-server:v1


## 2. Despliegue en Kubernetes

    kubectl apply -f k8s/

    kubectl get pods

## 3. Habilitar Acceso (Port Forwarding)

    # Redirige el puerto 8080 local al puerto 80 del servicio
    kubectl port-forward service/voto-service 8080:80

# Instrucciones para el Cliente (Votantes)

## 1. Ejecutar el 
    # Reemplaza 'tu_usuario' con el usuario del expositor
    docker run -it --network host tu_usuario/voto-server:v1 python client.py

## 2. Acceso Remoto con Ngrok
    ngrok http 8080

# Visualización de Resultados

## 1. Logs de Kubernetes
    kubectl logs -f deployment/voto-server-deployment

## 2. Contador de votos
    # entrar por comando o directamente por el navegador
    watch -n 2 "curl -s http://localhost:8080/"
