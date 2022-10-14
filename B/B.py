def vector(n):
    counter = 0
    best = 0
    for i in range(n):
        if int(input()) > 0:
            counter+=1
        else:
            counter = 0
        best = max(best, counter)
    return best

print(vector(int(input())))
