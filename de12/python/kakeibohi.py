from openpyxl import Workbook

# ワークブックを作成し、アクティブなシートを取得します。
wb = Workbook()
ws = wb.active

# ヘッダーを設定します。
ws.append(["日付"," 品目","金額"])

# データを追加します。
data = [
    ["2023-10-01", "食費",1000],
    ["2023-10-05", "交通費",500],
    ["2023-10-10", "服",2000],
]

for row in data:
    ws.append(row)

#　ファイルを保存します
wb.save("家計簿テンプレート.xlsx")