# PROBLEM_LINK
"""
Template reference: Emma, https://stackoverflow.com/a/62614733/13109740
"""

from typing import List
import collections
import itertools
import functools
import string
import random
import bisect
import re
import operator
import heapq
import queue

from math import *
from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

from textwrap import wrap
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key2vMap = {}
        self.v2keyMap = defaultdict(list)
        for i, key in enumerate(keys):
            v = values[i]
            self.key2vMap[key] = v
            self.v2keyMap[v].append(key)
        
        self.permittedStrings = {}
        for word in dictionary:
            self.permittedStrings[word] = True
            
        print(self.key2vMap)
        print(self.v2keyMap)
        print("permittedStrings")
        print([key for key in self.permittedStrings])
        

    def encrypt(self, word1: str) -> str:
        res = ""
        for c in word1:
            newC = self.key2vMap[c]
            res+=newC
        return res
        

    def decrypt(self, word2: str) -> int:
        if len(word2)%2>0:
            return 0
        possibleStrings = []
        
        for s in wrap(word2,2):
            vs = self.v2keyMap[s]
            if not possibleStrings:
                possibleStrings = vs[:]
                continue
            
            newStrings = []
            for v in vs:
                for ps in possibleStrings:
                    newString = ps+v
                    newStrings.append(newString)
            possibleStrings = newStrings
        
        ans = 0
        for s in possibleStrings:
            if s in self.permittedStrings:
                ans += 1
                
        print(possibleStrings)
        print(f"ANS:{ans}")
        
        return ans

ks,vs,d = [["e","t","m","s","v","w","y","b","x","h","o","c","i","u","q","p","d","n","j","g","k","l","f","z","r","a"],["ay","yn","by","ew","po","qg","ob","zf","jj","yz","kc","bg","kf","um","jb","lv","se","hw","td","al","sp","wg","rj","vl","tv","hj"],["s"]]
enc = Encrypter(ks, vs, d)
print("")

ciphers = ["ezqrlkgm"],["ymswyhml"],["iswtdnxm"],["vdfgupvo"],["qbzzduko"],["wszjkudb"],["jsmioejb"],["ebhckvie"],["idnwrcuh"],["cpopwjhh"],["wadoqotc"],["mubtmybg"],["ctsmdcuc"],["ppmofvyb"],["nuopvlvy"],["xqxtgtbh"],["nrluthnj"],["mbqylgzt"],["enlxrgwe"],["xhsegyzb"],["luktywus"],["qqbnueoa"],["npefvtqf"],["snlmabrf"],["gpoxtqhh"],["tsxcwztl"],["fojsmkhh"],["rfdyioeg"],["otwyrbev"],["aibstgxe"],["jsjycovp"],["nnetjrgf"],["hameocbg"],["flptwdim"],["geeejpuv"],["oppijhvq"],["tnmmmact"],["cpharytn"],["xebkfrfy"],["tgxihizb"],["degkrzro"],["ibliwlps"],["gejvxrxv"],["onlcouxv"],["nbhkczkz"],["alwkimpx"],["inydaakr"],["htoxtgxi"],["zpkshxyw"],["brwnbcma"],["tppwvoyk"],["qbaerwst"],["gbveophz"],["yukxkqbi"],["sysbvfcc"],["urknzucq"],["suchpinb"],["jbuheypf"],["swpotyet"],["bgkyyzra"],["yincmplm"],["ppguhblv"],["tpqncscn"],["whjwqicl"],["ppdygrpc"],["nebwonew"],["lslmajzv"],["dpzbakgk"],["gpdjdyoe"],["yszguhel"],["nlcnlcep"],["jqfeajxt"],["ixxxycdm"],["dvonxcql"],["ptbvtcxk"],["heurgdyr"],["tkztgmvx"],["wbduqekd"],["jjqqllqh"],["vlvsvkps"],["kpssufvo"],["eyubqktz"],["snugbxnu"],["upxafrim"],["odeaujac"],["euvzvlqn"],["jeyrppip"],["jvbmnaaj"],["tmeeiert"],["xboqkpsg"],["luxfdpkp"],["zgsfmiwn"],["yfgxndnq"],["uedmszun"],["egenlawk"],["hhzcocwl"],["wdovphoi"],["xmflljde"],["vyjbmnuf"],["zxyjyxbg"],["pxjbwyyp"],["isxvygld"],["qyfdkmjb"],["cxbwtspg"],["ffzqnwpv"],["jtqrbtpe"],["wjdtzdsc"],["nogpqbor"],["vtqjkctg"],["vzzartfe"],["cwqgrxdp"],["gftorojh"],["smuwbloa"],["hogcsjep"],["vonqcrwr"],["bmfcqmqh"],["yldejzwr"],["samonohp"],["bmkrmqxe"],["vdewfuyu"],["wczvjesp"],["qsvrntll"],["hrbblttx"],["visqwmap"],["naumbeac"],["zarszekr"],["cynvwgno"],["iagnapuj"],["blhmitww"],["dkzwyges"],["hslogaih"],["crjsmkmp"],["hqhqjxjf"],["rcpqxxmf"],["pkenrgwa"],["usqidfxw"],["sewskwkh"],["zjttkdbt"],["zfmlsupa"],["yotxebdw"],["fqgnehuo"],["vnquozaq"],["dxiprodg"],["ginmmwjv"],["orkeybjm"],["jjdqoler"],["mftvctry"],["nvsunilx"],["ypaeqflo"],["xtguvcyg"],["ryrscpqu"],["mcxracdd"],["khiwsxtw"],["ufelcopy"],["gyuitggt"],["tmfdocwq"],["axqmfmko"],["jddsflcj"],["sysbzfbr"],["igsxryeg"],["znjmxfue"],["dwebhxsg"],["viadremm"],["vqnbipne"],["nllmnxsa"],["gahailpi"],["wjhwwlej"],["mfgapumf"],["mxsgpfba"],["neaytree"],["lwcvvygg"],["kexjrmus"],["opwowldi"],["dvxihayu"],["rurmrvdb"],["sftmwwig"],["uywtaflc"],["wcsrsqfk"],["rdutwajq"],["ozktnvku"],["trhrisvg"],["zcmboyib"],["acqlauiw"],["jnavmxbe"],["evvhiyqa"],["rwiqerst"],["xlplovvd"],["kaantzlf"],["tjipfunb"],["zktlvlqi"],["nnjpezpu"],["fjdfapin"],["tvrlzbas"],["wwwygvwq"],["ynvvdnwx"],["hxkxkiii"],["hmoeyusn"],["pxjnskmd"],["tcrducim"],["ewcnkkpk"]

for c in ciphers:
    print(c[0])
    ans = enc.decrypt(c[0])
    print(ans)
print("DONE")


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)