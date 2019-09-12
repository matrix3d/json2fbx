from FbxCommon import *
from fbx import *
import json

 # Prepare the FBX SDK.
lSdkManager, lScene = InitializeSdkObjects()
geoms=[]
mats=[]
anims=[]
name2node={}
joints=[]
name2invmatr={}
waitSkins=[]

def getChildByName(node,name):
    return null

def buildDefAnim():
    stack=FbxAnimStack.Create(lScene,"matrix3d.github.io/static")
    animlayer=FbxAnimLayer.Create(lScene,"l0")
    stack.AddMember(animlayer)
    time = FbxTime()
    for targetnode in joints:# each(var tobj:Object in anim.track) {
        tx=targetnode.LclTranslation.GetCurve(animlayer,"X",True)
        ty=targetnode.LclTranslation.GetCurve(animlayer,"Y",True)
        tz=targetnode.LclTranslation.GetCurve(animlayer,"Z",True)
        rx=targetnode.LclRotation.GetCurve(animlayer,"X",True)
        ry=targetnode.LclRotation.GetCurve(animlayer,"Y",True)
        rz=targetnode.LclRotation.GetCurve(animlayer,"Z",True)
        sx=targetnode.LclScaling.GetCurve(animlayer,"X",True)
        sy=targetnode.LclScaling.GetCurve(animlayer,"Y",True)
        sz=targetnode.LclScaling.GetCurve(animlayer,"Z",True)
        tx.KeyModifyBegin()
        ty.KeyModifyBegin()
        tz.KeyModifyBegin()
        rx.KeyModifyBegin()
        ry.KeyModifyBegin()
        rz.KeyModifyBegin()
        sx.KeyModifyBegin()
        sy.KeyModifyBegin()
        sz.KeyModifyBegin()
        trs=[targetnode.LclTranslation.Get(),targetnode.LclRotation.Get(),targetnode.LclScaling.Get()]
        time.SetSecondDouble(0)
        index=tx.KeyAdd(time)[0]
        tx.KeySet(index,time,trs[0][0],FbxAnimCurveDef.eInterpolationLinear)
        index=ty.KeyAdd(time)[0]
        ty.KeySet(index,time,trs[0][1],FbxAnimCurveDef.eInterpolationLinear)
        index=tz.KeyAdd(time)[0]
        tz.KeySet(index,time,trs[0][2],FbxAnimCurveDef.eInterpolationLinear)
        index=rx.KeyAdd(time)[0]
        rx.KeySet(index,time,trs[1][0],FbxAnimCurveDef.eInterpolationLinear)
        index=ry.KeyAdd(time)[0]
        ry.KeySet(index,time,trs[1][1],FbxAnimCurveDef.eInterpolationLinear)
        index=rz.KeyAdd(time)[0]
        rz.KeySet(index,time,trs[1][2],FbxAnimCurveDef.eInterpolationLinear)
        index=sx.KeyAdd(time)[0]
        sx.KeySet(index,time,trs[2][0],FbxAnimCurveDef.eInterpolationLinear)
        index=sy.KeyAdd(time)[0]
        sy.KeySet(index,time,trs[2][1],FbxAnimCurveDef.eInterpolationLinear)
        index=sz.KeyAdd(time)[0]
        sz.KeySet(index,time,trs[2][2],FbxAnimCurveDef.eInterpolationLinear)
        tx.KeyModifyEnd()
        ty.KeyModifyEnd()
        tz.KeyModifyEnd()
        rx.KeyModifyEnd()
        ry.KeyModifyEnd()
        rz.KeyModifyEnd()
        sx.KeyModifyEnd()
        sy.KeyModifyEnd()
        sz.KeyModifyEnd()

