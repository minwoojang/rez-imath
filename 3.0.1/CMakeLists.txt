CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)


set(url_imath https://github.com/AcademySoftwareFoundation/Imath.git)

if(${REZ_BUILD_INSTALL})
    message("------------------------------")
    set(imath_verison ${IMATH_VERSION})
    set(tag_imath v${IMATH_VERSION})
    message(STATUS ${make_args})
    message("------------------------------")

    # Rez 환경의 루트 디렉토리로 설치 경로 설정
    set(CMAKE_INSTALL_PREFIX "/home/minwoo/packages/imath/3.0.1/platform-linux/arch-x86_64")  # {root} 경로로 설정

    # 설치 경로 내의 include, lib 디렉토리 설정
    set(CMAKE_INSTALL_INCLUDEDIR ${CMAKE_INSTALL_PREFIX}/include)
    set(CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_PREFIX}/lib)

    # make 설치 명령 설정
    set(install_cmd make -j install ${make_args})
    message("------------------------------")
    message("------------------------------")
    message(STATUS CMAKE_INSTALL_PREFIX)
    message("------------------------------")
    message("------------------------------")
    
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    imath
    GIT_REPOSITORY ${url_imath}
    GIT_TAG ${tag_imath}
    PREFIX ${CMAKE_BINARY_DIR}/imath
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}  # 설치 경로 지정
)

add_dependencies(imath imath)
add_custom_target(imath-install COMMAND ${install_cmd} WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/imath)

install(CODE "execute_process(COMMAND echo \"Hello World\")")
