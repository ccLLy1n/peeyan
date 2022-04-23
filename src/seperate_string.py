#畫圖
class graph:
    def __init__(self, side_1, side_2):       #創造物件並且定義邊長  
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

shape_sequence=["t","t","s","r","r","h","c"] #用這個列表紀錄形狀順序(三角，三角，正方形，長方形，長方形，梯形，圓形)
shape_wide=[21,13,8,10,11,14,6]#這個列表紀錄形狀對應到的寬度，三角形寬度為高度*2+1，梯形寬度為上邊+2*(高度-1)
space_num=max(shape_wide)
t=[10,6]#高
s=[8]#邊長
c=[6]#半徑
r=[7,10,4,11]#長，寬
h=[5,6]#高，上邊   #這邊是從界面獲得的個形狀數據

#上面部份只需要把一開始界面輸入的數值丟到相對應的位置即可
count=0
a= len(shape_sequence)

while True:
    if count==a :
        break

    space_num=int((max(shape_wide)-shape_wide[count])//2)+1 #每個圖形為了對齊需要往右移的量
    if shape_sequence[0]=="t":
        x=graph(t[0],t[0])#高
        x.draw_tri()
        t.pop(0)
    elif shape_sequence[0]=="s":
        x=graph(s[0],s[0])#邊長
        x.draw_square()
        s.pop(0)
    elif shape_sequence[0]=="c":
        x=graph(c[0],c[0])#半徑
        x.circle()
        c.pop(0) 
    elif shape_sequence[0]=="r":
        x=graph(r[0],r[1])
        x.draw_rec()
        r.pop(0)
        r.pop(0)        
    elif shape_sequence[0]=="h":
        x=graph(h[0],h[1])
        x.draw_trap()
        h.pop(0)   
        h.pop(0) 
    count=count+1 #判斷印完了沒有的計數器
    shape_sequence.pop(0)