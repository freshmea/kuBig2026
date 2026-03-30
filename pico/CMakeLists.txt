# git submodule add https://github.com/raspberrypi/pico-sdk.git deps/pico-sdk

cmake_minimum_required(VERSION 3.13)

if (NOT PICO_SDK_PATH AND NOT DEFINED ENV{PICO_SDK_PATH})
set(PICO_SDK_PATH "${CMAKE_CURRENT_LIST_DIR}/deps/pico-sdk" CACHE PATH "Path to the Raspberry Pi Pico SDK")
endif()

set(PICO_BOARD pico2_w CACHE STRING "Board type")

include(pico_sdk_import.cmake)
project(my_project C CXX ASM)

pico_sdk_init()

add_executable(hello_pico src/main.c)
add_executable(blink
    src/blink.c
    )

# 표준 라이브러리 연결
target_link_libraries(hello_pico pico_stdlib)
target_link_libraries(blink pico_stdlib)

if (PICO_CYW43_SUPPORTED)
    target_link_libraries(blink pico_cyw43_arch_none)
endif()


pico_add_extra_outputs(hello_pico)
pico_add_extra_outputs(blink)

# USB 출력을 활성화하려면 아래 주석 해제 (Serial 모니터용)
pico_enable_stdio_usb(hello_pico 1)
pico_enable_stdio_uart(hello_pico 0)
