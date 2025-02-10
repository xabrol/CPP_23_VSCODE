# Linux Build Depedencies Guide

## 1. Install Build Essentials

### Debian Based
```
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r) valgrind git wget curl
```


## 2. Install LLVM via sh script

```
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 19.1.7
```

Set alternatives for clang 19

```
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-19 100
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-19 100
sudo update-alternatives --config clang
sudo update-alternatives --config clang++
```

> Note: the conan profile for linux in this project expects clang-19 and clang++-19 in /usr/bin, the llvm sh install script does that for you.  Conan will not be able to generate the cmake/presets and build files if clang 19 is not in /usr/bin, if it's elsewhere you need to update the profile in profiles/linux_host

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