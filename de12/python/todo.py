# 空のToDoリストを作成
todo_list = []

# ToDoを追加する関数
def add_todo(todo):
    todo_list.append(todo)
    print(f"'{todo}' をToDoリストに追加しました！")

# ToDoリストを表示する関数
def show_todos():
    if todo_list:
        print("ToDoリスト:")
        for index, todo in enumerate(todo_list, start=1):
            print(f"{index}. {todo}")

    else:
        print("ToDoリストは空です！")

# ToDoを削除する関数
def delete_todo(index):
    if index > 0 and index <= len(todo_list):
        deleted_todo = todo_list.pop(index - 1)
        print(f"'{deleted_todo}' をToDoリストから削除しました！")
    else:
        print("無効なインデックスです。")

# ユーザーインターフェース
while True:
    print("\n操作を選択してください:")
    print("1. ToDoを追加")
    print("2. ToDoリストを表示")
    print("3. ToDoを削除")
    print("4. 終了")

    choice = input("選択 (1/2/3/4): ")

    if choice == '1':
        new_todo = input("予定の日程を入力してください: ")
        neww_todo = input("追加するToDoを入力してください: ")
        add_todo(new_todo)
    elif choice == '2':
        show_todos()
    elif choice == '3':
        show_todos()
        if todo_list:
            index = int(input("削除するToDoの番号を入力してください: "))
            delete_todo(index)
    elif choice == '4':
        print("プログラムを終了します。")
        break
    else:
        print("無効な選択です。もう一度お試しください。")


