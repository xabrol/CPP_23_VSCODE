> Note: This git project is an example of working with c++23 and c++23 standard modules assuming the following:
> * You are developing on windows or a debian based linux distro as your build host
> * You have all the build requirements installed for the relevant build host
> * You are using VSCode and have the necessary extensions installed

# Windows Users - (Building and Developing ON windows)

[Review the depedencies you need to install](./_docs/windows_depedencies.md)

# Debian Based Linux Users  - (Building and Developing ON a Debian Based Linux Distro)

[Review the dependencies you need to install](./_docs/linux_depedencies.md)

## 1. Clone the Project

> Assume you know how to use git and ssh keys on windows/linux

```
git clone git@github.com:xabrol/WINHOST_CPP_23_VSCODE.git
```

## 2. Open the project in vscode

## 3. Install recommended VSCode extensions

You should get a popup to install the recomended extensions, but if not you can find them in the .vscode/extensions.json file in the project.

The following extensions are required for llvm/clang/clangd development in vscode

```      
      "ms-vscode.cpptools",
      "ms-vscode.cpptools-extension-pack",
      "xaver.clang-format",
      "llvm-vs-code-extensions.vscode-clangd",
      "twxs.cmake",
      "ms-vscode.cmake-tools",      
```

The following extensions are further highly recommended

```
    "ms-python.black-formatter",
    "ms-azuretools.vscode-docker",
    "editorconfig.editorconfig",
    "shd101wyy.markdown-preview-enhanced",
    "esbenp.prettier-vscode",
    "ms-python.vscode-pylance",
    "ms-python.python",
    "ms-python.debugpy",
    "ms-vscode-remote.remote-wsl",
    "robertostermann.better-status-bar"    
```

> ** Note: The cpp intellisense engine conflicts with clangd, so it has to be turned off in vscode settings, this project already does that for you in .vscode/settings ** 

# Use the integrated terminal from here on out in vscode

## 4. Install python 3.11

```
pyenv install 3.11
```

## 5. Create the python virtual env

```
pyenv local 3.11
python -m venv .venv
```

Source into python

### On Linux

```
source ./.venv/bin/activate
```

### On Windows

```
"./.venv/scripts/activate"
```

## 6. Install Python requirements

```
pip install -r requirements.txt
```

## 7. Run invoke to install conan and do cmake configures

```
invoke configure-all
```

## 8. Try building everything

```
invoke build-all
```

---

# Notes

At this point you should be able to build.  Tasks are already setup in vscode for this if you use "run task" in the command pallet or via better status bar (recommended extension) you can do conan install and builds from tasks.

But also, CMake tools automatically picks up the build commands for debug and release so the run/debug buttons in vscode should just automatically work.  But we can add launch.json entries to do the builds to which give you more options for run/debug menu in vscode.

If you use "debug" looks like a debug, you should be able to breakpoint and step through the example program in src/example

More docs comming if needed, this repo is a work in progress.

