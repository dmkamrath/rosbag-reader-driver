cmake_minimum_required(VERSION 3.0.0)
set (CMAKE_CXX_STANDARD 17)

set(PROJECT_NAME unnamed)
project( ${PROJECT_NAME} CXX )

# Folders files
set(CPP_DIR ./src)
set(HEADER_DIR ./src )

find_package( OpenCV 3)
find_package( yaml-cpp REQUIRED)


file(GLOB SRC_FILES
  ${CPP_DIR}/*.cpp
)
file(GLOB HDR_FILES
  ${HEADER_DIR}/*.h
)

add_executable( ${PROJECT_NAME} ${CPP_DIR}/${PROJECT_NAME}.cpp )
target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} yaml-cpp )