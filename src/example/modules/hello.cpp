//with clang if you have normal header imports etc you need to define the global module fragment and include in there before defining the module itself
//https://clang.llvm.org/docs/StandardCPlusPlusModules.html#standard-c-named-modules
module;
#include <iostream>
module hello;

void say_hello() {
    std::cout << "Hello, World from C++23 Modules!" << std::endl;
}
