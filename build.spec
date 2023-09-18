# -*- mode: python ; coding: utf-8 -*-

# 这个变量是用来加密你的代码的，如果不需要加密，可以设置为None
block_cipher = None

# 这个类是用来分析你的项目的导入和依赖的，你需要传入你的主脚本和一些其他参数
a = Analysis(['main.py'],
             # 这个参数是用来设置你的项目的路径，如果你有一些模块不在这个路径下，可以添加到这个列表中
             pathex=['controllers'],
             # 这个参数是用来添加一些二进制文件，比如DLL或者SO文件，格式是一个元素为元组的列表，每个元组有两个元素，第一个是文件路径，第二个是运行时的位置
             binaries=[],
             # 这个参数是用来添加一些数据文件或者文件夹，比如图片、音频、字体等，格式和binaries一样
             datas=[],
             # 这个参数是用来添加一些隐式导入的模块，比如使用__import__或者eval等动态导入的模块，格式是一个字符串列表
             hiddenimports=[],
             # 这个参数是用来指定一些额外的hook文件的路径，hook文件是用来改变一些库的导入逻辑的，格式是一个字符串列表
             hookspath=[],
             # 这个参数是用来指定一些运行时hook文件的路径，在打包后的程序运行时会在所有代码之前执行这些hook文件，格式是一个字符串列表
             runtime_hooks=[],
             # 这个参数是用来指定一些可以被忽略的模块或者包，比如一些不需要的或者冲突的模块，格式是一个字符串列表
             excludes=[],
             # 这个参数是用来设置是否使用Windows重定向机制，默认为False
             win_no_prefer_redirects=False,
             # 这个参数是用来设置是否使用Windows私有程序集，默认为False
             win_private_assemblies=False,
             # 这个参数是用来设置是否使用加密密钥，默认为None
             cipher=block_cipher,
             # 这个参数是用来设置是否不使用归档，默认为False
             noarchive=False)

# 这个类是用来创建一个.pyz文件，它包含了所有分析后的纯Python模块
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# 这个类是用来创建最终的可执行文件，它处理了分析和.pyz文件的结果，并且可以设置一些其他参数
exe = EXE(pyz,
          a.scripts,  # 这个参数是用来指定主脚本文件
          a.binaries, # 这个参数是用来指定二进制文件
          a.zipfiles, # 这个参数是用来指定zip文件
          a.datas,    # 这个参数是用来指定数据文件
          [],         # 这个参数是保留给COLLECT类使用的
          name='my_project',  # 这个参数是用来指定生成的可执行文件的名字
          debug=False,        # 这个参数是用来设置是否生成调试版本的可执行文件，默认为False
          bootloader_ignore_signals=False,  # 这个参数是用来设置是否忽略信号，默认为False
          strip=False,         # 这个参数是用来设置是否去除可执行文件中的符号表，默认为False
          upx=True,            # 这个参数是用来设置是否使用UPX工具压缩可执行文件，默认为True
          upx_exclude=[],      # 这个参数是用来设置哪些文件不被UPX压缩，格式是一个字符串列表
          runtime_tmpdir=None, # 这个参数是用来设置运行时的临时目录，默认为None，表示使用系统的临时目录
          console=False,       # 这个参数是用来设置是否显示控制台窗口，默认为True
          icon='icon.ico')     # 这个参数是用来设置可执行文件的图标，默认为None

# 这个类是用来创建一个输出目录，它包含了所有的文件和文件夹，如果使用了-F参数，就不需要这个类
# coll = COLLECT(exe,
#                a.binaries,
#                a.zipfiles,
#                a.datas,
#                strip=False,
#                upx=True,
#                upx_exclude=[],
#                name='my_project')