def buildAnim(anim,root):
    time = FbxTime()
    if not anim is None: 
        for anims in anim:
            for tname in anims["target"]:
                stack=FbxAnimStack.Create(lScene,"matrix3d.github.io")
                animlayer=FbxAnimLayer.Create(lScene,"l0")
                stack.AddMember(animlayer)
                rootnode = root.FindChild(tname)#name2node[tname]
                for tobj in anims["track"]:# each(var tobj:Object in anim.track) {
                    targetnode=root.FindChild(tobj["target"])
                    tx=targetnode.LclTranslation.GetCurve(animlayer,"X",True)
                    ty=targetnode.LclTranslation.GetCurve(animlayer,"Y",True)
                    tz=targetnode.LclTranslation.GetCurve(animlayer,"Z",True)
                    rx=targetnode.LclRotation.GetCurve(animlayer,"X",True)
                    ry=targetnode.LclRotation.GetCurve(animlayer,"Y",True)
                    rz=targetnode.LclRotation.GetCurve(animlayer,"Z",True)
                    sx=targetnode.LclScaling.GetCurve(animlayer,"X",True)
                    sy=targetnode.LclScaling.GetCurve(animlayer,"Y",True)
                    sz=targetnode.LclScaling.GetCurve(animlayer,"Z",True)
                    tx.KeyModifyBegin()
                    ty.KeyModifyBegin()
                    tz.KeyModifyBegin()
                    rx.KeyModifyBegin()
                    ry.KeyModifyBegin()
                    rz.KeyModifyBegin()
                    sx.KeyModifyBegin()
                    sy.KeyModifyBegin()
                    sz.KeyModifyBegin()
                    for fobj in tobj["frame"]:
                        trs=exeMatr(fobj["matrix"],None)
                        time.SetSecondDouble(fobj["time"])
                        index=tx.KeyAdd(time)[0]
                        tx.KeySet(index,time,trs[0][0],FbxAnimCurveDef.eInterpolationLinear)
                        index=ty.KeyAdd(time)[0]
                        ty.KeySet(index,time,trs[0][1],FbxAnimCurveDef.eInterpolationLinear)
                        index=tz.KeyAdd(time)[0]
                        tz.KeySet(index,time,trs[0][2],FbxAnimCurveDef.eInterpolationLinear)
                        index=rx.KeyAdd(time)[0]
                        rx.KeySet(index,time,trs[1][0],FbxAnimCurveDef.eInterpolationLinear)
                        index=ry.KeyAdd(time)[0]
                        ry.KeySet(index,time,trs[1][1],FbxAnimCurveDef.eInterpolationLinear)
                        index=rz.KeyAdd(time)[0]
                        rz.KeySet(index,time,trs[1][2],FbxAnimCurveDef.eInterpolationLinear)
                        index=sx.KeyAdd(time)[0]
                        sx.KeySet(index,time,trs[2][0],FbxAnimCurveDef.eInterpolationLinear)
                        index=sy.KeyAdd(time)[0]
                        sy.KeySet(index,time,trs[2][1],FbxAnimCurveDef.eInterpolationLinear)
                        index=sz.KeyAdd(time)[0]
                        sz.KeySet(index,time,trs[2][2],FbxAnimCurveDef.eInterpolationLinear)
                    tx.KeyModifyEnd()
                    ty.KeyModifyEnd()
                    tz.KeyModifyEnd()
                    rx.KeyModifyEnd()
                    ry.KeyModifyEnd()
                    rz.KeyModifyEnd()
                    sx.KeyModifyEnd()
                    sy.KeyModifyEnd()
                    sz.KeyModifyEnd()
def getFbxMatr(arr):
    matr=FbxMatrix()
    for i in range(4):
        for j in range(4):
            matr.Set(i,j,arr[i*4+j])
    return matr
def getMatrByFbxMatr(matr):
    t=FbxVector4()
    q= FbxQuaternion()
    sh=FbxVector4()
    s=FbxVector4()
    matr.GetElements(t,q,sh,s)
    amatr=FbxAMatrix()
    amatr.SetTQS(t,q,s)
    return amatr
def exeMatrByFbxMatr(matr,node):
    t=FbxVector4()
    q= FbxQuaternion()
    sh=FbxVector4()
    s=FbxVector4()
    matr.GetElements(t,q,sh,s)
    amatr=getMatrByFbxMatr(matr)
    r=amatr.GetR()
    if not node is None:
        node.LclTranslation.Set(FbxDouble3(t[0],t[1],t[2]))
        node.LclRotation.Set(FbxDouble3(r[0], r[1], r[2]))
        node.LclScaling.Set(FbxDouble3(s[0],s[1],s[2]))
    return [t,r,s]
