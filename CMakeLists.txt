cmake_minimum_required(VERSION 3.10)
project(boost_python_example)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(Boost COMPONENTS python REQUIRED)

add_library(sumsq MODULE sumsq.cpp)
target_include_directories(sumsq PRIVATE ${Python3_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})
target_link_libraries(sumsq PRIVATE ${Python3_LIBRARIES} Boost::python)

set_target_properties(sumsq PROPERTIES
    PREFIX ""
    SUFFIX ".so"
)