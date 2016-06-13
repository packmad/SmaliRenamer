import os
import subprocess


class AlignAndSign(object):
    # You have to change these variables to make them work with your environment
    javaPath = "/usr/bin/java"
    jarSignerPath = "/usr/bin/jarsigner"
    zipAlignPath = "/home/simo/android-sdk-linux/build-tools/23.0.2/zipalign"
    keyStorePath = "/home/simo/.android/debug.keystore"
    aliasKeyName = "androiddebugkey"
    errMiss = "ERROR: no executable found in "

    def __init__(self):
        self.check_files()

    def check_files(self):
        blackhole = open(os.devnull, "w")
        try:
            rc = subprocess.call([self.javaPath, "-version"], stdout=blackhole, stderr=blackhole)
        except OSError:
            raise Exception(self.errMiss + self.javaPath)

        try:
            rc = subprocess.call([self.jarSignerPath, "-help"], stdout=blackhole, stderr=blackhole)
        except OSError:
            raise Exception(self.errMiss + self.jarSignerPath)

        try:
            rc = subprocess.call([self.zipAlignPath], stdout=blackhole, stderr=blackhole)
        except OSError:
            raise Exception(self.errMiss + self.zipAlignPath)

        if not os.path.isfile(self.keyStorePath):
            raise Exception(self.errMiss + self.jarSignerPath)

    def sign_apk(self, alignedApkPath):
        rc = subprocess.call(
            [self.jarSignerPath, "-verbose", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1", "-keystore", self.keyStorePath,
             alignedApkPath, self.aliasKeyName, "-storepass", "android"])
        if rc == 0:
            return True
        return False

    def align_apk(self, srcUnalignedApkPath, dstAlignedApkPath):
        rc = subprocess.call([self.zipAlignPath, "-f", "-v", "4", srcUnalignedApkPath, dstAlignedApkPath])
        if rc == 0:
            return True
        return False

    def align_and_sign(self, unalignedApk):
        appName, file_ext = os.path.splitext(unalignedApk)
        if file_ext != ".apk":
            raise Exception("ERROR: must be an apk file")
        workingFolder = os.path.abspath(os.path.join(unalignedApk, os.pardir))
        if not os.path.isdir(workingFolder):
            raise Exception("ERROR: '" + workingFolder + "' isn't a folder.")
        alignedApkPath = appName + "_signed.apk"
        if self.align_apk(unalignedApk, alignedApkPath):
            if self.sign_apk(alignedApkPath):
                print("SUCCESS: completed without errors!")
            else:
                raise Exception("ERROR: sign failed")
        else:
            raise Exception("ERROR: align failed")
