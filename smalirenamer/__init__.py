import smalirenamer.AlignAndSign as AS
import smalirenamer.SmaliRenamer as SR
import smalirenamer.ApkToolWrap as ATW
import datetime
import os
import sys


def phase_decompile(apkFile, outputFolder):
    print(">>> Start decompile phase of " + apkFile)
    t1 = datetime.datetime.now()
    rc = ATW.ApkTool.decode(apkFile, outputFolder)
    t2 = datetime.datetime.now()
    print("<<< Time needed for decompile'" + apkFile + "' is: " + str((t2 - t1)))


def phase_rename(decompiledApkFolder):
    print(">>> Start rename phase of " + decompiledApkFolder)
    t1 = datetime.datetime.now()
    smaliRenamer = SR.SmaliRenamer(decompiledApkFolder)
    smaliRenamer.run()
    t2 = datetime.datetime.now()
    print("<<< Time needed for renaming '" + decompiledApkFolder + "' is: " + str((t2 - t1)))


def phase_rebuild(decompiledApkFolder):
    print(">>> Start rebuilding phase of " + decompiledApkFolder)
    t1 = datetime.datetime.now()
    rc = ATW.ApkTool.build(decompiledApkFolder)
    t2 = datetime.datetime.now()
    print("<<< Time needed for rebuilding'" + decompiledApkFolder + "' is: " + str((t2 - t1)))
    return rc


def phase_align_sign(apkFile):
    print(">>> Start rebuilding phase of " + apkFile)
    t1 = datetime.datetime.now()
    alignAndSign = AS.AlignAndSign()
    alignAndSign.align_and_sign(apkFile)
    t2 = datetime.datetime.now()
    print("<<< Time needed for rebuilding'" + apkFile + "' is: " + str((t2 - t1)))


def batch_work(root):
    for f in os.listdir(root):
        file = os.path.join(root, f)
        if os.path.isfile(file):
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".apk":
                phase_decompile(file, os.path.join(root, filename))
    for f in os.listdir(root):
        decompiledApkFolder = os.path.join(root, f)
        if os.path.isdir(decompiledApkFolder):
            phase_rename(decompiledApkFolder)
            rc = phase_rebuild(decompiledApkFolder)
            if rc == 0:
                phase_align_sign(os.path.join(decompiledApkFolder, "dist", f+".apk"))
            else:
                raise Exception("Rebuild phase generated a bad apk")


def single_work(apkFile):
    decompiledApkFolder, file_ext = os.path.splitext(apkFile)
    phase_decompile(apkFile, decompiledApkFolder)
    phase_rename(decompiledApkFolder)
    phase_rebuild(decompiledApkFolder)
    phase_align_sign(os.path.join(decompiledApkFolder, "dist", os.path.basename(apkFile)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Only one argument needed!")
        sys.exit(-1)
    arg = sys.argv[1]
    if os.path.isdir(arg):
        phase_rename(arg)
    else:
        raise Exception("The argument isn't an existing folder")
