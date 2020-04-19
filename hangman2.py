# http://tinyurl.com/jhrvs94
import random

def hangman(word):
    # プレイヤーが間違えた回数
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    # 多分、ゲームの入り口（ステータス初期化をしている）
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

# http://tinyurl.com/ztrp5jc

    while wrong < len(stages) - 1: # 絵を完成させるまで繰り返す
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters: # 
            cind = rletters.index(char) 
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！！")
            print(" ".join(board))
            win = True
            break

    # http://tinyurl.com/zqklqxo
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


i = random.randint(0,5)
list2 = ["Git","services","kimetunoyaiba","kaede","keino","Python"]
hangman(list2[i])
