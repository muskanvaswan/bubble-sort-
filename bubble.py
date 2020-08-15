def bubble_sort(l):
    ran = list(range(len(l)1 4 2 5 3 9 6))
    ran.reverse()
    for k in ran:
        for i in range(k):
            if l[i]>l[i+1]:
                x = l[i]
                l[i]=l[i+1]
                l[i+1]=x
            else:
                continue
    return l

lst = [int(item) for item in input("Enter list (seperated by space): ").split()]
print(bubble_sort(lst))
