import smalirenamer.SmaliRenamer as sr
import unittest

class TestStringMethods(unittest.TestCase):  #TODO this is only a working code whence to start

    def setUp(self):
        self.smalirenamer = sr.SmaliRenamer("/home/simo/Downloads/decchinese/bp/smali/")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse(True)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

'''
TODO TESTS

bad:
ᓐ.smali
ᖮپᓭᓮリ.smali
te$ˊ.smali
ٻ$ˊ.smali
dN$if$if$ˊ.smali
ᑊ.smali=ᑊ.smali
ʻ.smali=ʻ.smali


good:
a.smali
CoN.smali
zzq$zzc.smali
StaggeredGridLayoutManager$LazySpanLookup$FullSpanItem.smali

'''