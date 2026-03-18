cmake_minimum_required(VERSION 3.10)
project(queue)

include_directories(${CMAKE_CURRENT_LIST_DIR})
add_executable(queue main.c queue.c)
