from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain, cmake_layout

class ViseConan(ConanFile):
    name = "example"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"
    requires = ["cli11/2.4.2", "spdlog/1.14.1", "gegles-spdlog_setup/1.1.0", "di/1.3.0"]

    def layout(self):
        cmake_layout(self, build_folder="")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        target_os = self.settings.get_safe("os").lower() if self.settings.os else None
        if (target_os == None):
            raise Exception("OS not set")

        tc = CMakeToolchain(self)
        tc.absolute_paths = False
        tc.presets_prefix = (
            f"{target_os}"  # will allow profiles to be generated for multiple platforms
        )
        tc.generator = "Ninja"
        tc.generate()
