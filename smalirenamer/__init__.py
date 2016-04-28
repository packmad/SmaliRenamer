import smalirenamer.SmaliRenamer as sr


if __name__ == "__main__":
    smaliRenamer = sr.SmaliRenamer("/home/simo/Downloads/decchinese/pid/smali/")
    smaliRenamer.run()
    #smaliRenamer.sanitize("ʻ.smali")


'''
TODO TESTS

ᓐ.smali
ᖮپᓭᓮリ.smali
te$ˊ.smali
ٻ$ˊ.smali
dN$if$if$ˊ.smali
ᑊ.smali=ᑊ.smali
ʻ.smali=ʻ.smali

a.smali
CoN.smali
zzq$zzc.smali
StaggeredGridLayoutManager$LazySpanLookup$FullSpanItem.smali

'''


