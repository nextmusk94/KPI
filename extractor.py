import numpy as np

spin = np.loadtxt('./spin1_4x4_5.csv', delimiter=',')
n = 4
ns = n*n
check = 0
cnt = 0
spin_extract = np.zeros([ns, 2000])
for i in range(len(spin[:, 0])):
    if spin[i, 0] > 0.8 and check == 0:
        check = 1
    elif spin[i, 0] < 0.1 and check == 1:
        check = 0
        if i+100 < len(spin[:,0]):
            print(spin[i+100, 0])
            spin_extract[:, cnt] = spin[i+100, 1:]
        cnt = cnt + 1

spin_final = np.zeros([ns, cnt-1])
for i in range(cnt-1):
    spin_final[:, i] = spin_extract[:, i]
spin_final[spin_final > 0.5] = 1
spin_final[spin_final <= 0.5] = -1

np.savetxt('spin1_4x4_5_ex.csv', spin_final, fmt = '%d', delimiter=',')