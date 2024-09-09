# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['slot_logic.py'],
    pathex=['/home/qjz/Downloads/qtDesign'],
    binaries=[
            ('/home/qjz/anaconda3/envs/RL/lib/python3.8/site-packages/tvm-0.17.dev170+g4a5e22e86-py3.8-linux-x86_64.egg/tvm/libtvm.so', '.'),
            ('/home/qjz/anaconda3/envs/RL/lib/python3.8/site-packages/tvm-0.17.dev170+g4a5e22e86-py3.8-linux-x86_64.egg/tvm/libtvm_runtime.so', '.'),
            ('/home/qjz/anaconda3/envs/RL/lib/python3.8/site-packages/xgboost/lib/libxgboost.so', '.')
            ],
    datas=[],
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
    name='upload_model',
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
