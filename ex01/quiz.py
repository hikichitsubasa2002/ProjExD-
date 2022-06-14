import random
def main():
    kotae = mondai()
    kaitou(kotae)
    
def mondai():
    QA = [{"q":"サザエの旦那の名前は？","a":["マスオ","鱒男","ますお"]},{"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
    {"q":"タラオはカツオから見てどんな関係？","a":["甥"]}]
    print("問題")
    r = random.arint(0,2)
    print(QA[r]["q"])
    return QA[r]["a"]

def kaitou(kotae):
    ans= input("A")
    if ans in kotae:
        print("正解")
    else:
        print("不正解")