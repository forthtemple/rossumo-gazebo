### 1 - Required CMake Version
cmake_minimum_required(VERSION 2.8.3)

#message(camera_calibration_parsers_LIBRARIES ${camera_calibration_parsers_LIBRARIES})

#set(CMAKE_CXX_COMPILER "/usr/bin/clang++")
#set(CMAKE_C_COMPILER "/usr/bin/clang") 
#set(CMAKE_CXX_COMPILER "/home/skinhat/gcc-5.3.0/outdir/gcc/xg++")
#set(CMAKE_C_COMPILER "/home/skinhat/gcc-5.3.0/outdir/gcc/xgcc") 
set(CMAKE_CXX_COMPILER "/usr/bin/g++-5")
set(CMAKE_C_COMPILER "/usr/bin/gcc-5") 
#export CC=/usr/bin/gcc-5 export CXX=/usr/bin/g++-5

#message() 
### 2- Package Name
project(rossumo)
SET(CMAKE_BUILD_TYPE RelWithDebInfo) #None Debug Release RelWithDebInfo MinSizeRel
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra") # add extra warnings
### 3 - Find other CMake/Catkin packages needed for build
#SET(CMAKE_MODULE_PATH "/opt/ros/kinetic/;${CMAKE_MODULE_PATH}" )
#message(catkin_LIBRARIES ${catkin_LIBRARIES})
message( CMAKE_MODULE_PATH   ${CMAKE_MODULE_PATH})  
find_package(catkin REQUIRED COMPONENTS roscpp roslib rospy rosconsole rostime
                    camera_calibration_parsers  cv_bridge  image_geometry  image_transport  std_msgs camera_info_manager )
#SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR})
#ARDrone libs
message(catkin_LIBRARIES ${catkin_LIBRARIES})
#message( CMAKE_MODULE_PATH   ${CMAKE_MODULE_PATH})  
SET(ARDRONESDK3_PATH /home/skinhat/ardrone/out/Unix-base/staging/usr
    CACHE PATH "The path to the ARDroneSDK3 'usr' folder")
include_directories(${ARDRONESDK3_PATH}/include)
link_directories(${ARDRONESDK3_PATH}/lib/)
set(ARDRONESDK3_LIBRARIES  arcommands  arcontroller  ardiscovery  arsal)
# other libs
find_package(OpenCV REQUIRED)
### 4 - Message/Service/Action Generators (add_message_files(), add_service_files(), add_action_files())
# nothing to do
### 5 - Invoke message/service/action generation (generate_messages())
## Generate added messages and services with any dependencies listed here
### 6 - Specify package build info export (catkin_package())
catkin_package(
  INCLUDE_DIRS   include  src
  CATKIN_DEPENDS roscpp roslib
    camera_calibration_parsers  cv_bridge image_transport std_msgs camera_info_manager
)
### 7 - Libraries/Executables to build (add_library()/add_executable()/target_link_libraries())
include_directories(include  src  ${catkin_INCLUDE_DIRS})
ADD_SUBDIRECTORY(src)
### 8 - Tests to build (catkin_add_gtest())
#~ ADD_SUBDIRECTORY(test)
### 9 - Install rules (install())
install(DIRECTORY include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.h"
   PATTERN ".svn" EXCLUDE
)

#target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
#)
