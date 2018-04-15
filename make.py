from functools import reduce

path = "buta012.dic"

#頭文字をキー、N字の語のリストを値とした辞書を構成
def make_dict(N):
    init = ""
    dic = {}
    for line in open(path, "r"):
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
    for k in dic.keys():
        result = {}
        for c in answer:
            result[c] = []
        words = dic[k]
        for w in words:
            if(answer.find(w[N - 1:]) != -1):
                result[w[N - 1]].append(w)
        #print
        if reduce(lambda b1, b2:b1 and b2, map(lambda l:len(l) > 0, result.values())):
            for r in result.keys():
                print("{0}:{1}".format(r, result[r]))
            print("return to next...\n")
            input()

while(True):
    s = input()
    if(s == ""):
        exit()
    make(s, 6)