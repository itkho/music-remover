# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        (
            "pretrained_models",
            "pretrained_models"
        ),

        # TODO: use hook for this because path can defer depending the
        
        # Uncomment for UNIX (Mac/Linux)
        (
            ".venv/lib/python3.8/site-packages/static_ffmpeg",
            "static_ffmpeg"
        ),
        (
            ".venv/lib/python3.8/site-packages/librosa",
            "librosa"
        ),
        (
            ".venv/lib/python3.8/site-packages/spleeter",
            "spleeter"
        )

        # Uncomment for Windows
        # (
        #     ".venv\Lib\site-packages\static_ffmpeg",
        #     "static_ffmpeg"
        # ),
        # (
        #     ".venv\Lib\site-packages\librosa",
        #     "librosa"
        # ),
        # (
        #     ".venv\Lib\site-packages\spleeter",
        #     "spleeter"
        # )
    ],
    hiddenimports=[
        # Doesn't seem to work
        #"static_ffmpeg",
        #"librosa",
        #"spleeter",
        
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
    # a.binaries,
    # a.zipfiles,
    # a.datas,
    [],
    # Uncomment this to have access to the files within the executable file
    exclude_binaries=True,
    name='music-remover',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    # Comment these 2 next lines to have access to the files within the executable file
    # upx_exclude=[],
    # runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# Uncomment this to have access to the files within the executable file
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
