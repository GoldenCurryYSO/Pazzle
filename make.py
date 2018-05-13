from functools import reduce
import sys

path = "buta012.dic"

#頭文字をキー、N字の語のリストを値とした辞書を構成
def make_dict(N):
    init = ""
    dic = {}
    for line in open(path, "r", encoding="shift-jis"):
        if(init != line[0]):
            init = line[0]
            dic[init] = []
        l = line.replace("\n", "")
        if(len(l) == N):
            dic[init].append(l)
    return dic

#同じ字から始まり尻がanswerとなるようなN字の言葉を検索する
def make(answer, N):
    dic = make_dict(N)
    canditate = {}
    for init in dic.keys():
        words = dic[init]

        result = {}
        for tail in answer:
            result[tail] = []
        for w in words:
            if(answer.find(w[N - 1:]) != -1):
                result[w[N - 1]].append(w)
        canditate[init] = result
        
        #print
        min = sys.maxsize
        min_tail = ""
        for k in result.keys():
            if(min > len(result[k])):
                min = len(result[k])
                min_tail = k
        if(min > 0):
            print("【{0}】".format(init))
            print("<{0}>:{1}".format(min_tail, result[min_tail]))
    init = ""
    while(True):
        print("choose initial")
        init = input()
        if(init == ""):
            break
        for tail in canditate[init].keys():
            print("<{0}>".format(tail), end="")
            for i in range(len(canditate[init][tail])):
                print("\t" + canditate[init][tail][i], end="")
                if(i % 3 == 2):
                    print()
            print()
        

while(True):
    print("<word> <length>")
    s = input()
    if(s == ""):
        exit()
    ss = s.split(" ")
    if(len(ss) > 1):
        make(ss[0], int(ss[1]))
    else:
        make(s, 4)
