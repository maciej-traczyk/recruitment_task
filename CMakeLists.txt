cmake_minimum_required(VERSION 3.21)

project(recruitment_task LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(PYBIND11_FINDPYTHON ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(dicelib
  lib/dicelib.cpp
  lib/bindings.cpp
)

target_include_directories(dicelib PRIVATE lib)
install(TARGETS dicelib DESTINATION ".")