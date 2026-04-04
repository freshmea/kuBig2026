cmake_minimum_required(VERSION 3.10)
project(mqttPub)

include_directories(${CMAKE_CURRENT_LIST_DIR})

find_library(PAHO_MQTT_LIB paho-mqtt3c)

if(NOT PAHO_MQTT_LIB)
    message(FATAL_ERROR
        "paho-mqtt3c library not found; install libpaho-mqtt3c-dev (Ubuntu) or set "
        "PAHO_MQTT_LIB to the path of the library before configuring this project.")
endif()

add_executable(mqttPub mqttPub.c)
target_link_libraries(mqttPub ${PAHO_MQTT_LIB})
