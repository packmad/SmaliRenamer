import smalirenamer.SmaliRenamer as sr
import unittest
import os
import inspect


class TestSmaliRenamer(unittest.TestCase):

    def setUp(self):
        pass
        '''
        testScriptFolder = inspect.getfile(inspect.currentframe())
        projTestFolder = os.path.abspath(os.path.join(testScriptFolder, os.pardir))
        app4Test = os.path.join(projTestFolder, "files4test", "apkmuzzle")
        self.smalirenamer = sr.SmaliRenamer(app4Test)
        '''

    def test_not_allowedClassName(self):
        names = ["ᓐ.smali", "ᖮپᓭᓮリ.smali", "te$ˊ.smali", "ٻ$ˊ.smali", "dN$if$if$ˊ.smali", "ᑊ.smali=ᑊ.smali", "ʻ.smali=ʻ.smali", "AndroidInstrumentationModule$$ModuleAdapter$ˋ.smali"]
        for name in names:
            self.assertFalse(sr.SmaliRenamer.allowedClassName.match(name))

    def test_allowedClassName(self):
        names = ["a.smali", "CoN.smali", "zzq$zzc.smali", "StaggeredGridLayoutManager$LazySpanLookup$FullSpanItem.smali"]
        for name in names:
            self.assertTrue(sr.SmaliRenamer.allowedClassName.match(name))

if __name__ == '__main__':
    unittest.main()
