ar = [int(item) for item in input("Enter array to be sorted: ").split(" ")]

def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        lh = a[:mid]
        rh = a[mid:]
        merge_sort(lh)
        merge_sort(rh)


        //merging the arrays
        i = j = k = 0
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                a[k]=lh[i]
                i=i+1
            else:
                a[k]=rh[j]
                j=j+1
            k=k+1

        while i < len(lh):
            a[k]=lh[i]
            i=i+1
            k=k+1

        while j < len(rh):
            a[k]=rh[j]
            j=j+1
            k=k+1

merge_sort(ar)
print(ar)
