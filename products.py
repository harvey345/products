pro=[]
ppp=[]
while True:
    x=input("請輸入商品名稱：")
    
    if x == 'q':
        break
    p=input("請輸入商品價格：")
    ppp=[]
    ppp.append(x)
    ppp.append("$"+p)
    pro.append(ppp)
print("您共買了",len(pro),"項商品，分別是：",end=" ")
print(pro)
