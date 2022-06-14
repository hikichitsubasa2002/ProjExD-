import random
from timeit import repeat

kurikaesi = 5 #繰り返し
taisyou = 10 #対象
keson = 2 #欠損

def  main():
    for _ in range(kurikaesi):
        A = mondai()
        seikai(A)
        

def mondai():
      ward = [chr(c+65) for c in range(26)]
      char = random.sample(ward,taisyou)#選択
      print(char)
      char_K = random.sample(char,keson)#欠損
      print(char_K)
      for i in (char):
        if i not in char_K:
            print(i)#表示
      return i

def seikai():
    kazu = int(input("欠損文字はいくつ？"))
    if kazu == keson:
        print("正解です")
        for i in range(kazu):
            c = input(f"{i+1}一つ目の文字を入力してください")
            if c not in seikai:
                print("不正解です、またチャレンジしてください")
            return 0
        return 1
    else:
        print("不正解")
        return 0

if __name__ == " __main__":
    main()
