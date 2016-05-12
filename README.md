# SmaliRenamer

Sometimes using [ApkTool](http://ibotpeaches.github.io/Apktool/) can happen that the names of decompiled classes contain characters that generate errors during the rebuild.

With this script the classes whose names contain characters that are different from the letters of the alphabet [A-Za-z]
will be renamed with a default prefix and an incremental number.

After this phase every occurrences in the smali code is renamed.

After that you can run the rebuild with ApkTool. Enjoy :)


I'm a python newbie and there are lot's of TODO any help/suggestions will be appreciated!
