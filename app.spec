# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

datas = []
binaries = []
hiddenimports = []

# TODO: clean here. Not all of this is required
tmp_ret = collect_all('librosa')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('static_ffmpeg')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('spleeter')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('scipy')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=binaries,
    datas=datas+[
        (
            "pretrained_models",
            "pretrained_models"
        ),
        (
            "src",
            "src"
        ),
        (
            "moubah_pb2*",
            "."
        ),
    ],
    hiddenimports=hiddenimports+[
        "google.protobuf.empty_pb2",
        "sklearn.metrics._pairwise_distances_reduction._datasets_pair",
        "sklearn.metrics._pairwise_distances_reduction._middle_term_computer"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    # Comment these 3 next lines to have access to the files within the executable file
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    # Uncomment this to have access to the files within the executable file
    # exclude_binaries=True,
    name='music-remover',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    # Comment these 2 next lines to have access to the files within the executable file
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# Uncomment this to have access to the files within the executable file
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='app',
# )
