import bisect

# 標準入力を受け付ける。
N, K = map(int, input().split())

# 3日目までの各生徒の合計点数をまとめる。
# score_list[0]は利用しない。
score_list = []
for _ in range(N + 1):
    score_list.append([])

# 3日目までの各生徒の合計点数を格納する。
sum_score_list = []
for i in range(N):
    score = list(map(int, input().split()))
    # 3日目までの合計点数を算出する。
    sum_score = sum(score)
    # score_list[1] : 1番目の生徒の3日目までの合計点数。
    # score_list[2] : 2番目の生徒の3日目までの合計点数。
    # ...
    score_list[i + 1] = sum_score
    sum_score_list.append(sum_score)

# 合計点数をソートする。
sum_score_list.sort()

# score_list[0]を利用しないため、range(1, N + 1)とする。
for i in range(1, N + 1):
    # 4日目の試験でi番目の生徒が満点(300点)を取り、その他の生徒が0点の場合に、一番順位が上がるため、その場合のみを検討する。
    # よって+300されている。
    best_score = score_list[i] + 300

    # 二分探索を用いて、4日目までのi番目の生徒の合計点数がどの順位に位置するのか算出する。
    # 二分探索とは? : https://codezine.jp/article/detail/12243
    # 参考 : https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3
    idx = bisect.bisect_right(sum_score_list, best_score)

    # K以内に入る場合、`Yes`を返す。
    if N - K + 1 <= idx:
        print('Yes')
    # K以内に入らない場合、`No`を返す。
    else:
        print('No')
