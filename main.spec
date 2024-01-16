# -*- mode: python ; coding: utf-8 -*-

import sys

block_cipher = None

icon = "resources/app_icon.icns" if sys.platform == "darwin" else "resources/app_icon.ico"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("resources", "resources"),
        ("lang/*.qm", "lang"),
        ("gui/*.py", "gui"),
        ("storage", "storage"),
        ("theme", "theme")
    ],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='AR Intercom',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
