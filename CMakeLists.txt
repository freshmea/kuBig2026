cmake_minimum_required(VERSION 3.10)
project(kuBig2026)

set(CMAKE_CXX_STANDARD 17)
include(ExternalProject)

add_subdirectory(c_example/part3)
add_subdirectory(c_example/part4/carSerial)
add_subdirectory(c_example/part4/myRandom)
add_subdirectory(c_example/part4/baseballGame)
add_subdirectory(c_example/part5/date)
add_subdirectory(c_example/part5/twoDouble)
add_subdirectory(c_example/part6/scoreProcess)
add_subdirectory(ds/stack/myStack1)
add_subdirectory(ds/stack/myStack2)
add_subdirectory(ds/stack/myStack3)
add_subdirectory(ds/stack/myStack4)
add_subdirectory(ds/queue/myQueue1)
add_subdirectory(ds/queue/myQueue2)
add_subdirectory(ds/queue/myQueue3)
add_subdirectory(network)
add_subdirectory(bowling)

ExternalProject_Add(atmega128_project
	SOURCE_DIR ${CMAKE_SOURCE_DIR}/atmega128
	BINARY_DIR ${CMAKE_BINARY_DIR}/atmega128-build
	CMAKE_ARGS
		-DCMAKE_TOOLCHAIN_FILE=${CMAKE_SOURCE_DIR}/atmega128/avr-toolchain.cmake
		-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
	INSTALL_COMMAND ""
)

ExternalProject_Add(pico_project
	SOURCE_DIR ${CMAKE_SOURCE_DIR}/pico
	BINARY_DIR ${CMAKE_BINARY_DIR}/pico-build
	CMAKE_ARGS
		-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
		-DPICO_SDK_PATH=${CMAKE_SOURCE_DIR}/pico/deps/pico-sdk
	INSTALL_COMMAND ""
)