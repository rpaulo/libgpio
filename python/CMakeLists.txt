cmake_minimum_required(VERSION 2.8)
project(py-gpio)
add_custom_target(py-gpio ALL 
	python setup.py build -b ${CMAKE_BINARY_DIR}/python
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/python)
