import fileinput
import os
import re


class SmaliRenamer(object):
    allowedClassNameRegex = "^[A-Za-z]([a-zA-Z0-9_]*\$?)*.smali$"
    allowedClassName = re.compile(allowedClassNameRegex)
    allowedNameRegex = "^[a-zA-Z0-9_]*$"
    allowedName = re.compile(allowedNameRegex)
    defaultClassName = "Class"
    smali = ".smali"
    mapping = {}
    folder = ""

    def __init__(self, folder):
        self.folder = folder

    def run(self):
        self.generateMappingAndRenameFiles()
        self.replaceOccurrencesInFiles()
        print(len(self.mapping))

    def generateMappingAndRenameFiles(self):
        for root, dirs, files in os.walk(self.folder, topdown=False):
            for name in files:  # print(os.path.join(root, name))
                if name.endswith(self.smali):
                    if not self.allowedClassName.match(name):  # Loop all smali files with non printable names
                        newName = self.sanitize(name)
                        if newName != name:
                            os.rename(root + "/" + name, root + "/" + newName)  # Rename the files with new names
                            print(name + "->" + newName + "\n")
                        else:
                            print(name + "=" + newName + "\n")
                else:
                    raise Exception("Only .smali file allowed: " + name)

            for name in dirs:
                if not self.allowedName.match(name):
                    raise Exception("Folder with invalid name: " + name)

    def replaceOccurrencesInFiles(self):
        for root, dirs, files in os.walk(self.folder, topdown=False):
            for file in files:
                with fileinput.FileInput(file, inplace=True, backup=".bak") as openFile:
                    for line in openFile:
                        a=1
                        #line = self.searchAndReplace(line)

    def searchAndReplace(self, line):
        for key, value in self.mapping.items():
            if key in line:
                line.replace(key, value)
        return line

    def checkAndAdd(self, name):
        if not self.allowedName.match(name):
            if name not in self.mapping:
                tmpName = self.defaultClassName + str(len(self.mapping))
                self.mapping[name] = tmpName
                return tmpName
            else:
                return self.mapping[name]
        return name

    def sanitize(self, fileName):
        name = fileName[:-len(self.smali)]
        newName=""
        split = name.split("$")
        # print(len(split))
        if len(split) > 1:
            for s in split:
                newName += self.checkAndAdd(s)
                newName += "$"
            newName = newName[:-1]
        else:
            newName = self.checkAndAdd(name)
        # print(name + "->" + newName+"\n")
        return newName + self.smali  # Replace the obfuscated class name with ClassX (X incremental integer)