def exeMatr(arr,node):
    matr=getFbxMatr(arr)
    return exeMatrByFbxMatr(matr,node)

def createCubeMesh(pSdkManager, pName):
    lMesh = FbxMesh.Create(pSdkManager,pName)
    s=2
    lControlPoint0 = FbxVector4(-s, -s, s)
    lControlPoint1 = FbxVector4(s, -s, s)
    lControlPoint2 = FbxVector4(s, s, s)
    lControlPoint3 = FbxVector4(-s, s, s)
    lControlPoint4 = FbxVector4(-s, -s, -s)
    lControlPoint5 = FbxVector4(s, -s, -s)
    lControlPoint6 = FbxVector4(s, s, -s)
    lControlPoint7 = FbxVector4(-s, s, -s)
    
    lMesh.InitControlPoints(24)
    lMesh.SetControlPointAt(lControlPoint0, 0)
    lMesh.SetControlPointAt(lControlPoint1, 1)
    lMesh.SetControlPointAt(lControlPoint2, 2)
    lMesh.SetControlPointAt(lControlPoint3, 3)
    lMesh.SetControlPointAt(lControlPoint1, 4)
    lMesh.SetControlPointAt(lControlPoint5, 5)
    lMesh.SetControlPointAt(lControlPoint6, 6)
    lMesh.SetControlPointAt(lControlPoint2, 7)
    lMesh.SetControlPointAt(lControlPoint5, 8)
    lMesh.SetControlPointAt(lControlPoint4, 9)
    lMesh.SetControlPointAt(lControlPoint7, 10)
    lMesh.SetControlPointAt(lControlPoint6, 11)
    lMesh.SetControlPointAt(lControlPoint4, 12)
    lMesh.SetControlPointAt(lControlPoint0, 13)
    lMesh.SetControlPointAt(lControlPoint3, 14)
    lMesh.SetControlPointAt(lControlPoint7, 15)
    lMesh.SetControlPointAt(lControlPoint3, 16)
    lMesh.SetControlPointAt(lControlPoint2, 17)
    lMesh.SetControlPointAt(lControlPoint6, 18)
    lMesh.SetControlPointAt(lControlPoint7, 19)
    lMesh.SetControlPointAt(lControlPoint1, 20)
    lMesh.SetControlPointAt(lControlPoint0, 21)
    lMesh.SetControlPointAt(lControlPoint4, 22)
    lMesh.SetControlPointAt(lControlPoint5, 23)
    lPolygonVertices = ( 0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
        12, 13, 14, 15,
        16, 17, 18, 19,
        20, 21, 22, 23 )
        
    for i in range(6):
        
        lMesh.BeginPolygon(-1, -1, False)

        for j in range(4):
            
            lMesh.AddPolygon(lPolygonVertices[i*4 + j]) 
            

        lMesh.EndPolygon()
    return lMesh

