from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
INCLUDES = ["fbxsip"]

options = {
    "py2exe" :
        {
            "compressed" : 1, # 压缩   
            "optimize" : 2,
            "bundle_files" : 1, # 所有文件打包成一个 exe 文件  
            "includes" : INCLUDES,
            "dll_excludes" : ["MSVCR100.dll"]
        }
}

setup(
    options=options,    
    description = "json2fbx",   
    zipfile=None,
    #console = [{"script":'Json2fbx.py'}])
    console = [{"script":'Json2fbx.py',"icon_resources":[(1,"favicon.ico")]}])