def polynomial(x, coef):
    n = len(coef)
    s = 0
    for i in range(0,n):
        s = s*x+coef[i]
    return s

cf = [1,2,3,4,5]
# 2^4+2*2^3+3*2^2+4*2+5
print(polynomial(2,cf))