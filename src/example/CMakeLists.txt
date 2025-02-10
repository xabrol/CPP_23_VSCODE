file(GLOB_RECURSE MODULE_INTERFACE_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.ixx")
file(GLOB_RECURSE FILE_SOURCES 
    "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.hpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.h"    
)

#add an executable with the same name as PROJECT_NAME_LOWER defined in the root cmakelists.txt
#and include all the found source files in the current source directory (this subdirectory this cmakelists.txt is in)
add_executable(${PROJECT_NAME_LOWER} ${FILE_SOURCES})

#find the CLI11 package installed by Conan2 and links it into the project
find_package(CLI11 REQUIRED)

# Declare module interface files explicitly
target_sources(${PROJECT_NAME_LOWER}
    PUBLIC
        FILE_SET CXX_MODULES FILES ${MODULE_INTERFACE_FILES})

target_link_libraries(${PROJECT_NAME_LOWER} 
    PRIVATE 
        CLI11::CLI11
)

# Add a custom target for running the executable, 
# reason: cmake --build . --target run, works cross platform and handles the differences of how to 
# run executables on different platforms.
add_custom_target(run
    COMMAND $<TARGET_FILE:${PROJECT_NAME_LOWER}>
    DEPENDS ${PROJECT_NAME_LOWER}
    WORKING_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
    COMMENT "Running the example executable"
)