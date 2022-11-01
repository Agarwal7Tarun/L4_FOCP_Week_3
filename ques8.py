num=int(input("Enter the number for times table: "))
if num>0:
    for i in range(0,13):
        mul=i*num
        print("%d X %d = %d" %(i,num,mul))
else:
    for i in range(12,-1,-1):
        mul=i*num
        print("%d X %d = %d" %(i,num,mul))