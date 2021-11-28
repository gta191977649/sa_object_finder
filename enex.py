import glob, os

def readEnexSection(path):
    f = open(path)
    lines = f.readlines()
    flag = False
    for l in lines:
        l = l.strip()
        if "end" in l:
            flag = False
        if flag:
            print(l)
        if "enex" in l:
            flag = True



if __name__ == '__main__':
    os.chdir("./data/all")
    for file in glob.glob("*.ipl"):
        path = "D:/dev/sa_object_finder/data/all/" + file
        readEnexSection(path)