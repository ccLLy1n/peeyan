
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
    def draw_circle(self):
        side=self.side_1
        time=int((side-7)/2+1)   #time是空格數
        t=time-2
        for i in range(side):
            answer=str()
            space_1 = " "*(time-i)
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
                space_1 = " "*(time)
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
            answer = (1+space_num)*" "+space_1 + pixel_1 + space_2 + pixel_2 + space_1
            print(answer)   
    def draw_star(self):
        side=self.side_1
        height=1+(side-1)*3
        for i in range(height):
            if i < side-1:                    #上
                space_1=" "*((side-1)*2-i)
                space_2=" "*(1+2*(i-1))
                draw_1="*"
                if i==0:                #判斷第一行
                    draw_2='*'
                    space_2=1+(side-2)*2
            elif i==side-1:                 
                space_1=""
                draw_1="*"*side
                space_2=' '*(1+(side-2)*2)
            elif i>=side and i<2*side-2:        #中
                space_1=" "*(i-side+1)
                draw_1="*"
                #draw_2="***"
                space_2=" "*((height-(i-side)*2)+side-5)
            elif i>=2*side-2 and i<height-1:
                space_1=" "*(height-i-1)
                draw_1="*"
                draw_2="*"*(1+(side-4)*2)
                space_2="  "
                space_3=" "*((1+(i-(height-side))*2)+2*(side-5))
            elif i==height-1:
                space_1="  "
                draw_1="**"
                space_2=" "*(1+(i-(height-side))*2+(side-5)*2)
            #----------------------------------------------
            if i<=side-1:
                if i==0:
                    print(space_num*" "+space_1+draw_1+space_1)
                else:
                    print(space_num*" "+space_1+draw_1+space_2+draw_1+space_1)
            elif i>=side and i<2*side-2:
                print(space_num*" "+space_1+draw_1+space_2+draw_1)
            elif i>=2*side-2 and i<height-1:
                if i==2*side-2:
                    print(space_num*" "+space_1+draw_1+space_2+draw_2+space_2+draw_1)    
                else:
                    print(space_num*" "+space_1+draw_1+space_2+draw_1+space_3+draw_1+space_2+draw_1)
            elif i==height-1:
                print(space_num*" "+space_1+draw_1+space_2+draw_1)
shape_sequence=["t","t","s","r","r","h","c","st"] #用這個列表紀錄形狀順序(三角，三角，正方形，長方形，長方形，梯形，圓形)
shape_wide=[21,13,8,10,11,14,10,13]#這個列表紀錄形狀對應到的寬度，三角形寬度為高度*2+1，梯形寬度為上邊+2*(高度-1)，星星寬度邊*3-1，圓形寬度為直徑
space_num=max(shape_wide)
t=[10,6]#高
s=[8]#邊長
c=[10]#直徑
r=[7,10,4,11]#長，寬
h=[5,6]#高，上邊   #這邊是從界面獲得的個形狀數據
st=[4]#邊長
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
        x.draw_circle()
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
    elif shape_sequence[0]=="st":
        x=graph(st[0],st[0])#半徑
        x.draw_star()
        st.pop(0)  
    count=count+1 #判斷印完了沒有的計數器
    shape_sequence.pop(0)