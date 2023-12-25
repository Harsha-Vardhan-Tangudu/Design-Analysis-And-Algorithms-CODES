def quicksort(A):

    if len(A)<=1:
        return A
    
    pivot = A[0]

    left=[]
    right=[]
    equal=[]

    for element in A:
        if element<pivot:
            left.append(element)
        elif element >pivot:
            right.append(element)
        else:
            equal.append(element)

    left= quicksort(left)
    right=quicksort(right)
    return left+equal+right


A=[1,5,2,3]
print(quicksort(A))