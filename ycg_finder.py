# FGAM TAG
import struct
import os
Textures = []
def dumpTxd(file):
    with open(file, "rb") as f:
        # txd_file_t
        struct_fmt = "III"
        data = f.read(struct.calcsize(struct_fmt) )
        s = struct.unpack(struct_fmt,data)
        (id,chunk_size,rw_version) = s

        # txd_info_t
        struct_fmt = "IIIHH"
        data = f.read(struct.calcsize(struct_fmt))
        s = struct.unpack(struct_fmt, data)
        (id, chunk_size, rw_version,count,unknown) = s
        #print(count)
        # dump_txd_texture_t, array
        for txd_index in range(count):
            # txd_texture_t
            struct_fmt = "III"
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)
            (id, chunk_size, rw_version) = s
            # txd_texture_data_t
            struct_fmt = "IIIII32s32sIIHHbbbb"
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)

            #print(s)
            depth = s[-4]
            midmaps_count = s[-3]
            txd_name = str(s[5],"ANSI").replace("\0","")

            #print("General Info")
            #print(s)
            # Dump pattern
            if depth == 8:
                f.read(256 * 4)
            #read datasize
            struct_fmt = "I"
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)
            data_size = s[0]
            # skip texture data

            txd_data = f.read(data_size)
            # mipmaps_s
            #print("Process midmaps sections")
            for midmaps in range(midmaps_count-1):
                struct_fmt = "I"
                data = f.read(struct.calcsize(struct_fmt))
                s = struct.unpack(struct_fmt, data)
                mipmaps_size = s[0]
                #print(mipmaps_size)
                f.read(mipmaps_size)

            # txd_extra_info_s
            #print("Extension Data:")
            struct_fmt = "III"
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)
            (id, chunk_size, rw_version) = s
            #print("RW_VER: {}".format(hex(rw_version)))
            # read extension data
            struct_fmt = "{}s".format(chunk_size)
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)
            extension = s[0]

            Textures.append({
                "txd_name" : txd_name,
                "rw_version": rw_version,
                "is_ycg": b"GCY" in extension,
            })

def dumpAllTxds():
    path = "E:\\dev\\mta-vcs\\mods\\deathmatch\\resources\\[vcs]\\vcs\\Content\\textures"
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".txd")):
                fullpath = "{}\\{}".format(path, name)
                dumpTxd(fullpath)

def writeOutYCGTxds():
    output = ""
    total = 0
    for txd in Textures:
        if txd["is_ycg"]:
            output = output + txd["txd_name"] + "\n"
            total = total + 1
    f = open("raw_textures.txt", "w")
    f.write(output)
    f.close()
    print("Total: {}".format(total))
def printYCGTable():
    print("{\n")
    for txd in Textures:
        if txd["is_ycg"]:
            print("\t\"{}\",".format(txd["txd_name"]))
    print("}")

if __name__ == '__main__':
    dumpTxd("./golfvegealpha.txd")
    #dumpAllTxds()
    printYCGTable()