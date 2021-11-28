import os
output= ""
if __name__ == '__main__':
    path = "E:\\dev\\vcs_map\\Textures"
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".tga")):
                name = name.replace(".tga", "")
                print("<file src=\"data/raw/{}.tga\"/>".format(name))
                output = output + name +"\n"


    f = open("raw_textures.txt","w")
    f.write(output)
    f.close()