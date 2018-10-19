def binarySearch(L, x):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right) // 2    # integer division

        if L[mid] == x:
            return mid      # got the result in correct position
        elif L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__=="__main__":
    L = [1,2,3,4,5,6,7,8,9]


    for x in range(1, 11):
        position = binarySearch(L, x)

        if position == -1:
            if x in L:
                print(x, "is in  L but function returned -1")
            else:
                print(x," is not found")
        else:
            if L[position] == x:
                print(x, " found in correct position")
            else:
                print("binary search returned ", position, " for ", x , "which is not correct")