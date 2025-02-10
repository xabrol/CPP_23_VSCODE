# Working with C++ 23 on Windows 10 and 11
> * Windows 10 requires at least version 2004 (Build 19041)
> * Windows 11 requires at least version 22000 aka 21H2, 22000.194
> * **i.e. Just have windows 10 or 11 up to date and you should be good to go**

# Build Dependencies

> For ease of this exmaple repo, everything assumes all of these will be installed and put in the system/user path where applicable, i.e. cmake, clangcl, msvc, etc

## Depedency List (install all of these)

| Name | Install Url |
|------|-------------|
| Powershell 7.5 | https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5 |
| WSL2 | [Install WSL2 Guide](./_docs/WSL2_Install_Guide.md) |
| Docker | https://docs.docker.com/desktop/setup/install/windows-install |
|| Docker is used for cross compiling with conan 2 runners, so it's necessary |
| Git SCM | https://git-scm.com/downloads/win |
| CMake | https://cmake.org/download/ |
|| **version 3.31.5 or better (get the latest under binary distributions)** |
| LLVM CLANG | https://github.com/llvm/llvm-project/releases |
|| Get the latest (non prerelease) LLVM-XX.X.X-win64.exe under assets |
|| I.e https://github.com/llvm/llvm-project/releases/download/llvmorg-19.1.7/LLVM-19.1.7-win64.exe |
| Ninja-Build | **Install via winget** | 
|| ```winget install Ninja-build.Ninja```|
| MS Build Tools | [Refer to this guide](./_docs/MSBuildTools_Install_Guide.md)
| Python Version Manager | https://github.com/pyenv-win/pyenv-win |