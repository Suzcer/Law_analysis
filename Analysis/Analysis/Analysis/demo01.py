from pyhanlp import *

HanLP.Config.ShowTermNature = False
text = "小区居民有的反对喂养流浪猫"
CRFnewSegment = HanLP.newSegment("crf")
term_list = CRFnewSegment.seg(text)
print(term_list)
HanLP.Config.ShowTermNature = True


CRFnewSegment = HanLP.newSegment("crf")
term_list = CRFnewSegment.seg(text)
print(term_list)
print([str(i.word) for i in term_list])
print([str(i.nature) for i in term_list])

