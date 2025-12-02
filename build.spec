# -*- mode: python ; coding: utf-8 -*-

import PyInstaller.__main__
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.win32.versioninfo import (
    VSVersionInfo,
    FixedFileInfo,
    StringFileInfo,
    StringTable,
    StringStruct,
    VarFileInfo,
    VarStruct
)

GAME_PARAM = '-game=build\datafiles\GB.win'

block_cipher = None

a = Analysis(
    ['ScriptEngine.py'],
    pathex=[],
    binaries=[],
    datas=[('libs', '.'), (r'Data\Options\windows\Icons', r'Data\Options\windows\Icons')],
    hiddenimports=['utils.res.ResourceManager', 'utils.simplegml.Interpreter'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

version = VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(1, 0, 0, 0),
        prodvers=(1, 0, 0, 0),
        mask=0x3F,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([
            StringTable(
                u'040904B0',
                [
                    StringStruct(u'CompanyName', u''),
                    StringStruct(u'FileDescription', u'Made in Constructor ToolMaker'),
                    StringStruct(u'FileVersion', u'1.0.0.0'),
                    StringStruct(u'InternalName', u'Runner'),
                    StringStruct(u'LegalCopyright', u'(c) ThreeGuysTeam'),
                    StringStruct(u'OriginalFilename', u'Runner.exe'),
                    StringStruct(u'ProductName', u'Runner'),
                    StringStruct(u'ProductVersion', u'1.0.0.0')
                ]
            )
        ]),
        VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
    ]
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Runner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    version=version,
    icon="Data\Options\windows\Icons\Icon.ico"
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Runner',
    outdir='build\libs'
)
