<h1 align="center">
    🔇 Music remover</br>
    🚧 (WIP) 🚧 </br>
</h1>
</br>

## Description

Removes the music from an audio file, so that only the voices remain.

This API was built for [Moubah](https://github.com/karim-bouchez/moubah).

## 💻 Tech Stack:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

## 🔧 Setup

> _**On Windows:** use `.exe` (PowerShell recommended)_

> _**On Mac with Apple chip:** use `arch -x86_64` at the beginning of the command when indicated_

<!-- TODO: check if we cannot install requirements.txt first, then install the rest -->

Download [Python 3.8](https://www.python.org/downloads/release/python-3810/) if it's not already installed
and check that everything is ok:

```bash
python3.8 --version
```

> You may just have to use `python.exe --version`, without `3.8` on Windows

Make sure that the submodule is correctly imported:

```bash
git submodule update --init
```

Create and active a virtual environment:

```bash
# On UNIX OS:
python3.8 -m venv .venv
source .venv/bin/activate

# On Windows OS:
python3.8.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade pip: _(add `arch -x86_64` at the beginning for Mac with Apple silicon)_

```bash
[arch -x86_64] python[.exe] -m pip install --upgrade pip [--user]  # Not sure if --user is really needed
```

> If `ModuleNotFoundError: No module named 'pip'` error --> run `python[.exe] -m ensurepip`

Download 3rd party dependencies:

```bash
python[.exe] -m pip install requests
python[.exe] download_3rd_party_deps.py
```

> If `No such file or directory` error --> run `git submodule update --init`

Install Spleeter manually:

-   for Mac with Apple silicon:

```bash
arch -x86_64 python -m pip install --upgrade spleeter-2.3.0b0-cp38-cp38-macosx_11_0_x86_64.whl
```

-   for other platforms:

```bash
python[.exe] -m pip install spleeter
```

<!-- TODO: check if we really have to add arch -x86_64 everywhere -->

Install other libraries: _(add `arch -x86_64` at the beginning for Mac with Apple silicon)_

```bash
[arch -x86_64] python[.exe] -m pip install -r requirements.txt
```

~~Generate gRPC code:~~ TODO: store these files in Github and move this command in ~ "Contribution"

```bash
[arch -x86_64] python[.exe] -m python -m grpc_tools.protoc --proto_path=src/protobuf --python_out=. --grpc_python_out=. src/protobuf/moubah.proto
```

## 🐍 Run it with Python

_(add `arch -x86_64` just before `python` for Mac with Apple silicon)_

```bash
[arch -x86_64] python[.exe] app.py
```

## 📦 Create an executable file

_(add `arch -x86_64` at the beginning for Mac with apple silicon)_

```bash
[arch -x86_64] pyinstaller[.exe] app.spec --noconfirm --clean
```

> Apple Silicon: the executable file doesn't currently work (_TODO: add the error thrown_)

## ☄️ Run the executable file

-   ~~on Mac: _(no need for `arch -x86_64`)_~~ (not working right now)

```bash
./dist/app/app
```

-   on Windows:

```bash
TODO
```

## 🎯 To-do list

-   [ ] 🆕 fake a first request to avoid cold start and so the real first request is quick
-   [ ] 🧼 Clean: use strict version from `spleeter`
-   [x] 🧼 Clean: use [static-ffmpeg](https://pypi.org/project/static-ffmpeg/)
-   [ ] 🆕 Feature: add progress status or infos on downloading 3rd party
