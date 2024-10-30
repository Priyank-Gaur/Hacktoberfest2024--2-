n=int(input())
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        left=j
        right=(2*n-1-1)-j
        down=(2*n-1-1)-i
        print(n-min(top,left,right,down),end=" ")
        j+=1
    print()
