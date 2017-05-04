# ROS Sumo Gazebo
This is a gazebo simulation of Parrot Jumping Sumo including ROS wrapper for Ardrone SDK 3 . It allows you to simulate a Jumping Sumo Drone and also run a real Sumo Drone through ROS. You can record movements on the real Sumo drone with ROSBAG and play them in the simultion. The purpose of creating the simulation is to use reinforcement learning to teach a sumo to do things like climb stairs in Gazebo and apply what is learnt to a real jumping sumo. The ROS wrapper is from https://github.com/arnaud-ramey/rossumo  and has been modified to make the behaviour of the real jumping sumo and gazebo jumping sumo the same.

The following shows an example of a movements of a real sumo being recorded with Rosbag on the left and the movements being played to the simulation in Gazebo. The layout of both rooms are the same:

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
and press the keys to move the sumo.

# Installation rossumo
To install the ROS wrapper for Ardrone SDK 3 follow instructions for install rossumo under 'rossumo' directory including building the ardrone SDK. It is similar to https://github.com/arnaud-ramey/rossumo but has been modified to behave like the Gazebo sumo.





