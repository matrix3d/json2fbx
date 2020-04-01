# json2fbx
可以把smd格式直接转换成fbx

第一步用https://github.com/matrix3d/FlashShader/blob/master/example/src/ModelViewer.as
这个库把smd转成json格式。然后用这个json2fbx.py脚本将mesh.json转成fbx文件。

需要根据这里的方法安装必要环境
https://matrix3d.github.io/fbx/2019/08/25/fbxsdk

用py2exe打包，用http://www.xiconeditor.com/ 生成ico

###model3d

http://lizhi.gitee.io/idewww/model3d/model3d.exe