def CreateTexture(pSdkManager, pMesh,mat):
    lMaterial = None
    lNode = pMesh.GetNode()
    if lNode:
        lMaterial = lNode.GetSrcObject(FbxCriteria.ObjectType(FbxSurfacePhong.ClassId), 0)
        if not lMaterial:
            lMaterialName = "toto"
            lShadingName  = "Phong"
            lDiffuseColor = FbxDouble3(mat["d"][0], mat["d"][1],mat["d"][2])
            lAmbientColor = FbxDouble3(mat["a"][0], mat["a"][1],mat["a"][2])

            lLayer=pMesh.GetLayer(0)
            lLayerElementMaterial=FbxLayerElementMaterial.Create(pMesh,lMaterial)
            lLayerElementMaterial.SetMappingMode(FbxLayerElement.eAllSame)
            lLayerElementMaterial.SetReferenceMode(FbxLayerElement.eIndexToDirect)
            lLayer.SetMaterials(lLayerElementMaterial)
            lLayerElementMaterial.GetIndexArray().Add(0)
            lMaterial = FbxSurfacePhong.Create(pSdkManager, lMaterialName)
            lMaterial.Ambient.Set(lAmbientColor)
            lMaterial.Diffuse.Set(lDiffuseColor)
            lMaterial.ShadingModel.Set(lShadingName)

            lNode.AddMaterial(lMaterial)

    lTexture = FbxFileTexture.Create(pSdkManager,"Diffuse Texture")
    if "dmap" in mat:
        lTexture.SetFileName(mat["dmap"]) 
    lTexture.SetTextureUse(FbxTexture.eStandard)
    lTexture.SetMappingType(FbxTexture.eUV)
    lTexture.SetMaterialUse(FbxFileTexture.eModelMaterial)
    lTexture.SetSwapUV(False)
    lTexture.SetTranslation(0.0, 0.0)
    lTexture.SetScale(1.0, 1.0)
    lTexture.SetRotation(0.0, 0.0)
    if lMaterial:
        lMaterial.Diffuse.ConnectSrcObject(lTexture)

def LinkPatchToSkeleton():
    for wo in waitSkins:
        obj=wo[0]
        skinnode=wo[1]
        lSkin = FbxSkin.Create(lSdkManager, "")
        skinnode.GetNodeAttribute().AddDeformer(lSkin)
        skin=load_dict["skin"][obj["skin"]]
        geom=load_dict["geom"][obj["geom"]]
        js=skin["joint"]
        jd=geom["joint"]
        wd=geom["weight"]
        l=int(len(geom["pos"])/3)
        stepJ=int(len(jd)/l)
        clusters={}
        for i in range(l):
            for j in range(stepJ):
                jv=jd[i*stepJ+j]
                wv=wd[i*stepJ+j]
                if wv >0:
                    if not jv in clusters:
                        jname=js[jv]
                        jnode=name2node[jname]
                        cluster=FbxCluster.Create(lSdkManager,jname)
                        lSkin.AddCluster(cluster)
                        clusters[jv]=cluster
                        cluster.SetLink(jnode)
                        cluster.SetLinkMode(FbxCluster.eTotalOne)
                        #cluster.SetTransformMatrix(skinnode.EvaluateGlobalTransform())
                        cluster.SetTransformMatrix(getMatrByFbxMatr(getFbxMatr(name2invmatr[jname])))
                        #cluster.SetTransformLinkMatrix(jnode.EvaluateGlobalTransform())
                        #cluster.SetTransformMatrix(jnode.EvaluateGlobalTransform())
                        #cluster.SetTransformLinkMatrix(getMatrByFbxMatr(getFbxMatr(name2invmatr[jname])))
                    cluster=clusters[jv]
                    cluster.AddControlPointIndex(i,wv)

