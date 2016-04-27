import os
import re


class SmaliRenamer(object):
    allowedClassNameRegex = "^[A-Za-z]([a-zA-Z0-9_]*\$?)*.smali$"
    allowedClassName = re.compile(allowedClassNameRegex)
    allowedNameRegex = "^[a-zA-Z0-9_]*$"
    allowedName = re.compile(allowedNameRegex)
    defaultClassName = "Class"
    mapping = {}
    folder = ""

    def __init__(self, folder):
        self.folder = folder

    def run(self):
        for root, dirs, files in os.walk(self.folder, topdown=False):

            for name in files:  # print(os.path.join(root, name))
                if name.endswith(".smali"):
                    if not self.allowedClassName.match(name):
                        self.sanitize(name)
                else:
                    raise Exception("Only .smali file allowed: " + name)

            for name in dirs:
                if not self.allowedName.match(name):
                    raise Exception("Folder with invalid name: " + name)

    def checkAndAdd(self, name):
        if (not self.allowedName.match(name)) and (name not in self.mapping):
            tmpName = self.defaultClassName + str(len(self.mapping))
            self.mapping[name] = tmpName
            return tmpName
        return name

    def sanitize(self, fileName):
        name = fileName[:-len(".smali")]
        newName=""
        split = name.split("$")
        print(len(split))
        if len(split) > 1:
            for s in split:
                newName += self.checkAndAdd(s)
                newName += "$"
            newName = newName[:-1]
        else:
            newName = self.checkAndAdd(name)
        print(name + "->" + newName+"\n")
        return newName