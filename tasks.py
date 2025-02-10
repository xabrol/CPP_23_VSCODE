import os
import platform
import shutil
from invoke import task

# todo add more profile platforms
platform_profiles = {
    "Linux": {
        "Linux": "./profiles/linux_host",
    },
    "Windows": {"Windows": "./profiles/windows_host"},
}


def get_host_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    elif os_name == "Darwin":
        return "macOS"
    else:
        return "Unknown"


def get_platform_values():
    osName = get_host_os()
    profiles = platform_profiles.get(osName)
    return profiles


@task
def conan_install(c, platform=None, build_type=None):
    platformValues = get_platform_values()
    if platform not in platformValues:
        raise ValueError(
            f"Invalid platform. Expected one of {[p.value for p in platformValues]}, got: {platform}"
        )

    osName = get_host_os()

    profiles = platform_profiles.get(osName)
    if not profiles:
        raise ValueError(f"Unsupported build platform: {osName}")

    build_profile = profiles.get(osName)
    if not build_profile:
        raise ValueError(f"Unsupported host platform: {platform}")

    host_profile = profiles.get(platform)
    if not host_profile:
        raise ValueError(
            f"Unsupported build platform: {platform}, unable to locate conan profile called {platform}"
        )

    if build_type not in {"Debug", "Release"}:
        raise ValueError(f"Unsupported build type: {build_type}")

    cmd = ["conan install ."]
    cmd.append(f"--build=missing")
    cmd.append(f"--output-folder=build/{platform}")
    cmd.append(f"--profile:h={host_profile}")
    cmd.append(f"--profile:b={build_profile}")
    cmd.append(f"-s build_type={build_type}")
    cmd.append(f"-s os={platform}")
    # If building for Linux, make sure Conan sets CMAKE_SYSTEM_NAME=Linux
    if platform == "Linux":
        cmd.append("-c tools.cmake.cmaketoolchain:system_name=Linux")
    c.run(" ".join(cmd))


@task
def nuke(c):
    current_folder = os.getcwd()
    build_folder = os.path.join(current_folder, "build")
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)
        print(f"Removed build folder: {build_folder}")


@task
def cmake_config(c, os="", buildtype=""):
    build_type = buildtype.lower() if buildtype else ""
    if buildtype not in {"debug", "release"}:
        raise ValueError(f"Unsupported build type: {buildtype}")

    platformValues = get_platform_values()
    if os not in platformValues:
        raise ValueError(f"Unsupported os: {os}")

    presetName = f"{os.lower()}-{build_type}"

    cmd = ["cmake . --preset", presetName]
    c.run(" ".join(cmd))


@task
def conan_all(c, clean=False):
    platformValues = get_platform_values()
    if clean:
        nuke(c)
    for platform in platformValues:
        for build_type in ["Debug", "Release"]:
            conan_install(c, platform, build_type)


@task
def configure_all(c, clean=False):
    if clean:
        nuke(c)
    conan_all(c)
    platformValues = get_platform_values()
    for os in platformValues:
        for build_type in ["debug", "release"]:
            cmake_config(c, os, build_type)


@task
def build_all(c, clean=False):
    if clean:
        nuke(c)
    configure_all(c, clean)
    platformValues = get_platform_values()    
    for os in platformValues:
        for build_type in ["debug", "release"]:
            presetName = f"{os.lower()}-{build_type}"
            print(f"presetName!!!!: {presetName}")
            cmd = ["cmake"]
            cmd.append(f"--build")
            cmd.append(f"--preset {presetName}")
            c.run(" ".join(cmd))
            
