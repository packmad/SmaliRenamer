# SmaliRenamer

Sometimes when using [ApkTool](http://ibotpeaches.github.io/Apktool/) can happen that the names of decompiled classes contain characters that generate errors during the rebuild.

With this script the classes whose names contain non alphanumeric-characters
will be renamed with a default prefix and an incremental number.

After this phase every occurrences in the smali code is renamed.

