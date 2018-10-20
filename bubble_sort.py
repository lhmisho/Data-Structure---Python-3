def bubblo_sort(L):
    n = len(L)

    for i in range(0, n):
        for j in range(0, n-i-1):
            # if L[j] < L[j+1]:                    # decending order
            #     L[j], L[j+1] = L[j+1], L[j]

            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
if __name__=="__main__":
    L = [3,2,2,5,4,6,8,7]
    print("Before sort: ", L)
    bubblo_sort(L)
    print("After sort:", L)

