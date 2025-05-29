# IOT-Talleres

##
---
# SpaceMax Defender 🚀

Un emocionante juego espacial desarrollado en Python con Pygame, donde defiendas la galaxia de invasores alienígenas. (Osea un SpaceInvander de toda la vida)

## 🎮 Características del Juego

- **Controles simples**: Usa las flechas para moverte y ESPACIO para disparar
- **Sistema de puntuación**: Gana puntos por cada enemigo eliminado
- **Múltiples tipos de enemigos**: 3 diferentes tipos de naves enemigas
- **Efectos de sonido**: Sonidos inmersivos de láser y explosiones
- **Vidas limitadas**: 3 vidas para completar el desafío

## 🕹️ Controles

- **← →**: Mover nave izquierda/derecha
- **ESPACIO**: Disparar láser
- **ESC**: Salir del juego
- **P**: Pausa el juego

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Pygame 2.0+**
- **Docker** para containerización
- **Assets personalizados** (sprites, sonidos, fondos) creados con IA

## 📁 Estructura del Proyecto

```
spacemax-defender/
├── spacemax_defender.py      # Código principal del juego
├── Dockerfile               # Configuración Docker
├── requirements.txt         # Dependencias Python
├── README.md               # Este archivo
├── assets/                 # Recursos del juego
    ├── images/            # Sprites y fondos
    │   ├── player.png
    │   ├── enemy1.png
    │   ├── enemy2.png
    │   ├── enemy3.png
    │   ├── bullet.png
    │   └── background.jpg
    └── sounds/            # Efectos de sonido
        ├── laser.mp3
        └── explosion.mp3

```

## 🎨 Personalización

### 
- **Niveles bucle**: Cada vez que termines con tus enemigos, avanzas de nivel!
- **Barra de vida**: Ahora cuentas con una barra de vida, no muerees al primer disparo!
- **Enemigos mas agresivos**: Ahora los enemigos varian su velocidad entre ellos, y te pueden disparar!
- **Pausa**: Ahora puedes pausar el juego con la tecla 'P'


![SpaceMax](https://github.com/user-attachments/assets/9fe4a08c-7337-49fb-b56c-a8f6287d1ad2)

---
# Taller 2
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
--



