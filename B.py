# 標準入力を受け付ける。
N, i = map(int, input().split())

A = list(map(int, input().split()))

# 友達が秘密を知っているかどうかを表すフラグを用意する。
# temp[0]は利用しない。
temp = [False] * (N + 1)

# 友達A[i]が秘密を知らない間、秘密の伝言ゲームを続ける。
while True:
    # 友達A[i]が秘密を知っていたならば、秘密の伝言ゲームを終了する。
    if temp[i]:
        break
    # 友達A[i]が高橋くんの秘密を知らなくて、友達iがA[i]へ秘密を話した場合、フラグを更新する。
    temp[i] = True
    # 次に秘密を伝えるA[i]を指定する。
    # -1しているのは、配列のidx調整のため。
    i = A[i - 1]

# 秘密を知っている人数を出力する。
print(sum(temp))
