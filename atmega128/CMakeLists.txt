cmake_minimum_required(VERSION 3.10)

# standalone configure일 때만 기본 AVR 툴체인 파일을 지정한다.
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
    set(CMAKE_TOOLCHAIN_FILE "${CMAKE_CURRENT_SOURCE_DIR}/avr-toolchain.cmake")
endif()

project(Atmega128_Project C)

# --- 하드웨어 설정 ---
set(MCU atmega128)
set(F_CPU 16000000UL)
set(PROG_TYPE stk500v2)
set(PROG_PORT usb)
set(UART0_DIR "${CMAKE_CURRENT_SOURCE_DIR}/lib/uart0")

# --- 1. src 폴더의 모든 .c 파일 목록 가져오기 ---
file(GLOB SRC_FILES "src/*.c")

# --- 2. 각 파일별로 빌드 및 업로드 타겟 자동 생성 ---
foreach(SOURCE_FILE ${SRC_FILES})
    # 파일 경로에서 확장자를 제외한 이름만 추출 (예: src/fnd1.c -> fnd1)
    get_filename_component(EXE_NAME ${SOURCE_FILE} NAME_WE)

    # --- 실행 파일 및 옵션 ---
    add_executable(${EXE_NAME}.elf ${SOURCE_FILE})

    if(EXE_NAME STREQUAL "uart2")
        target_sources(${EXE_NAME}.elf PRIVATE "${UART0_DIR}/uart0.c")
        target_include_directories(${EXE_NAME}.elf PRIVATE "${UART0_DIR}")
    endif()

    target_compile_options(${EXE_NAME}.elf PUBLIC
        -mmcu=${MCU}
        -DF_CPU=${F_CPU}
        -Os -Wall
    )

    target_link_options(${EXE_NAME}.elf PUBLIC -mmcu=${MCU})

    # --- 빌드 후처리 (HEX 생성) ---
    add_custom_command(TARGET ${EXE_NAME}.elf POST_BUILD
        COMMAND avr-objcopy -j .text -j .data -O ihex ${EXE_NAME}.elf ${EXE_NAME}.hex
        COMMAND avr-size --format=avr --mcu=${MCU} ${EXE_NAME}.elf
        COMMENT "Generating Intel HEX file and analysis"
    )

    # --- 업로드 타겟 추가 ---
    add_custom_target(upload_${EXE_NAME}
        COMMAND avrdude -p m128 -c ${PROG_TYPE} -P ${PROG_PORT} -U flash:w:${EXE_NAME}.hex:i
        DEPENDS ${EXE_NAME}.elf
        COMMENT "Flashing ${EXE_NAME}.hex to hardware..."
    )
endforeach()