import array as ar
q=int(input("Enter the length of the fionachhi series to be determined: "))
a=ar.array('i',[0,1])
m=1
n=0
new=0
count=2
if q<=0:
    print("enter proper length")
elif q==1:
    print(a[0])
elif q==2:
    print(a[0], end=",")
    print(a[1])
else:
    while(count<q):
        new=m+n
        a.append(new)
        n=m
        m=new
        count+=1
    for i in a:
        print(i, end=",")
    print()
