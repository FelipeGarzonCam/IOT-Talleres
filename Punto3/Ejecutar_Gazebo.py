# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 19:30:28 2025

@author: amsua
"""

# Terminal 1: Simulación (Gazebo)
docker run -it --rm \
    --env="DISPLAY" \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network-host \
    --name slam-bot \
    turtlebot3-slam

# Terminal 2: SLAM (dentro del mismo contenedor)
docker exec -it slam-bot bash -c "source /opt/ros/noetic/setup.bash && \
    roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping"

# Terminal 3: Teleoperación (para mover el robot)
docker exec -it slam-bot bash -c "source /opt/ros/noetic/setup.bash && \
    rosrun turtlebot3_teleop turtlebot3_teleop_key"