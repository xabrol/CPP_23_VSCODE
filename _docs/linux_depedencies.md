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

## 3. Install CMake 3.3+ (atm 3.28 is the highest version with a package on many repos)

### Debian Based

```
wget https://cmake.org/files/v3.31/cmake-3.31.5-linux-x86_64.sh
chmod +x cmake-3.31.5-linux-x86_64.sh
sudo ./cmake-3.31.5-linux-x86_64.sh --skip-license --prefix=/usr/local
```

## 4. Install Ninja Build

### Debian Based

```
sudo apt update
sudo apt install ninja-build
```

## 5. Install PyEnv

```
curl -fsSL https://pyenv.run | bash
```