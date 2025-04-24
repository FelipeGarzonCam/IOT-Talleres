# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 19:32:42 2025

@author: amsua
"""

docker exec -it slam-bot bash -c "source /opt/ros/noetic/setup.bash && \
    rosrun rviz rviz -d /opt/ros/noetic/share/turtlebot3_slam/rviz/turtlebot3_gmapping.rviz"