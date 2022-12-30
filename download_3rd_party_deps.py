import os
import platform
import requests
from zipfile import ZipFile
import tarfile


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


def unzip(zipname: str):
    with ZipFile(zipname, "r") as zip_object:
        zip_object.extractall()
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
        # TODO: remove the .whl file once extracted
    # Spleeter ML model
    download(
        url="https://github.com/deezer/spleeter/releases/download/v1.4.0/2stems.tar.gz",
        output_file="2stems.tar.gz"
    )
    untar(
        tarname="2stems.tar.gz",
        output_dir="pretrained_models/2stems"
    )


if __name__ == "__main__":
    download_spleeter()
