import jieba
import jieba.posseg as pseg


def jieba_load():
    jieba.load_userdict("jib.txt")  # jieba加辭典
    jieba.load_userdict("text.txt")  # jieba加權重'


def jieba_cut_word(test):
    word = jieba.cut(test)  # jieba 分割問句句子
    print('/'.join(word))


def jieba_pseg_cut(test):   # jieba 分割資料文字 並打上標籤
    words = pseg.cut(test)
    return words
