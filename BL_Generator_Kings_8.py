import numpy as np

n = 4
ns = n*n
BW = 4
WW = 6

def D2B(dec):
    global BL_temp
    dec = int(dec)
    if dec >= 1:
        D2B(dec//2)
        BL_temp = np.append(BL_temp, dec % 2)


def vbit_pattern(coeff):
    global n, ns, BW
    BL = np.zeros(24, dtype=np.float64)
    for i in range(n):
        for j in range(n):
            # N
            if coeff[i*n+j, 0] == 0:
                BL[j*BW] = BL[j*BW] * 64
                BL[j*BW+1] = BL[j*BW+1] * 64
                BL[j*BW] = BL[j*BW] + 40
                BL[j*BW+1] = BL[j*BW+1] + 40
            elif coeff[i*n+j, 0] == 1:
                BL[j*BW] = BL[j*BW] * 64
                BL[j*BW+1] = BL[j*BW+1] * 64
                BL[j*BW] = BL[j*BW] + 42
                BL[j*BW+1] = BL[j*BW+1] + 40
            elif coeff[i*n+j, 0] == -1:
                BL[j*BW] = BL[j*BW] * 64
                BL[j*BW+1] = BL[j*BW+1] * 64
                BL[j*BW] = BL[j*BW] + 40
                BL[j*BW+1] = BL[j*BW+1] + 42
            # NE
            if coeff[i*n+j, 1] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+3] = BL[j*BW+3] * 64
                BL[j*BW+2] = BL[j*BW+2] + 40
                BL[j*BW+3] = BL[j*BW+3] + 40
            elif coeff[i*n+j, 1] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+3] = BL[j*BW+3] * 64
                BL[j*BW+2] = BL[j*BW+2] + 42
                BL[j*BW+3] = BL[j*BW+3] + 40
            elif coeff[i*n+j, 1] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+3] = BL[j*BW+3] * 64
                BL[j*BW+2] = BL[j*BW+2] + 40
                BL[j*BW+3] = BL[j*BW+3] + 42
            # E
            if coeff[i*n+j, 2] == 0:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
            elif coeff[i*n+j, 2] == 1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW] = BL[j*BW] + 2
            elif coeff[i*n+j, 2] == -1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW+1] = BL[j*BW+1] + 2
            # SE
            if coeff[i*n+j, 3] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
            elif coeff[i*n+j, 3] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+2] = BL[j*BW+2] + 2
            elif coeff[i*n+j, 3] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+3] = BL[j*BW+3] + 2
            # S
            if coeff[i*n+j, 4] == 0:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW + 1] = BL[j*BW+1] * 4
            elif coeff[i*n+j, 4] == 1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW] = BL[j*BW] + 2
            elif coeff[i*n+j, 4] == -1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW+1] = BL[j*BW+1] + 2
            # SW
            if coeff[i*n+j, 5] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
            elif coeff[i*n+j, 5] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+2] = BL[j*BW+2] + 2
            elif coeff[i*n+j, 5] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+3] = BL[j*BW+3] + 2
            # W
            if coeff[i*n+j, 6] == 0:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW + 1] = BL[j*BW+1] * 4
            elif coeff[i*n+j, 6] == 1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW] = BL[j*BW] + 2
            elif coeff[i*n+j, 6] == -1:
                BL[j*BW] = BL[j*BW] * 4
                BL[j*BW+1] = BL[j*BW+1] * 4
                BL[j*BW+1] = BL[j*BW+1] + 2
            # NW
            if coeff[i*n+j, 7] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
            elif coeff[i*n+j, 7] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+2] = BL[j*BW+2] + 2
            elif coeff[i*n+j, 7] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 4
                BL[j*BW+3] = BL[j*BW+3] * 4
                BL[j*BW+3] = BL[j*BW+3] + 2
    return BL

# Main
coeff = np.loadtxt('./coeff8_4x4_1.csv', delimiter=',')
BL_dec = vbit_pattern(coeff)
BL_bin = np.zeros([BW*n, WW*n*2])


for i in range(BW*n):
    BL_temp = np.zeros(0)
    D2B(BL_dec[i])
    print(BL_temp)
    BL_bin[i] = BL_temp

np.savetxt('BL_bit1.csv', BL_bin, fmt='%d', delimiter='')










