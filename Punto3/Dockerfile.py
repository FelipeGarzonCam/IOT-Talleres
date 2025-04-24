# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 19:29:29 2025

@author: amsua
"""

FROM osrf/ros:noetic-desktop-full

# Instalar TurtleBot3 y SLAM
RUN apt-get update && apt-get install -y \
    ros-noetic-turtlebot3 \
    ros-noetic-turtlebot3-simulations \
    ros-noetic-slam-gmapping

# Configurar entorno
RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc

# Script de inicio
CMD ["bash", "-c", "source /opt/ros/noetic/setup.bash && \
    roslaunch turtlebot3_gazebo turtlebot3_world.launch"]