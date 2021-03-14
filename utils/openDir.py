# Open maya  current files working directory
import maya.cmds as mc
import os
def working_directory():
    # current flie path 
    filepath = mc.file(q=True,sn=True)
    # raw,ext = os.path.splitext(filename)
    # current file name
    filename = os.path.basename(filepath)
    # remove file name
    directory = filepath.replace(filename," ")
    # replace forward slash with backward slash
    director = directory.split('/')
    del director[-1:]
    # current working directory
    dire = "\\".join(director)
    
    return dire

def openPWD():
    working_dir = working_directory()
    toOpen = "explorer.exe {0}".format(working_dir)
    os.system(toOpen)


openPWD()