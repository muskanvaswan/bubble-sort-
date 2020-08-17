ar = [int(item) for item in input("Enter array to be sorted: ").split(" ")]

def selection_sort(a):
    for i in range(len(a)-1):
        smallest = i
        for j in range(i+1, len(a)-1):
            if a[j]<a[smallest]:
                smallest = j
            else:
                continue
        if smallest == i:
            continue
        else:
            x = a[i]
            a[i]= a[smallest]
            a[smallest]= x

    return a

print(selection_sort(ar))
