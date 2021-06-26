a=[10,25,31]
for i in range(len(a)):
        for j in range(len(a)):
            if a[i]>a[j]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
            print(a)