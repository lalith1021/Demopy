print("Hi from git")
#selection sort
def sort(a):
    for i in range(0,len(a)-1):
        min=i
        for j in range(i,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
        print(a)
    print("Final sorted:")
    print(a)

a=[800,100,130,30,0]
sort(a)
