import numpy as np

n = 4
m = 4
ns = n*m
BW = 4
WW = 6

def D2B(dec):
    global BL_temp
    dec = int(dec)
    if dec >= 1:
        D2B(dec//2)
        BL_temp = np.append(BL_temp, dec % 2)


def vbit_pattern(coeff):
    global n, m, ns, BW
    BL = np.zeros(BW*n, dtype=np.float64)
    for i in range(n):
        for j in range(m):
            # Up
            if coeff[i*n+j, 0] == 0:
                BL[j*BW] = BL[j*BW] * 16
            elif coeff[i*n+j, 0] == 1:
                BL[j*BW] = BL[j*BW] * 16
                BL[j*BW] = BL[j*BW] + 10
            elif coeff[i*n+j, 0] == -1:
                BL[j*BW] = BL[j*BW] * 16
                BL[j*BW] = BL[j*BW] + 2
            # UpRight
            if coeff[i*n+j, 1] == 0:
                BL[j*BW+1] = BL[j*BW+1] * 16
            elif coeff[i*n+j, 1] == 1:
                BL[j*BW+1] = BL[j*BW+1] * 16
                BL[j*BW+1] = BL[j*BW+1] + 10 
            elif coeff[i*n+j, 1] == -1:
                BL[j*BW+1] = BL[j*BW+1] * 16
                BL[j*BW+1] = BL[j*BW+1] + 2
            # Right
            if coeff[i*n+j, 2] == 0:
                BL[j*BW+2] = BL[j*BW+2] * 16
            elif coeff[i*n+j, 2] == 1:
                BL[j*BW+2] = BL[j*BW+2] * 16
                BL[j*BW+2] = BL[j*BW+2] + 10 
            elif coeff[i*n+j, 2] == -1:
                BL[j*BW+2] = BL[j*BW+2] * 16
                BL[j*BW+2] = BL[j*BW+2] + 2
            # DownRight
            if coeff[i*n+j, 3] == 0:
                BL[j*BW+3] = BL[j*BW+3] * 16
            elif coeff[i*n+j, 3] == 1:
                BL[j*BW+3] = BL[j*BW+3] * 16
                BL[j*BW+3] = BL[j*BW+3] + 10 
            elif coeff[i*n+j, 3] == -1:
                BL[j*BW+3] = BL[j*BW+3] * 16
                BL[j*BW+3] = BL[j*BW+3] + 2
    return BL

# Main
coeff = np.loadtxt('./coeff_4x4_1.csv', delimiter=',')
BL_dec = vbit_pattern(coeff)
BL_bin = np.zeros([BW*m, 2*n*2])
BL_bin2 = np.zeros([BW*m, WW*n*2])

for i in range(BW*m):
    BL_temp = np.zeros(0)
    D2B(BL_dec[i])
    print(BL_temp)

    if BL_temp.size == 14:
        BL_bin[i] = np.concatenate(([0,0], BL_temp), axis=None)
    elif BL_temp.size == 12:
        BL_bin[i] = np.concatenate(([0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 10:
        BL_bin[i] = np.concatenate(([0,0,0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 8:
        BL_bin[i] = np.concatenate(([0,0,0,0,0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 6:
        BL_bin[i] = np.concatenate(([0,0,0,0,0,0,0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 4:
        BL_bin[i] = np.concatenate(([0,0,0,0,0,0,0,0,0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 2:
        BL_bin[i] = np.concatenate(([0,0,0,0,0,0,0,0,0,0,0,0,0,0], BL_temp), axis=None)
    elif BL_temp.size == 0:
        BL_bin[i] = np.zeros(16)
    else :
        BL_bin[i] = BL_temp

for i in range(BW*m):
    cnt = 0
    for j in range(WW*n*2):
        if j % 12 == 0 or j % 12 == 1 or j % 12 == 2 or j % 12 == 3:
            BL_bin2[i,j] = BL_bin[i,cnt]
            cnt = cnt + 1
        elif j % 12 == 5 or j % 12 == 7 or j % 12 == 9 or j % 12 == 11:
            BL_bin2[i,j] = 0
        elif j % 12 == 4 or j % 12 == 8:
            BL_bin2[i,j] = 1
        elif j % 12 == 6 or j % 12 == 10:
            BL_bin2[i,j] = 0

np.savetxt('BL_bit.csv', BL_bin2, fmt='%d', delimiter='')










