# IOT-Talleres

Repositorio para reforzar conocimientos en Docker, aprendiendo sobre Pybullet y Tkinter

---

## Punto 1: Investigacion Sobre  Gazebo, Molvet y Ros 



---

## Punto 2: Simulación de Robot de Dos Articulaciones con PyBullet

- **Descripción**  
  Simulación de un manip­ulador de dos juntas en entorno PyBullet, con sliders para controlar ángulos y velocidad de la simulación, todo esto corriendo en un Docker con Ubuntu
- **Carpeta / Archivos**  
  `Punto2Taller2/Dockerfile` · `Punto2Taller2/Main.py` · `Punto2Taller2/two_joint_robot_custom.urdf`
- **Tecnologías**  
  Python · PyBullet · URDF · Docker (para contenerización opcional)

---

## Punto 3: Integración con Gazebo y Visualización de Mapas

- **Descripción**  
  Scripts para levantar entornos en Gazebo, visualizar mapas y configurar contenedores Docker para robótica.
- **Carpeta / Archivos**  
  `Punto3/Dockerfile.py` · `Punto3/Ejecutar_Gazebo.py` · `Punto3/Visualizar_mapa.py`
- **Tecnologías**  
  Python · ROS/Gazebo · Docker

---

## Simulación de Control PID en Pista Circular

- **Descripción**  
  Simulación de un carro seguidor de pista circular usando control PID.
- **Carpeta / Archivo**  
  `PistatKinter/main.py`
- **Tecnologías**  
  Python · Tkinter · PID
---

## Requisitos

- Python 3.7+  
- Módulos Python:  
  ```bash
  pip install numpy pybullet tkinter
