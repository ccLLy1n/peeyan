#畫圖
class graph:
    def __init__(self, side_1, side_2):       #創造物件並且定義邊長  
        self.side_1=side_1
        self.side_2=side_2
    def draw_tri(self):                       #畫三角形
        for i in range(self.side_1+1):
            x=" "*(self.side_1-i)+ '*'*(2*i-1)
            print(x)
        print("\n")
    def draw_rec(self):                       #畫長方形
        for i in range(self.side_1):
            print("*"*self.side_2)
            #print("\n")
        print("\n")
    def draw_square(self):                    #畫正方形
        for i in range(self.side_1):
            print("*"*self.side_1)
    def draw_trap(self):                      #畫梯形   side_1是上底   side_2是高
        for i in range(self.side_1):
            x=(" "*(self.side_1-i-1)+"*"*(self.side_2+2*i))
            print(x)

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