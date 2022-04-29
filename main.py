import graph_integrate as G
#參數定義
t=[] #三角形「邊長」
s=[] #星形 「邊長」
c=[] #圓形 「直徑」
r=[] #矩形「長、寬」
h=[] #梯形「上底、高」
shape_sequence=[] #存放輸入圖形順行
shape_wide=[]
space_num =0      #為了將圖形校正到中心的空格數量
#主程式
#第一階段
print("Create_componemt")
print("------------------")
print("t是三角形，r是矩形，s是星形，c是圓形，h是梯形，最後輸入exit進入下一階段")
while True:
    shape=input("請輸入想要的形狀：")
    if shape=='t':
        ans=input("請輸入三角形高度（層數)：")
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
        shape_wide.append(2*int(ans)+1) #三角形對應的最長寬度為：三角形高度*2+1
        print("這個三角形編號是t"+str(shape_sequence.count('t')))  #此處的.count()涵式是用來計算現有的三角形數量
    
    elif shape=='r':
        r_length = list()
        ans=input("請輸入矩形Y軸邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        r_length.append(int(ans))

        ans=input("請輸入矩形X軸邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        r_length.append(int(ans))
        r.append(r_length)
        shape_sequence.append(shape)
        shape_wide.append(int(ans))  #矩形對應的最長寬度為：X軸邊長
        print("這個矩形編號是r"+str(shape_sequence.count('r')))#此處的.count()涵式是用來計算現有的矩形數量
        
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
        s.append(int(ans))
        shape_sequence.append(shape)
        shape_wide.append(4*(int(ans)-1)+1)  #星星對應的最長為：星星寬度邊*4+1
        print("這個星形編號是s"+str(shape_sequence.count('s')))
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
        c.append(int(ans))
        shape_sequence.append(shape)
        shape_wide.append((int(ans)-1)) #圓形對應的最長為：圓形寬度為直徑-1
        print("這個圓形編號是c"+str(shape_sequence.count('c')))
    elif shape=='h':
        ans=input("請輸入梯形高：") #integrate 整合變數時發現弊病，變更輸入順序
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

        ans=input("請輸入梯形上邊長：")
        try:
            int(ans)
        except:
            print("輸入錯誤")
            continue
        if int(ans)<=0:
            print("輸入錯誤")
            continue
        h_length.append(int(ans))
        h.append(h_length)
        shape_sequence.append(shape)
        shape_wide.append(h_length[1]+2*(h_length[0]-1)) #梯形對應的最常寬度為：上邊+2*(高度-1)
        print("這個梯形編號是h"+str(shape_sequence.count('h')))
    elif shape=='exit':
        print("進入下一階段")
        break
    else:
        print("輸入錯誤，請重新輸入")
#進入畫圖階段
print("\nDraw_graphic")
print("------------------")
# print('t=',t)
# print('s=',s)
# print('c=',c)
# print('r=',r)
# print('h=',h)
# print('shape_sequence = ',shape_sequence)
# print('shape_wide = ',shape_wide)

'''
接下來交給string—sperater跟graphic了
'''


for count in range(0,len(shape_sequence)):
    space_num=int((max(shape_wide)-shape_wide[count])//2)
    if shape_sequence[0]=="t":  #畫三角形
        x=G.graph(t[0],0,space_num)#高
        x.draw_tri()
        t.pop(0)
    elif shape_sequence[0]=="s":#畫星形（尚未成功）
        x=G.graph(s[0],0,space_num)#邊長
        x.draw_star()
        s.pop(0)
    elif shape_sequence[0]=="c":#畫圓形（尚未成功）
        x=G.graph(c[0],0,space_num)#直徑
        x.draw_circle()
        c.pop(0) 
    elif shape_sequence[0]=="r":#畫矩形
        x=G.graph(r[0][0],r[0][1],space_num)
        x.draw_rec()
        r.pop(0)     
    elif shape_sequence[0]=="h":#畫梯形
        x=G.graph(h[0][0],h[0][1],space_num)
        x.draw_trap()
        h.pop(0)   
    shape_sequence.pop(0)