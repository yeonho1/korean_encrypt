# -*- mode: python -*-

block_cipher = None


a = Analysis(['qtgui_dec.py'],
             pathex=['C:\\Users\\Yeonho\\korean_encrypt'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='qtgui_dec',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
