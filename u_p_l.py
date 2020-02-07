oupro=[]
inpro=[]
while 1:
    pro=input("請輸入商品名稱：")
    if pro == "q":
        break
    pri=input("請輸入商品價格：")
    oupro.append([pro,'$'+pri])
print("您總共買了",len(oupro),"項商品，分別是：")
print(oupro)
print("已存入 '記帳檔案' 中。")
with open('記帳檔案.csv','w')as fi:
    fi.write("名稱"+","+"價格"+"\n")
    for i in (oupro):
        fi .write(i[0]+','+i[1]+'\n')

