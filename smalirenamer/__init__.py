import smalirenamer.SmaliRenamer as sr
import datetime


if __name__ == "__main__":
    decompiledApkFolder = "/home/simo/Downloads/decchinese/bp/"  #TODO parse from cmd line
    t1 = datetime.datetime.now()
    smaliRenamer = sr.SmaliRenamer(decompiledApkFolder)
    smaliRenamer.run()
    t2 = datetime.datetime.now()
    print("Execution time for '" + decompiledApkFolder + "' is: " + str((t2-t1)))



