def linear(L, x):
    # if the value is existis the function will return the position of the value
    n = len(L)

    for item in range(n):
        if L[item] == x:
            return item
    return -1

if __name__=="__main__":
    L = [3,4,5,6,10,23]
    x = int(input())
    result = linear(L,x)
    print(result)