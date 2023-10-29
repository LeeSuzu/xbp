print("~ PKゲームにようこそ ~")
name=input("プレイヤー名を入力してください。")
print(name,"さんは、キッカーです。キーパーを出し抜いてシュートを決めよう！")
point=0

for i in range(1,5):
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

   if point>=3:
    print(name,"さんの結果は...",point,"点獲得で勝利！")
   elif point<=2:
    print(name,"さんの結果は...",point,"点獲得で敗退...")