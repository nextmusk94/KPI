import numpy as np
import matplotlib.pyplot as plt

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
coeff = np.loadtxt('./coeff8_4x4_1.csv', delimiter=',')
spin = np.loadtxt('./spin1_1V_800mV_1_ex.csv', delimiter=',')

n = 4
ns = n*n

print(f"Size = {n}")
KPI = np.zeros(spin[0, :].shape)

for i in range(len(KPI)):
    for j in range(ns):
        KPI[i] = KPI[i] + kpi(spin[:, i], coeff, j)
print(KPI)

plt.figure(figsize=(10, 6))
plt.plot(KPI)
plt.title('VDDRND = 1V, VDDL = 800mV', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('KPI', fontsize=10)
plt.grid()
plt.show()




