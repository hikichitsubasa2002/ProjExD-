import random
from timeit import repeat
from sympy import Chi


ward = list("ABCDEFGHIJKLMNOPQRSTUVWXYG")
kurikaesi = 5 #繰り返し
taisyou = 10 #対象
keson = 2 #欠損

def  main():
    for _ in range(kurikaesi):
        A = mondai()
        seikai(A)
        

def mondai():
      char = random.sample(ward,taisyou)#選択
      print(char)
      char_K = random.sample(char,keson)#欠損
      print(char_K)
      for i in (char):
        if i not in char_K:
            print(i)#表示

def seikai():
    kazu = int(input("欠損文字はいくつ？"))
    if kazu == keson:
        print("正解")
    else:
        print("不正解")


