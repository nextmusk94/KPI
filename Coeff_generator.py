import numpy as np

n = 8
m = 8
ns = n*m

coeff = np.random.randint(3, size = (n*m, 4))
coeff[coeff==2] = -1

def setzero(coeff):
    global n, m, ns
    for i in range(n):
        for j in range(m):
            if i == 0:
                coeff[i*n+j,0] = 0
                coeff[i*n+j,1] = 0
            if j == m-1:
                coeff[i*n+j,1] = 0
                coeff[i*n+j,2] = 0
                coeff[i*n+j,3] = 0
            if i == n-1:
                coeff[i*n+j,3] = 0
    return coeff

def Four2Eight(coeff_row):
    global n, m, ns
    coeff = np.zeros([ns, 8])
    for i in range(ns):
        coeff[i, 0] = coeff_row[i, 0]
        coeff[i, 1] = coeff_row[i, 1]
        coeff[i, 2] = coeff_row[i, 2]
        coeff[i, 3] = coeff_row[i, 3]
        if i >= n*(n-1):
            coeff[i, 4] = 0
        else:
            coeff[i, 4] = coeff_row[i+n, 0]
        if i % n == 0 or i >= n*(n-1):
            coeff[i, 5] = 0
        else:
            coeff[i, 5] = coeff_row[i-5, 1]
        if i % n == 0:
            coeff[i, 6] = 0
        else:
            coeff[i, 6] = coeff_row[i-1, 2]
        if i < n or i % n == 0:
            coeff[i, 7] = 0
        else:
            coeff[i, 7] = coeff_row[i-7, 3]

    return coeff

coeff = setzero(coeff)
coeff = Four2Eight(coeff)
print(coeff)

np.savetxt('coeff_8x8_1.csv', coeff, fmt='%d', delimiter=',')

