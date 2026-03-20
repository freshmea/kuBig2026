cmake_minimum_required(VERSION 3.10)
project(bowling)

include_directories(${CMAKE_CURRENT_LIST_DIR})
add_executable(bowling main.c board.c)
