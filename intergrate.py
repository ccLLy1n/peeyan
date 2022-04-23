class graph:
    def __init__(self, side_1, side_2=0):       #創造物件並且定義邊長  
        self.side_1=side_1
        self.side_2=side_2
    def draw_tri(self):                       #畫三角形
        for i in range(self.side_1+1):
            x=" "*(self.side_1-i+space_num)+ '*'*(2*i+1)
            print(x)
    def draw_rec(self):                       #畫長方形
        for i in range(self.side_1):
            print(" "*space_num+"*"*self.side_2)
        
    def draw_square(self):                    #畫正方形
        for i in range(self.side_1):
            print(" "*space_num+"*"*self.side_1)
    def draw_trap(self):                      #畫梯形   side_1是上底   side_2是高
        for i in range(self.side_1):
            x=(" "*(self.side_1-i-1+space_num)+"*"*(self.side_2+2*i))
            print(x)
    def circle(self):                          #畫圓形
        side=self.side_1
        time=int((side-7)/2+1)   #time是空格數
        t=time-2
        for i in range(side):
            answer=str()
            space_1 = " "*(time-i+space_num)
            #space_2 = "="*(time-i)
            #print(space)
            if i==0:
                pixel_1="*****"
                pixel_2=""
                space_2=""
            elif i==side-1:
                pixel_1="*****"
                pixel_2=""
                space_2=""
                space_1 = " "*(time+space_num)
            elif i>0 and i <=side-time-1:
                pixel_1="*"
                pixel_2="*"
                if time-i>=0:
                    space_2 = "     " + ((i-1)*2) * " "
                else:
                    space_2 = "     " + ((time-1)*2)*" "
            elif i>side-time-1 and i<side-1:
                pixel_1="*"
                pixel_2="*"
                #space_1="="*(side-i-1)
                for x in range(side-i):    
                    space_1 = " "*(time-x)
                if t>=0:
                    space_2="     " +((t)*2)*" "
                t=t-1
            answer = space_1 + pixel_1 + space_2 + pixel_2 + space_1
            print(answer)            
t=[] #三角形「邊長」
s=[] #星形 「邊長」
c=[] #圓形 「直徑」
r=[] #矩形「長、寬」
h=[] #梯形「上底、高」
shape_sequence=[] #存放輸入圖形順行
shape_wide=[]
#為了執行程式暫時設定的變數
space_num=0
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
        ans=input("請輸入三角形邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        t.append(int(ans))
        shape_sequence.append(shape)
        shape_wide.append(2*int(ans))
        print("這個三角形編號是t"+str(tc+1))
        tc+=1
    elif shape=='r':
        r_length = list()
        ans=input("請輸入矩形長邊邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        r_length.append(int(ans))

        ans=input("請輸入矩形寬邊邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        r_length.append(int(ans))
        shape_sequence.append(shape)
        shape_wide.append(int(ans))
        print("這個矩形編號是r"+str(rc+1))
        r.append(r_length)
        rc+=1
    elif shape=='s':
        ans=input("請輸入星形邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        shape_sequence.append(shape)
        s.append(int(ans))
        print("這個星形編號是s"+str(sc+1))
        sc+=1
    elif shape=='c':
        ans=input("請輸入圓形直徑：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        shape_sequence.append(shape)
        c.append(int(ans))
        print("這個圓形編號是c"+str(cc+1))
        cc+=1
    elif shape=='h':
        ans=input("請輸入梯形上邊長：")
        h_length=[]
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        h_length.append(int(ans))

        ans=input("請輸入梯形高：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        h_length.append(int(ans))
        print("這個梯形編號是h"+str(hc+1))
        shape_sequence.append(shape)
        h.append(h_length)
        shape_wide.append(h_length[0]+2*h_length[1])
        hc+=1
    elif shape=='exit':
        print("進入下一階段")
        break
    else:
        print("輸入錯誤，請重新輸入")
#進入畫圖階段
print("\nDraw_graphic")
print("------------------")
print(shape_sequence)

'''
接下來交給string—sperater跟graphic了
'''

for count in range(0,len(shape_sequence)):
    if shape_sequence[0]=="t":  #畫三角形
        # space_num=max(shape_wide)-t[0]//2+1#每個圖形為了對齊需要往右移的量
        x=graph(t[0])#高
        x.draw_tri()
        t.pop(0)
    elif shape_sequence[0]=="s":#畫星形（尚未成功）
        # space_num=(尚未寫成）#每個圖形為了對齊需要往右移的量
        x=graph(s[0])#邊長
        # x.draw_square()
        s.pop(0)
    elif shape_sequence[0]=="c":#畫圓形（尚未成功）
        # space_num=(尚未寫成）#每個圖形為了對齊需要往右移的量
        x=graph(c[0])#直徑
        x.circle()
        c.pop(0) 
    elif shape_sequence[0]=="r":#畫矩形
        # space_num=(尚未寫成）#每個圖形為了對齊需要往右移的量
        x=graph(r[0][0],r[0][1])
        x.draw_rec()
        r.pop(0)     
    elif shape_sequence[0]=="h":#畫梯形
        # space_num=(尚未寫成）#每個圖形為了對齊需要往右移的量
        x=graph(h[0][0],h[0][1])
        x.draw_trap()
        h.pop(0)   
    shape_sequence.pop(0)