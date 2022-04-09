import glob, os
MODELNAMES = {}
MODELS = {}
TDFX_MODELS = {}
def readIDESection(path):
    f = open(path)
    lines = f.readlines()
    flag = False
    for l in lines:
        l = l.strip()
        if "end" in l:
            flag = False
        if flag:
            p = l.strip().split(",")
            id = p[0]
            model = p[1].strip().lower()
            MODELNAMES[id] = model
        if "objs" in l:
            flag = True

def readIPLSection(path):
    f = open(path)
    lines = f.readlines()
    flag = False
    for l in lines:
        l = l.strip()
        if "end" in l:
            flag = False
        if flag:
            p = l.strip().split(",")
            id = p[0]
            x = float(p[3].strip())
            y = float(p[4].strip())
            z = float(p[5].strip())
            if id in MODELNAMES:
                model = MODELNAMES[id]
                if model in TDFX_MODELS:
                    print(TDFX_MODELS[model])
                #print(MODELNAMES[id])


        if "inst" in l:
            flag = True
def read2DFX():
    # process 2dfx
    path = os.path.join(os.path.dirname(__file__), "./data/2dfx/2dfx.dat")
    f = open(path)
    lines = f.readlines()
    current = None
    for l in lines:
        l = l.strip()
        if l and l[0] == '%':
            model = l.replace("%", "")
            if not model == current:
                TDFX_MODELS[model] = []
                current = model
        elif not current == None:
            if not model in TDFX_MODELS:
                TDFX_MODELS[model] = []
            TDFX_MODELS[model].append(l)



if __name__ == '__main__':

    read2DFX()

    os.chdir("./data/all_ide")
    # read ide
    for file in glob.glob("*.ide"):
        path = filename = os.path.join(os.path.dirname(__file__), "./data/all_ide/" + file)
        readIDESection(path)
    # read ipl
    os.chdir("../../")
    os.chdir("./data/all")

    for file in glob.glob("*.ipl"):
        path = filename = os.path.join(os.path.dirname(__file__), "./data/all/" + file)
        readIPLSection(path)


    print("DONE")
    #print(MODELNAMES["airport_11_sfse"])
