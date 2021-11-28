import glob, os
TextureTable = []
PS2_IMG = "D:\\dev\\sa_ps2\\PS2 Feels SA Edition\\PS2 Feels Default\\models\\gta3.img"
output = ""
meta = ""
txds = []
def loadDat(id,path):
    f = open(path+"/data/gta.dat","r")
    Lines = f.readlines()
    for l in Lines:
        files = l.split(" ")
        if files and files[0] == "IPL":
            ipl = files[1].strip()
            findModelEntryInIDE(id,path+"/"+ipl.replace("\\","/"))

def findModelEntryInIDE(path):
    global output,meta,txds
    print("READ IDE: {}".format(path))
    f = open(path, "r")
    Lines = f.readlines()
    tag = False
    lastTxd = ""
    for l in Lines:
        if l.strip() == "end":
            tag = False
        if tag:
            param = l.split(",")
            id = param[0]
            dff = param[1].strip()
            txd = param[2].strip()
            dis = param[3].strip()
            print(PS2_IMG+"/"+txd+".txd")
            if os.path.exists(PS2_IMG+"/"+txd+".txd") and float(dis) <= 300: #skip lods
                output = output + "{},{}.txd\n".format(id,txd)
                if not txd.lower() in txds:
                    meta = meta + "<file src=\"data/txd/{}.txd\" type=\"client\"/>\n".format(txd.lower())
                    txds.append(txd.lower())
                """ 
                TextureTable.append({
                    "id": id,
                    "dff": dff,
                    "txd": txd
                })
                """
        if l.strip() == "objs":
            tag = True
# Press the green button in the gutter to run the script.
def readFileFromData():
    os.chdir("./data/ide")
    for file in glob.glob("*.ide"):
        path = "D:/dev/sa_object_finder/data/ide/"+file
        findModelEntryInIDE(path)
if __name__ == '__main__':
    readFileFromData()
    f = open("D:/dev/sa_object_finder/ps2_txd.txt","w")
    f.write(output)
    f.close()
    f = open("D:/dev/sa_object_finder/meta.txt","w")
    f.write(meta)
    f.close()

