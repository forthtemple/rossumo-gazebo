# ROS Sumo Gazebo
This is a gazebo simulation of Parrot Jumping Sumo including ROS wrapper for Ardrone SDK 3. It allows you to simulate a Jumping Sumo Drone and also run a real Sumo Drone through ROS. You can record movements on the real Sumo drone with ROSBAG and play them in the simultion. The purpose of creating the simulation is to use reinforcement learning to teach a sumo to do things like climb stairs in Gazebo and apply what is learnt to a real jumping sumo.

Includes Gazebo simulation of a jumping Sumo. 

Also includes copy of https://github.com/arnaud-ramey/rossumo modified to have the same behaviour as Gazebo so can do simulations that are the same.

[![Youtube sumo](http://forthtemple.com/sumo/youtube500.jpg)](https://www.youtube.com/watch?v=5opPQ47Y-WE) 


# Installation Gazebo Only
Install ROS (eg http://wiki.ros.org/indigo/Installation/Ubuntu if from ubuntu)

If you just want run the model under gazebo then under your catkin_src directory:
```
cd ~/catkin_ws/src
git clone https://github.com/forthtemple/rossumo-gazebo.git
cd ~/catkin_ws
catkin_make --only-pkg-with-deps rossumo_gazebo
catkin_make --only-pkg-with-deps rossumo_description
```

# Run with Gazebo Only
In one terminal run:
```
roslaunch rossumo_gazebo rossumo_world.launch
```
In another terminal run:
```
rosrun rossumo teleop_twist_keyboard.py
```

# Installation rossumo
To install the ROS wrapper for Ardrone SDK 3 follow instructions for install rossumo under 'rossumo' directory including building the ardrone SDK

