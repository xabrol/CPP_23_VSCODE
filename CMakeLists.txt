#force cmake 3.31 or higher, fail if not met
cmake_minimum_required(VERSION 3.31 FATAL_ERROR)

# Define project name as a variable
set(PROJECT_NAME "Example")
string(TOLOWER ${PROJECT_NAME} PROJECT_NAME_LOWER) #stores the project name in all lowercase to PROJECT_NAME_LOWER

# Enable modern CMake behaviors
cmake_policy(SET CMP0177 NEW) # install() DESTINATION paths are normalized.
cmake_policy(SET CMP0178 NEW) # Test command lines preserve empty arguments.
cmake_policy(SET CMP0180 NEW) # project() always sets <PROJECT-NAME>_* as normal variables.
cmake_policy(SET CMP0048 NEW)  # Project version in project() command
cmake_policy(SET CMP0077 NEW)  # Option() honors normal variables
cmake_policy(SET CMP0155 NEW)  # Enable new CMake module support behavior

# Set C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_EXPERIMENTAL_CXX_MODULE_CMAKE_API "TRUE") # Enables proper module handling in CMake
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

# Ensure your compiler supports C++ modules
if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    add_compile_options(/experimental:module)
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    add_compile_options(-fmodules)
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # GCC's module support is still experimental
    add_compile_options(-fmodules-ts)
endif()

#https://cmake.org/cmake/help/latest/command/project.html
project(${PROJECT_NAME}
    VERSION 0.0.1 
    LANGUAGES CXX
    DESCRIPTION "Example Project"  # Adding description is good practice
)

# Set default build type to Debug if not specified
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "Choose the type of build" FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS 
        "Debug" "Release")
endif()

#tells cmake to compile a compile_commands.json file for the compiled commands for each source file
#this is needed for clangd/clang-tidy to function properly
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Define output directories for binaries
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_BINARY_DIR}/lib)

#subdirectories
add_subdirectory(src/${PROJECT_NAME_LOWER})