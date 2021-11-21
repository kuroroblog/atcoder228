# 標準入力を受け付ける。
S, T, X = map(int, input().split())

# 部屋の電気をつけている間の、1時間単位の値を格納する。
time_list = []
while True:
    time_list.append(S)
    # 部屋の電気を消すタイミングでwhile文を終了する。
    if S == T:
        break
    # 日付が変わる場合、S = 0となる。
    if S == 24:
        S = 0
    else:
        S += 1

for i in range(0, len(time_list) - 1):
    # X時30分の時間帯に電気はついているのか確認する
    if time_list[i] <= X < time_list[i + 1]:
        print('Yes')
        exit()

print('No')
