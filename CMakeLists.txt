cmake_minimum_required(VERSION 3.0.0)
set (CMAKE_CXX_STANDARD 17)

set(PROJECT_NAME rosbag-reader-driver)
project( ${PROJECT_NAME} CXX )

# Folders files
set(CPP_DIR ./src)
set(HEADER_DIR ./src )

find_package( OpenCV 3)
find_package( yaml-cpp REQUIRED)

find_package(cv_bridge REQUIRED)
find_package(roscpp REQUIRED)
find_package(roslib REQUIRED)
find_package(rosbag REQUIRED)
find_package(image_transport REQUIRED)
find_package(sensor_msgs REQUIRED)

set(ros_INCLUDE_DIRS 
  ${roslib_INCLUDE_DIRS}
  ${roscpp_INCLUDE_DIRS}
  ${rosbag_INCLUDE_DIRS}
  ${cv_bridge_INCLUDE_DIRS}
  ${image_transport_INCLUDE_DIRS}
  ${sensor_msgs_INCLUDE_DIRS}
)

set(ros_LIBRARIES 
  ${roslib_LIBRARIES}
  ${roscpp_LIBRARIES}
  ${rosbag_LIBRARIES}
  ${cv_bridge_LIBRARIES}
  ${image_transport_LIBRARIES}
  ${sensor_msgs_LIBRARIES}
)

include_directories(include ${ros_INCLUDE_DIRS})


file(GLOB SRC_FILES
  ${CPP_DIR}/*.cpp
  ${CPP_DIR}/rosbag-reader/*.cpp
)
file(GLOB HDR_FILES
  ${HEADER_DIR}/*.h
  ${CPP_DIR}/rosbag-reader/*.h
)

add_executable( ${PROJECT_NAME} ${CPP_DIR}/${PROJECT_NAME}.cpp ${SRC_FILES})
target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} yaml-cpp ${ros_LIBRARIES})