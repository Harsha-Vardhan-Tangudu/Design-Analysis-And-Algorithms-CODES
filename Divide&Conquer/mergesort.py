def mergesort(arr):
    n=len(arr)

    if n>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]

        i = j = k =0

        mergesort(l)
        mergesort(r)

        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i=i+1
            else:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            k=k+1
            i+=1

        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
            
    return arr

arr=[5,4,3,6]
p=mergesort(arr)
print(p)