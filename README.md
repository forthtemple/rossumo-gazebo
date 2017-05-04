# ROS Sumo Gazebo
Gazebo simulation of Parrot Jumping Sumo with ROS wrapper for Ardrone SDK 3 

Includes Gazebo simulation of a jumping Sumo. 

Also includes copy of https://github.com/arnaud-ramey/rossumo modified to have the same behaviour as Gazebo so can do simulations that are the same.

[![Youtube sumo](http://forthtemple.com/sumo/youtube500.jpg)](https://www.youtube.com/watch?v=5opPQ47Y-WE) 


# Installation Gazebo Only
Install ROS (eg http://wiki.ros.org/indigo/Installation/Ubuntu if from ubuntu)

If you just want run the model under gazebo then under your catkin_src directory:
 cd ~/catkin_ws/src
 git clone https://github.com/forthtemple/rossumo-gazebo.git
 cd ~/catkin_ws
 catkin_make --only-pkg-with-deps rossumo_gazebo
 catkin_make --only-pkg-with-deps rossumo_description

# Run with Gazebo Only
In one terminal run:
roslaunch rossumo_gazebo rossumo_world.launch

In another terminal run:
rosrun rossumo teleop_twist_keyboard.py


# Installation Full
Follow instructions for install rossumo under 'rossumo' directory

