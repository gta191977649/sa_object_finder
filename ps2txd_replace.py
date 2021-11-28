import math
import glob, os


FoundTable = []
def CompressRotation(rotation):
	return rotation - math.floor(rotation/360.0)*360.0

def quaternionToYawPitchRoll(qw,qx,qy,qz):
    asin = 2 * qy * qz - 2 * qx * qw
    if asin > 1:
        asin = 1
    elif asin < -1:
        asin = -1

    rx = CompressRotation(math.asin(asin)  * 180 / math.pi );
    ry = CompressRotation(-math.atan2(qx*qz+qy*qw,0.5-qx*qx-qy*qy) * 180 / math.pi);
    rz = CompressRotation(-math.atan2(qx*qy+qz*qw,0.5-qx*qx-qz*qz)  * 180 / math.pi);
    return (round(rx,4),round(ry,4),round(rz,4))

def loadDat(id,path):
    f = open(path+"/data/gta.dat","r")
    Lines = f.readlines()
    for l in Lines:
        files = l.split(" ")
        if files and files[0] == "IPL":
            ipl = files[1].strip()
            findModelEntryInIDE(id,path+"/"+ipl.replace("\\","/"))

def findModelEntryInIDE(id,path):
    print("READ IPL: {}".format(path))
    f = open(path, "r")
    Lines = f.readlines()
    tag = False
    for l in Lines:
        if l.strip() == "end":
            tag = False
        if tag:
            param = l.split(",")
            model = param[0]
            dff = param[1]
            if int(model) == int(id):
                FoundTable.append(l.replace(","," ").split())
                #print(l.split())
        if l.strip() == "inst":
            tag = True
# Press the green button in the gutter to run the script.
def readFileFromData(txdName):
    os.chdir("D:\\dev\\sa_object_finder\\data\\all_ide")
    for file in glob.glob("*.ide"):
        path = "D:/dev/sa_object_finder/data/all_ide/"+file
        findTxdEntryInIDE(txdName,path)
        print(path)
def findTxdEntryInIDE(txdName,path):
    print("READ IDE: {}".format(path))
    f = open(path, "r")
    Lines = f.readlines()
    tag = False
    for l in Lines:
        if l.strip() == "end":
            tag = False
        if tag:
            param = l.split(",")
            model = param[0].strip()
            dff = param[1].lower().strip()
            txd = param[2].strip()
            if txd == txdName.strip():
                #FoundTable.append("{},{},{}".format(model,dff,txd))
                FoundTable.append({"dff":dff,"txd":txd})
                #FoundTable.append(dff+".dff")

                #print(l.split())
        if l.strip() == "objs":
            tag = True
if __name__ == '__main__':
    SA_HOME = "D:\\game\\GTA San Andreas\\"
    #loadDat(1978,SA_HOME)
    os.chdir("C:\\Users\\gta19\\Desktop\\txd")
    for file in glob.glob("*.txd"):
        file = file.replace(".txd","")
        readFileFromData(file)

    for item in FoundTable:
        print("<file src=\"data/img/{}.dff\"/>".format(item["dff"]))
        print("<file src=\"data/img/{}.txd\"/>".format(item["txd"]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
