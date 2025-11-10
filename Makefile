# Makefile for building sumsq.cpp with Boost.Python

CXX = g++
CXXFLAGS = -O2 -Wall -fPIC
BOOST_PYTHON_LIB = -lboost_python
PYTHON_CONFIG = python3-config

INCLUDES = -I/usr/include/python3.10 -I/usr/include
LDFLAGS = /usr/lib/x86_64-linux-gnu/libboost_python310.so -shared

TARGET = sumsq.so
SRC = sumsq.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -shared $^ -o $@ $(LDFLAGS)

clean:
	rm -f $(TARGET)