def fileSize (fname):
    import os
    statinfo=os.stat(fname)
    return statinfo.st_size

print("File size :: "+str(fileSize("testing.txt"))+" bytes")
