import numpy as np
import matplotlib.pyplot as plt

def coarray(coeff_row):
    global n, ns
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

# Calculate KPI
def kpi(spin, coeff, N):
    global n, ns
    kpi_temp = 0
    for i in range(8):
        if coeff[N, i] != 0:
            if i == 0:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N-n]
            elif i == 1:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N-n+1]
            elif i == 2:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N+1]
            elif i == 3:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N+n+1]
            elif i == 4:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N+n]
            elif i == 5:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N+n-1]
            elif i == 6:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N-1]
            elif i == 7:
                kpi_temp = kpi_temp - coeff[N, i] * spin[N] * spin[N-n-1]

    return kpi_temp

# Main
coeff_row = np.loadtxt('./coeff2.csv', delimiter=',')
spin = np.loadtxt('./spin2_sweep2_extracted.csv', delimiter=',')

n = 6
ns = n*n

print(f"Size = {n}")
coeff = coarray(coeff_row)
np.savetxt('coeff2_trans.csv', coeff, fmt='%d', delimiter=',')
KPI = np.zeros(spin[0, :].shape)

for i in range(len(KPI)):
    for j in range(ns):
        KPI[i] = KPI[i] + kpi(spin[:, i], coeff, j)
print(KPI)

plt.figure(figsize=(10, 6))
plt.plot(KPI)
plt.title('VDDL = 950mV', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('KPI', fontsize=10)
plt.grid()
plt.show()




