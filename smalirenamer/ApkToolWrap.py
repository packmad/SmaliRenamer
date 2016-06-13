import subprocess


class ApkTool(object):
    # You have to change these variables to make them work with your environment
    apkToolPath = "/usr/local/bin/apktool"

    @classmethod
    def decode(cls, apkFile, outputFolder):
        return subprocess.call([cls.apkToolPath, "d", "-f", apkFile, "-o", outputFolder])

    @classmethod
    def build(cls, decompiledApkFolder):
        return subprocess.call([cls.apkToolPath, "b", "-f", decompiledApkFolder])
