# 🔇 Music remover

Removes the music from an audio file, so that only the voices remain.

This API was built for [Moubah](https://github.com/karim-bouchez/moubah).


## 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)


## 🔧 Setup

> **_For Windows users:_** use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

<!-- TODO: check if we cannot install requirements.txt first, then install the rest -->

Create and active a virtual environment:
```bash
python3.8 -m venv .venv
source .venv/bin/activate
```

Upgrade pip: _(add `arch -x86_64` at the beginning for Mac with Apple silicon)_
```bash
pip install --upgrade pip
```

Download 3rd party dependencies:
```bash
pip install requests
python download_3rd_party_deps.py
```

Install Spleeter manually:

 + for Mac with Apple silicon:
```bash
arch -x86_64 pip install --upgrade spleeter-2.3.0b0-cp38-cp38-macosx_11_0_x86_64.whl
```
 + for other platforms:
```bash
pip install spleeter
```

Install other libraries: _(add `arch -x86_64` at the beginning for Mac with Apple silicon)_
```bash
pip install -r requirements.txt
```

Generate gRPC code:
```bash
python -m grpc_tools.protoc -Isrc/protobuf --python_out=src/protobuf --grpc_python_out=src/protobuf src/protobuf/moubah.proto
```


## 🐍 Run it with Python

_(add `arch -x86_64` just before `python` for Mac with Apple silicon)_
```bash
(arch -x86_64) python src/grpc_server.py
```


## 📦 Create an executable file


For the first time:
+ on Mac: _(add `arch -x86_64` at the beginning for Mac with Apple silicon)_
```bash
pyinstaller app.py --noconfirm --add-data "pretrained_models:pretrained_models" --add-data "ff*:." --collect-data librosa
```

+ on Windows:
```bash
pyinstaller app.py --noconfirm --add-data "pretrained_models;pretrained_models" --add-data "ff*;." --collect-data librosa
```

Then, the next times, the `app.spec` can be use like this: _(add `arch -x86_64` at the beginning for Mac with apple silicon)_
```bash
pyinstaller app.spec --noconfirm --clean
```


## ☄️ Run the executable file

+ on Mac: _(no need for `arch -x86_64`)_
```bash
./dist/app/app
```

+ on Windows:
```bash
TODO
```

## 🎯 To-do list

- [ ] 🧼 Clean: use strict version from `spleeter`
- [ ] 🧼 Clean: use [static-ffmpeg](https://pypi.org/project/static-ffmpeg/)
- [ ] 🆕 Feature: add progress status or infos on downloading 3rd party
