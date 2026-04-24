cmake_minimum_required(VERSION 3.8)
project(limo_car)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch urdf worlds config maps
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/robot_description_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
