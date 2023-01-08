<h1 align="center">
    🔇 Music remover</br>
    🚧 (WIP) 🚧 </br>
</h1>
</br>

## ℹ️ Description

Removes the music from an audio file, so that only the voices remain.

This API was built for [Moubah](https://github.com/karim-bouchez/moubah).

</br>

## 💻 Tech Stack:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![gRPC](https://img.shields.io/badge/gRPC-244c5a.svg?style=for-the-badge&logoColor=white)

</br>

## 🔗 Prerequisite

-   [Python 3.8](https://www.python.org/downloads/release/python-3810/)

</br>

## 🔧 Setup

> _**On Windows:** use `.exe` (PowerShell recommended)_

> _**On Mac with Apple chip:** use `arch -x86_64` at the beginning of the command when indicated_

<!-- TODO: check if we cannot install requirements.txt first, then install the rest -->

Check that Python3.8 is correctly installed:

```bash
python3.8 --version
```

> You may just have to use `python.exe --version`, without `3.8` on Windows

</br>

If you came from [Moubah](https://github.com/karim-bouchez/moubah), make sure that the submodule is correctly imported:

```bash
git submodule update --init
```

Otherwise, just clone the repo:

```bash
git clone git@github.com:karim-bouchez/music-remover.git
```

And make sure you are in the `music-remover` directory:
```bash
pwd
```

</br>

Create and active a virtual environment:

```bash
# On UNIX OS:
python3.8 -m venv .venv
source .venv/bin/activate

# On Windows OS:
python3.8.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
```

</br>

Upgrade pip:

```bash
[arch -x86_64] python[.exe] -m pip install --upgrade pip
```

> If `ModuleNotFoundError: No module named 'pip'` error --> run `python[.exe] -m ensurepip`

</br>

Download 3rd party dependencies:

```bash
python[.exe] -m pip install requests
python[.exe] download_3rd_party_deps.py
```

> If `No such file or directory` error --> run `git submodule update --init`

</br>

Install Spleeter manually:

-   for Mac with Apple silicon:

```bash
arch -x86_64 python -m pip install --upgrade spleeter-2.3.0b0-cp38-cp38-macosx_11_0_x86_64.whl
```

-   for other platforms:

```bash
python[.exe] -m pip install spleeter
```

</br>

<!-- TODO: check if we really have to add arch -x86_64 everywhere -->

Install other libraries:

```bash
[arch -x86_64] python[.exe] -m pip install -r requirements.txt
```

</br>

~~Generate gRPC code:~~ TODO karim: store these files in Github and move this command in ~ "Contribution"

```bash
[arch -x86_64] python[.exe] -m grpc_tools.protoc --proto_path=src/protobuf --python_out=. --grpc_python_out=. src/protobuf/moubah.proto
```

</br>

## 🐍 Run it with Python

```bash
[arch -x86_64] python[.exe] app.py --host localhost --port 46471
```

</br>

## 🚀 Test it with Postman

You can access to the workspace [here](https://www.postman.com/warped-moon-691802/workspace/moubah/overview)

</br>

## 📦 Create an executable file

```bash
[arch -x86_64] pyinstaller[.exe] app.spec --noconfirm --clean
```

</br>

## ☄️ Run the executable file

-   ~~on Mac: _(no need for `arch -x86_64`)_~~ (not working right now)

```bash
./dist/app/app --host localhost --port 46471
```

> **Apple Silicon**: the executable file doesn't currently work<br>
> Error thrown: 
> ```bash
> malloc: Incorrect checksum for freed object 0x7f7a43d24280: probably modified after being freed.
> malloc: *** set a breakpoint in malloc_error_break to debug
> ```

-   on Windows:

```bash
.\dist\music-remover.exe --host localhost --port 46471
```

</br>

## 🎯 To-do list

-   [ ] 🆕 fake a first request to avoid cold start and so the real first request is quick
-   [ ] 🧼 Clean: use strict version from `spleeter`
-   [x] 🧼 Clean: use [static-ffmpeg](https://pypi.org/project/static-ffmpeg/)
-   [ ] 🆕 Feature: add progress status or infos on downloading 3rd party
