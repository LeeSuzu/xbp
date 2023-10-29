waist_list=[] #waist_listというリストを作る
for i in range(1,4):
    print(i,"人目")
    waist=float(input("腹囲は？"))

    waist_list.append(waist) #ここでwaistという変数の値をリストに追加している

l=len(waist_list) 
s=sum(waist_list) 
mean=s/l #平均は合計/件数

print("今回の腹囲の平均は",mean,"cmです")
