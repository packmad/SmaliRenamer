import smalirenamer.SmaliRenamer as sr


if __name__ == "__main__":
    smaliRenamer = sr.SmaliRenamer("/home/simo/Downloads/decchinese/BancoPosta_v5.0_apkpure.com/smali/")
    smaliRenamer.sanitize("ᖮپᓭᓮリ.smali")



'''
TODO TESTS

ᓐ.smali
ᖮپᓭᓮリ.smali
te$ˊ.smali
ٻ$ˊ.smali
dN$if$if$ˊ.smali

a.smali
CoN.smali
zzq$zzc.smali
StaggeredGridLayoutManager$LazySpanLookup$FullSpanItem.smali

'''


