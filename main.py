with open("/Users/sch/Desktop/猜词辅助/words.txt", "r") as words:
    global_words = words.read().split("\n")

# 以字母数排除
num_try = 0
oc = True
while oc:
    try:
        oc = False
        num_try = float(input("输入字母数："))
    except ValueError:
        print("请输入正整数")
        oc = True
    if not oc:
        num = int(num_try)
        if num != num_try or num <= 0:
            print("请输入正整数")
            oc = True

global_words = list(filter(lambda x: len(x) == num, global_words))


def unexpected_filter(words_list):  # 以不存在的字母排除
    alpha = False
    loop = True
    while loop:
        loop = False
        alpha = input("输入不存在的字母（不需要间隔，若没有直接回车）：")
        for j in alpha:
            if not j.isalpha():
                print("请输入字母")
                loop = True
                break
    if alpha:
        for j in alpha:
            if j.isupper():
                words_list = list(filter(lambda x: j not in x and j.lower() not in x, words_list))
            if j.islower():
                words_list = list(filter(lambda x: j not in x and j.upper() not in x, words_list))
    return words_list


def confirmed_filter(words_list):  # 以确定的字母排除
    if_exit = False
    for j in range(num):
        loop = True
        alpha = False
        while loop:
            loop = False
            alpha = input("输入第{}位已确定的字母，以'-abc...'表示存在但位置错误的字母，以'a-bcd...'表示同时存在的情况（没有直接回车）:".format(str(j + 1)))
            if not alpha:
                if_exit = True
                break
            if len(alpha) == 1:
                if not alpha.isalpha():
                    print("请输入字母")
                    loop = True
            else:
                if alpha[0].isalpha():
                    if alpha[1] != "-":
                        print("请按格式输入")
                        loop = True
                    for k in alpha[2:]:
                        if not k.isalpha():
                            print("请按格式输入")
                            loop = True
                else:
                    if alpha[0] != "-":
                        print("请按格式输入")
                        loop = True
                    for k in alpha[1:]:
                        if not k.isalpha():
                            print("请按格式输入")
                            loop = True
        if if_exit:
            if_exit = False
            continue
        if len(alpha) == 1:
            if alpha.isupper():
                words_list = list(filter(lambda x: alpha[0] == x[j] or alpha[0].lower() == x[j], words_list))
            if alpha.islower():
                words_list = list(filter(lambda x: alpha[0] == x[j] or alpha[0].upper() == x[j], words_list))
        elif alpha[0].isalpha():
            if alpha.isupper():
                words_list = list(filter(lambda x: alpha[0] == x[j] or alpha[0].lower() == x[j], words_list))
            if alpha.islower():
                words_list = list(filter(lambda x: alpha[0] == x[j] or alpha[0].upper() == x[j], words_list))
            for k in alpha[2:]:
                if k.isupper():
                    words_list = list(filter(lambda x: k in x or k.lower() in x, words_list))
                    words_list = list(filter(lambda x: not k == x[j] and not k.lower() == x[j], words_list))
                if k.islower():
                    words_list = list(filter(lambda x: k in x or k.upper() in x, words_list))
                    words_list = list(filter(lambda x: not k == x[j] and not k.upper() == x[j], words_list))
        elif alpha[0] == "-":
            for k in alpha[1:]:
                if k.isupper():
                    words_list = list(filter(lambda x: k in x or k.lower() in x, words_list))
                    words_list = list(filter(lambda x: not k == x[j] and not k.lower() == x[j], words_list))
                if k.islower():
                    words_list = list(filter(lambda x: k in x or k.upper() in x, words_list))
                    words_list = list(filter(lambda x: not k == x[j] and not k.upper() == x[j], words_list))
    return words_list


global_words = unexpected_filter(global_words)
global_words = confirmed_filter(global_words)
if global_words:
    print("剩余单词有：")
    for i in global_words:
        print(i)
else:
    print("无剩余单词，请检查输入或词库")

if_continue = True
while if_continue:
    if_continue = input("输入 c 以继续排除，按回车退出：")
    if if_continue == "c":
        global_words = unexpected_filter(global_words)
        global_words = confirmed_filter(global_words)
        if global_words:
            print("剩余单词有：")
            for i in global_words:
                print(i)
        else:
            print("无剩余单词，请检查输入或词库")
