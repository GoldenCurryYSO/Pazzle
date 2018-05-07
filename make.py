from functools import reduce

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
    for init in dic.keys():
        print("【{0}】".format(init))
        words = dic[init]

        result = {}
        for tail in answer:
            result[tail] = []
        for w in words:
            if(answer.find(w[N - 1:]) != -1):
                result[w[N - 1]].append(w)
        #print
        if reduce(lambda b1, b2:b1 and b2, map(lambda l:len(l) > 0, result.values())):
            for tail in result.keys():
                print("<{0}>".format(tail), end="")
                for i in range(len(result[tail])):
                    print("\t" + result[tail][i], end="")
                    if(i % 3 == 2):
                        print()
                print()
            print("return to next...\n")
            input()

while(True):
    s = input()
    if(s == ""):
        exit()
    ss = s.split(" ")
    if(len(ss) > 1):
        make(ss[0], int(ss[1]))
    else:
        make(s, 4)
