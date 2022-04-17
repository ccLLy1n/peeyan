#宣告各形狀代號跟陣列
t=[]
s=[]
c=[]
r=[]#長，寬
h=[]#下邊，上邊，高

#計算目前個類別的形狀數 ShapeCount
tc=0
rc=0
sc=0
cc=0
hc=0
#主程式
#第一階段
print("Create_componemt")
print("------------------")
print("t是三角形，r是矩形，s是星形，c是圓形，h是梯形，最後輸入exit進入下一階段")
while True:
    shape=input("請輸入想要的形狀：")
    if shape=='t':
        t.append(input("請輸入三角形邊長："))
        print("這個三角形編號是t"+str(tc+1))
        tc+=1
    elif shape=='r':
        r.append(input("請輸入矩形長邊邊長："))
        r.append(input("請輸入矩形寬邊邊長："))
        print("這個矩形編號是r"+str(int(rc/2)+1))
        rc+=2
    elif shape=='s':
        s.append(input("請輸入星形邊長："))
        print("這個星形編號是s"+str(sc+1))
        sc+=1
    elif shape=='c':
        c.append(input("請輸入圓形直徑："))
        print("這個圓形編號是c"+str(cc+1))
        cc+=1
    elif shape=='h':
        h.append(input("請輸入梯形下邊長："))
        h.append(input("請輸入梯形上邊長："))
        h.append(input("請輸入梯形高："))
        print("這個梯形編號是h"+str(int(hc/3)+1))
        hc+=3
    elif shape=='exit':
        print("進入下一階段")
        break
    else:
        print("輸入錯誤，請重新輸入")
#進入畫圖階段
print("\nDraw_graphic")
print("------------------")

'''
接下來交給string—sperater跟graphic了
'''