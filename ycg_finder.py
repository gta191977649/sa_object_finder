# FGAM TAG
import struct



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
            struct_fmt = "IIIII32c32cIIHHbbbbbI"

            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)

            data_size = s[-1]
            print( s)
            # skip texture data
            print(data_size)
            f.read(data_size)
            # mipmaps_s
            struct_fmt = "I"
            data = f.read(struct.calcsize(struct_fmt))

            s = struct.unpack(struct_fmt, data)
            print(s)
            print(s[0])
            f.read(s[0])
            # txd_extra_info_s
            struct_fmt = "III"
            data = f.read(struct.calcsize(struct_fmt))
            s = struct.unpack(struct_fmt, data)
            (id, chunk_size, rw_version) = s
            print(rw_version)
            f.read(chunk_size)







dumpTxd("E:\\dev\\vcs_map_e3\\img\\airporterminal.txd")