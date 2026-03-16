cmake_minimum_required(VERSION 3.10)
project(twoDouble)

include_directories(${CMAKE_CURRENT_LIST_DIR})
add_executable(twoDouble main.c twoDouble.c)
