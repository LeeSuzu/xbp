# 支出データを格納するための空のリスト
expenses = []

# ユーザーから支出の項目と金額を入力してもらう関数
def add_expense():
    item = input("支出の項目を入力してください: ")
    amount = float(input("金額を入力してください: "))
    expenses.append((item, amount))
    print("支出が追加されました.")

# 支出の合計を計算する関数
def calculate_total_expenses():
    total = sum(amount for _, amount in expenses)
    return total

# メインの実行部分
while True:
    print("\n1. 支出を追加")
    print("2. 支出の合計を表示")
    print("3. 終了")
    choice = input("操作を選んでください (1/2/3): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        total_expenses = calculate_total_expenses()
        print(f"支出の合計は {total_expenses} 円です.")
    elif choice == '3':
        print("プログラムを終了します.")
        break
    else:
        print("無効な選択です. もう一度お試しください.")
