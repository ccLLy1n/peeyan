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
    def circle(self):
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
            answer = space_1 + pixel_1 + space_2 + pixel_2 + space_1
            print(answer)
        

x=graph(9,5)
x.draw_rec()
x.circle()