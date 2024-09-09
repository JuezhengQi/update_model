# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['slot_logic.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/qjz/tvm/python/tvm/libtvm.so', './tvm'), ('/home/qjz/tvm/python/tvm/libtvm_runtime.so', './tvm')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='slot_logic',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