def parserM5(obj):
    if "geom" in obj:
        for geom in obj["geom"]:
            node=FbxMesh.Create(lSdkManager,"g")
            if "source" in geom:
                pos=geom["source"]["pos"]
                node.InitControlPoints(len(pos)/3)
                for i in range(int(len(pos)/3)):
                    node.SetControlPointAt(FbxVector4(pos[i*3],pos[i*3+1],pos[i*3+2]),i)
                for a in geom["source"]["index"]:
                    node.BeginPolygon(-1, -1, False)
                    for b in a:
                        node.AddPolygon(b)
                    node.EndPolygon()
            else:
                pos=geom["pos"]
                node.InitControlPoints(len(pos)/3)
                for i in range(int(len(pos)/3)):
                    node.SetControlPointAt(FbxVector4(pos[i*3],pos[i*3+1],pos[i*3+2]),i)
                node.CreateLayer()
                lLayer = node.GetLayer(0)
                if "norm" in geom:
                    lLayerElementNormal= FbxLayerElementNormal.Create(node, "")
                    lLayerElementNormal.SetMappingMode(FbxLayerElement.eByControlPoint)
                    lLayerElementNormal.SetReferenceMode(FbxLayerElement.eDirect)
                    norm=geom["norm"]
                    for i in range(int(len(norm)/3)):
                        lLayerElementNormal.GetDirectArray().Add(FbxVector4(norm[i*3],norm[i*3+1],norm[i*3+2]))
                    lLayer.SetNormals(lLayerElementNormal)
                lTextureDiffuseLayer=FbxLayerElementTexture.Create(node, "Diffuse Texture")
                lTextureDiffuseLayer.SetMappingMode(FbxLayerElement.eByPolygon)
                lTextureDiffuseLayer.SetReferenceMode(FbxLayerElement.eIndexToDirect)
                lLayer.SetTextures(FbxLayerElement.eTextureDiffuse, lTextureDiffuseLayer)

                lUVDiffuseLayer = FbxLayerElementUV.Create(node, "DiffuseUV")
                lUVDiffuseLayer.SetMappingMode(FbxLayerElement.eByControlPoint)
                lUVDiffuseLayer.SetReferenceMode(FbxLayerElement.eDirect)
                lLayer.SetUVs(lUVDiffuseLayer, FbxLayerElement.eTextureDiffuse)

                uv =geom["uv"]
                for i in range(int(len(uv)/2)):
                    lUVDiffuseLayer.GetDirectArray().Add(FbxVector2(uv[i*2],1-uv[i*2+1]))

                index=geom["index"]
                lUVDiffuseLayer.GetIndexArray().SetCount(len(index))
                lTextureDiffuseLayer.GetIndexArray().SetCount(int(len(index)/3))
                for i in range(int(len(index)/3)):
                    node.BeginPolygon(-1, -1, False)
                    lTextureDiffuseLayer.GetIndexArray().SetAt(i,0)
                    node.AddPolygon(index[i*3])
                    node.AddPolygon(index[i*3+2])
                    node.AddPolygon(index[i*3+1])
                    node.EndPolygon()
                geoms.append(node)
    if "mat" in obj:
        for mat in obj["mat"]:
            mats.append(mat)        
    if "anim" in obj:
        for anim in obj["anim"]:
            anims.append(anim)
    if "hierarchy" in obj:
        global target
        target = importHierarchy(obj["hierarchy"])
    if "skin" in obj:
        skins=obj["skin"]
    LinkPatchToSkeleton()
    buildDefAnim()
def importHierarchy(obj):
    node = FbxNode.Create(lSdkManager, obj["name"])
    if "isJoint" in obj:
        lSkeletonRootAttribute = FbxSkeleton.Create(lSdkManager, obj["name"])
        node.SetNodeAttribute(lSkeletonRootAttribute)
        joints.append(node)
        name2invmatr[obj["name"]]=obj["invBindMatrix"]
    exeMatr(obj["matrix"],node)
    
    if "geom" in obj:
        geom=geoms[obj["geom"]]
        node.SetNodeAttribute(geom) 
        if "mat" in obj:
            node.SetNodeAttribute(geom)
            node.SetShadingMode(FbxNode.eTextureShading)
            CreateTexture(lSdkManager, geom,mats[obj["mat"]])
    #else:
        #node.SetNodeAttribute(cubeMesh)
    if "skin" in obj:
        waitSkins.append([obj,node])

    name2node[node.GetName()] = node
    if "children" in obj:
        for c in obj["children"]:
            cnode=importHierarchy(c)
            node.AddChild(cnode)    
    if "anim" in obj:
        buildAnim(anims[obj["anim"]],node)
    return node

cubeMesh=createCubeMesh(lSdkManager,"cubemesh")

if len(sys.argv)>1:
    filepath=sys.argv[1]
else:
    filepath="mesh.json"
with open(filepath,"r") as f:
    load_dict=json.load(f)
    print(load_dict["magic"])
if load_dict["magic"]=="m5":
    parserM5(load_dict)
lRootNode = lScene.GetRootNode()
lRootNode.AddChild(target)

lResult = SaveScene(lSdkManager, lScene, filepath.replace(".json",".fbx"),lSdkManager.GetIOPluginRegistry().GetNativeWriterFormat(),True)
print(lResult)

