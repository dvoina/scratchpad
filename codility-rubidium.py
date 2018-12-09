    
def intersect(x1, y1, x2, y2, d):
    return max(abs(x2-x1), abs(y2-y1))<2*d

def solution(X, Y):
    # write your code in Python 3.6
    n = len(X)
    d=max(max(X), max(Y))/2
    while d>0:
        flg = False
        for i in range(n-1):
            for j in range(i+1, n):
                if intersect(X[i], Y[i], X[j], Y[j], d):
                    flg = True
                    break
            if flg:
                break
        if flg:
            d = d-1
            continue
        else:
            break
    return int(d)

print(solution([0, 2], [0, 0]))
print(solution([0, 0, 10, 10], [0, 10, 0, 10])) 
print(solution([1, 1, 8], [1, 6, 0])) 
