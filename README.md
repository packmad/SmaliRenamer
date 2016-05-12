# SmaliRenamer

Sometimes using [ApkTool](http://ibotpeaches.github.io/Apktool/) can happen that the names of decompiled classes contain characters that generate errors during the rebuild.

With this script the classes whose names contain characters that are different from the letters of the alphabet [A-Za-z]
will be renamed with a default prefix and an incremental number.

After this phase every occurrences in the smali code is renamed.

Finally you can rebuild with ApkTool without errors. Enjoy :)

## Help
I'm a python newbie, any help/suggestions will be appreciated!

