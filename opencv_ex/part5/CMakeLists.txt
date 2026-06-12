cmake_minimum_required(VERSION 3.16)
project(opencv_cpp_part5)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(ZBAR REQUIRED zbar)

file(GLOB SOURCES "*.cpp")

foreach(SOURCE ${SOURCES})
    get_filename_component(EXE_NAME ${SOURCE} NAME_WE)
    add_executable(${EXE_NAME} ${SOURCE})
    target_include_directories(${EXE_NAME} PRIVATE
        ${OpenCV_INCLUDE_DIRS}
        ${ZBAR_INCLUDE_DIRS}
    )
    target_link_libraries(${EXE_NAME} ${OpenCV_LIBS} ${ZBAR_INCLUDE_DIRS})
endforeach()
