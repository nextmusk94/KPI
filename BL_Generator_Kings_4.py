import numpy as np

n = 4
ns = n*n
BW = 4
WW = 2

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
            # Up
            if coeff[i*n+j, 0] == 0:
                BL[j*BW] = BL[j*BW] * 16
                BL[j*BW] = BL[j*BW] + 0
            elif coeff[i*n+j, 0] == 1:
                BL[j*BW] = BL[j*BW] * 16
                BL[j*BW] = BL[j*BW] + 10
            elif coeff[i*n+j, 0] == -1:
                BL[j*BW] = BL[j*BW] * 16
                BL[j*BW] = BL[j*BW] + 8
            # UpRight
            if coeff[i*n+j, 1] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+2] = BL[j*BW+2] + 40
            elif coeff[i*n+j, 1] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+2] = BL[j*BW+2] + 42 
            elif coeff[i*n+j, 1] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 64
                BL[j*BW+3] = BL[j*BW+3] * 64
                BL[j*BW+2] = BL[j*BW+2] + 40
                BL[j*BW+3] = BL[j*BW+3] + 42
            # Right
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
            # DownRight
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










