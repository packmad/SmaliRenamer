import smalirenamer.SmaliRenamer as sr
import datetime
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("The only argument needed is the folder of decompiled Apk")
        sys.exit(-1)
    decompiledApkFolder = sys.argv[1]
    t1 = datetime.datetime.now()
    smaliRenamer = sr.SmaliRenamer(decompiledApkFolder)
    smaliRenamer.run()
    t2 = datetime.datetime.now()
    print("Execution time for '" + decompiledApkFolder + "' is: " + str((t2-t1)))



