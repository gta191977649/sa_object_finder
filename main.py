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
def readFileFromData(id):
    os.chdir("D:/dev/sa_object_finder/data/all/")
    for file in glob.glob("*.ipl"):
        path = "D:/dev/sa_object_finder/data/all/"+file
        findModelEntryInIDE(id, path)
if __name__ == '__main__':
    #SA_HOME = "D:\\game\\GTA San Andreas\\"
    #loadDat(7312,SA_HOME)
    items = [
        2318,
        2312,
        2317,
        2316,
        2320,
        2322,
        1783,
        1788,
        1790,
        2103,
        2102,
        2226,
        1809,
        2101,
        1719,
        2028,
        2149,
    ]
    for id in items:
        readFileFromData(id)


    for item in FoundTable:
        model = item[0]
        dff = item[1]
        int = item[2]
        x = item[3]
        y = item[4]
        z = item[5]
        qx = float(item[6])
        qy = float(item[7])
        qz = float(item[8])
        qw = float(item[9])
        rx,ry,rz = quaternionToYawPitchRoll(qw, qx, qy, qz)
        print("{} {} {} {} {} {} {} {}".format(model,x,y,z,rx,ry,rz,int))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
