cmake_minimum_required(VERSION 3.10)
project(iotLogReport)

include_directories(${CMAKE_CURRENT_LIST_DIR})
add_executable(iotLogReport main.c iotLogReport.c)
