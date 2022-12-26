import os
import platform
from typing import Optional
import requests
from zipfile import ZipFile
import subprocess
import tarfile
import glob
import shutil

# TODO: handle Windows case
is_mac_m1 = False
if platform.system().lower() == "darwin":
    current_os = "mac"
    if platform.machine().lower() == "arm64": is_mac_m1 = True
elif platform.system() == "windows":
    current_os = "win"
# TODO: support Linux because of WSL
elif platform.system().lower() == "linux" and "microsoft" in platform.uname().release.lower():
    current_os = "win"
else:
    raise SystemExit(f"OS not supported yet ({platform.system()})")


def download(url: str, output_file: str) -> None:
    allowed_extensions = ("zip", "tar.gz")
    if not url.endswith(allowed_extensions):
        raise ValueError(f"File extension must be in: {allowed_extensions}")
    # Save zipped file locally
    with open(output_file, "wb") as file:
        file.write(requests.get(url).content)


def unzip(zipname: str, output_path: Optional[str] = None, executable_filename: Optional[str] = None):
    with ZipFile(zipname, "r") as zip_object:
        zip_object.extractall(path=output_path)
    if executable_filename:
        if output_path:
            executable_filename = f"{output_path}/{executable_filename}"
        subprocess.call(["chmod", "u+x", executable_filename])
    os.remove(zipname)


def untar(tarname: str, output_dir: str):
    tar = tarfile.open(tarname, "r:gz")
    tar.extractall(output_dir)
    tar.close()
    os.remove(tarname)


def download_spleeter():
    if is_mac_m1:
        # Spleeter wheel
        download(
            url="https://github.com/deezer/spleeter/files/7936622/spleeter-2.3.0b0-cp38-cp38-macosx_11_0_x86_64.whl.zip",
            output_file="spleeter.whl.zip"
        )
        unzip(
            zipname="spleeter.whl.zip",
        )
        # TODO: remove the .whl file
    # Spleeter ML model
    download(
        url="https://github.com/deezer/spleeter/releases/download/v1.4.0/2stems.tar.gz",
        output_file="2stems.tar.gz"
    )
    untar(
        tarname="2stems.tar.gz",
        output_dir="pretrained_models/2stems"
    )


def download_ffmpeg():
    if current_os == "mac":
        download(
            url="https://evermeet.cx/ffmpeg/getrelease/zip",
            output_file="ffmpeg.zip"
        )
        unzip(
            zipname="ffmpeg.zip",
            output_path="third_party",
            executable_filename="ffmpeg"
        )
        download(
            url="https://evermeet.cx/ffmpeg/getrelease/ffprobe/zip",
            output_file="ffprobe.zip"
        )
        unzip(
            zipname="ffprobe.zip",
            output_path="third_party",
            executable_filename="ffprobe"
        )
    elif current_os == "win":
        download(
            url="https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
            output_file="ffmpeg.zip"
        )
        unzip(
            zipname="ffmpeg.zip",
            output_path=".",
        )
        # Keep only ffmpeg and ffprobe
        for file in glob.glob("ffmpeg*/bin/ff[mp][pr]*.exe"):
            os.rename(file, os.path.join("third_party/win/ffmpeg", os.path.basename(file)))
        shutil.rmtree(glob.glob("ffmpeg*")[0])



if __name__ == "__main__":
    download_spleeter()
    download_ffmpeg()
