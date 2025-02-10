# MS Build Tools - Guide

## Why?

You need the MSBuild Tools (even when using Clang, CMake, and Ninja) because:

* It provides the Windows SDK and system libraries.
* It includes necessary linkers and runtime libraries.
* CMake and Ninja expect MSVC tooling for a proper Windows build environment.
* The Clang toolchain on Windows is designed to interoperate with MSVC libraries and linking.

# Install the MSBuild Tools

Download the MS Build Tools Visual Studio Installer from: https://visualstudio.microsoft.com/downloads/?q=build+tools

> Scroll down to Tools for Visual Studio "Build Tools for Visual Studio 2022"

Run the installer and when you get to the screen where you can install options for the build tools make sure the following are checked:

* MSVC v143 - VS 2022 C++ x64/x86 build...
* Windows 11 SDK (10.0.22621.0) or newer
* C++ Cmake tools for windows
* Testing tools core features - Build Tools
* C++ AddressSanitizer

Optional:

* Older Windows 11 sdk's
* Windows 10 sdks (if on windows 11)
* Older versions of MSVC (not recommended unless you have legacy code), having these installed and in paths can complicate tools that rely on "find" scripts to find tooling and require manually specifying versions/paths to msvc v143.


> This is all you need, you don't need "Visual Studio" but you can also install Visual Studio 2022 if you want to.