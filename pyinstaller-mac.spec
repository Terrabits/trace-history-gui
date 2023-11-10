# -*- mode: python ; coding: utf-8 -*-


# constants
APP_NAME = 'R&S Trace History GUI'


# names
EXE_NAME       = APP_NAME
FOLDER_NAME    = APP_NAME
MACOS_APP_NAME = f'{APP_NAME}.app'


# pyinstaller

a = Analysis(
    ['__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=EXE_NAME,
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=FOLDER_NAME,
)
app = BUNDLE(
    coll,
    name=MACOS_APP_NAME,
    icon=None,
    bundle_identifier=None,
)
