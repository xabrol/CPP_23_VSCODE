# Linux Build Depedencies Guide

## 1. Install Build Essentials

### Debian Based
```
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r) valgrind git wget curl
```


## 2. Install Clang19, Clangd19, clang-tools-19

```
sudo apt-get update
sudo apt-get install clang-19 clangd-19 clang-tools-19
```

Set Alternatives

> assuming this is where your clang-19 files installed

```
sudo update-alternatives --install /usr/bin/clang   clang   /usr/lib/llvm-19/bin/clang   100
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-19/bin/clang++ 100
sudo update-alternatives --install /usr/bin/clangd  clangd  /usr/lib/llvm-19/bin/clangd  100

sudo update-alternatives --config clang
sudo update-alternatives --config clang++
sudo update-alternatives --config clangd
```
That puts clang 19 as the current clang, clang++, clangd commands

Check and verify clang in path is version 19

```
clang --version
```
## 3. Install Clang Tools 19 (Super important for modules as it incldues clang-scan-deps)

```
sudo apt update
sudo apt install clang-tools-19
```

## 4. Install CMake 3.3+ (atm 3.28 is the highest version with a package on many repos)

### Debian Based

```
wget https://cmake.org/files/v3.31/cmake-3.31.5-linux-x86_64.sh
chmod +x cmake-3.31.5-linux-x86_64.sh
sudo ./cmake-3.31.5-linux-x86_64.sh --skip-license --prefix=/usr/local
```

## 5. Install Ninja Build

### Debian Based

```
sudo apt update
sudo apt install ninja-build
```

## 6. Install PyEnv

```
curl -fsSL https://pyenv.run | bash
```