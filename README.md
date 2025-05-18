# Informe Comparativo: Máquinas Virtuales vs Contenedores Docker

## Introducción

Las máquinas virtuales (VM) y los contenedores Docker son tecnologías ampliamente utilizadas en el despliegue y la administración de aplicaciones. Aunque ambos proporcionan entornos aislados para ejecutar software, su funcionamiento difiere fundamentalmente:

- Las **máquinas virtuales** emulan hardware completo y ejecutan un sistema operativo independiente.
- Los **contenedores Docker** se ejecutan sobre el sistema operativo anfitrión compartiendo su núcleo, lo que los hace más ligeros y rápidos de iniciar.

Este documento presenta un análisis comparativo entre ambos enfoques, usando una aplicación web con Flask para evaluar el rendimiento en ambas plataformas.

---

## Configuración del entorno de prueba

### Especificaciones de la máquina host

- **Modelo:** HP Victus by HP Gaming Laptop 16-s0xxx  
- **Procesador:** AMD Ryzen 5 (Family 25 Model 116)  
- **RAM:** 16 GB  
- **Sistema operativo:** Windows 11 Home  

### Máquina Virtual

- **Virtualizador:** VirtualBox  
- **Sistema operativo invitado:** Ubuntu  
- **CPU asignadas:** 3  
- **Memoria RAM:** 3 GB (memoria dinámica)  
- **Software instalado:** Python 3 y Flask  

### Docker

- **Imagen base utilizada:** `python:3.10-slim`  
- **Dockerfile:**

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app.py /app/app.py

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]```



## Métricas y herramientas utilizadas

El benchmarking se realizó mediante un script en Python que lanza solicitudes HTTP a una aplicación Flask durante un periodo de 60 segundos. Durante ese tiempo, se recolectaron las siguientes métricas:

- **Latencia por solicitud** (`requests.get`)
- **Porcentaje de uso de CPU**
- **Porcentaje de uso de memoria RAM**
- **Espacio utilizado en disco del entorno**
- **Total de solicitudes realizadas**
- **Tráfico de red estimado**

Los datos recopilados se almacenaron en archivos `.csv` para su posterior análisis. A partir de estos archivos se generaron gráficos comparativos para visualizar mejor las diferencias de rendimiento entre los entornos.

---

## Resultados

Los resultados visuales se encuentran disponibles en la carpeta `/results/` del repositorio. Las gráficas allí contenidas comparan el rendimiento de Docker y de la máquina virtual en función de las siguientes variables:

- Latencia: promedio, máxima y mínima
- Uso de CPU: promedio, máximo y mínimo
- Uso de memoria RAM: promedio, máximo y mínimo
- Tamaño del entorno en disco
- Cantidad total de peticiones procesadas
- Tráfico de red estimado

Estos resultados permiten analizar cómo se comporta cada tecnología bajo condiciones de carga similares.

---

## Análisis comparativo

### Docker

**Fortalezas:**

- Bajo consumo de recursos del sistema  
- Tiempo de despliegue y ejecución muy rápido  
- Escalabilidad sencilla  
- Ideal para aplicaciones pequeñas y medianas  

**Debilidades:**

- Menor aislamiento que una máquina virtual  
- Limitaciones al ejecutar aplicaciones complejas con múltiples dependencias o interfaces gráficas  

---

### Máquina Virtual

**Fortalezas:**

- Proporciona un entorno completamente aislado  
- Capacidad de emular diversos sistemas operativos y configuraciones  
- Adecuado para entornos corporativos o pruebas cercanas a producción  

**Debilidades:**

- Mayor consumo de recursos (RAM, CPU, almacenamiento)  
- Tiempo de arranque y configuración más prolongado  
- Menor eficiencia para aplicaciones pequeñas o tareas automatizadas  

---

## Conclusión

Docker resulta una alternativa más eficiente para escenarios donde se requiere rapidez, portabilidad y bajo consumo de recursos. Es especialmente adecuado para aplicaciones simples, microservicios o entornos donde la escalabilidad sea una prioridad.

Por otro lado, las máquinas virtuales ofrecen un mayor nivel de aislamiento y control, lo que las convierte en una opción más apropiada para entornos complejos, simulaciones, laboratorios o sistemas que deben mantenerse separados completamente entre sí.

Ambas tecnologías pueden coexistir y su elección dependerá del contexto, los objetivos del proyecto y los recursos disponibles.
