print("~ PKゲームにようこそ ~")
name=input("プレイヤー名を入力してください。")
print(name,"さんは、キッカーです。キーパーを出し抜いてシュートを決めよう！")
point=0

# 5回の試合を実行
for i in range(1,6):
     # プレイヤーがPKを蹴る
 print(i,"戦目")
 print("１．左上　２．左下　３．真ん中　４．右上　５．右下")
 serect=int(input("蹴りたい場所の数字を入力してね"))

 import random
 a = random.randint(1,5)
 print("キーパーが動いた方向は",a)
 if serect==a:
  print("止められた...。")
 else:
   print("ナイスシュートだー‼︎")
   point=point+1

    # ゴール数を確認して勝敗を表示
if point >= 3:
        print(f"ゴール数: {point} - 点獲得で勝利！！")
else:
        print(f"ゴール数: {point} - 残念ながら敗退...。")

    