import math
import numpy as np
import matplotlib.pyplot as plt

# Set initial spins
def hot_start():
    global ns
    spin = np.random.randint(0, 2, ns)
    spin[spin == 0] = -1

    return spin

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

# The main Monte Carlo Loop

# beta represents 1/kT
def update1(spin, beta):
    global n, ns
    spin_temp = np.copy(spin)
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                E = kpi(spin, coeff, i*n+j)
                dE = -2*E
                if dE <= 0:
                    spin_temp[i*n+j] = -spin[i*n+j]
                elif np.exp(-beta*dE) >= np.random.rand():
                    spin_temp[i*n+j] = -spin[i*n+j]
    spin = np.copy(spin_temp)
    return spin

def update2(spin, beta):
    global n, ns
    spin_temp = np.copy(spin)
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 1:
                E = kpi(spin, coeff, i*n+j)
                dE = -2*E
                if dE <= 0:
                    spin_temp[i*n+j] = -spin[i*n+j]
                elif np.exp(-beta*dE) >= np.random.rand():
                    spin_temp[i*n+j] = -spin[i*n+j]
    spin = np.copy(spin_temp)
    return spin

def update3(spin, beta):
    global n, ns
    spin_temp = np.copy(spin)
    for i in range(n):
        for j in range(n):
            if i % 2 == 1 and j % 2 == 0:
                E = kpi(spin, coeff, i*n+j)
                dE = -2*E
                if dE <= 0:
                    spin_temp[i*n+j] = -spin[i*n+j]
                elif np.exp(-beta*dE) >= np.random.rand():
                    spin_temp[i*n+j] = -spin[i*n+j]
    spin = np.copy(spin_temp)
    return spin

def update4(spin, beta):
    global n, ns
    spin_temp = np.copy(spin)
    for i in range(n):
        for j in range(n):
            if i % 2 == 1 and j % 2 == 1:
                E = kpi(spin, coeff, i*n+j)
                dE = -2*E
                if dE <= 0:
                    spin_temp[i*n+j] = -spin[i*n+j]
                elif np.exp(-beta*dE) >= np.random.rand():
                    spin_temp[i*n+j] = -spin[i*n+j]
    spin = np.copy(spin_temp)
    return spin

# Main

coeff = np.loadtxt('./coeff_4x4_1.csv', delimiter=',')
n = 4
ns = n*n
iteration = 2000
beta = 0
step = 0.002

print(f"Size = {n}")
print(f"iteration = {iteration}")
spin = hot_start()
KPI = np.zeros(iteration)

for i in range(iteration):
    spin = update1(spin, beta)
    spin = update2(spin, beta)
    spin = update3(spin, beta)
    spin = update4(spin, beta)
    beta = beta + step
    for j in range(ns):
        KPI[i] = KPI[i] + kpi(spin, coeff, j)

print(np.amin(KPI))

plt.figure(figsize=(10, 6))
plt.plot(KPI)
plt.title('4x4 Spin2 by CPU', fontsize=18)
plt.xlabel('Iteration', fontsize=10)
plt.ylabel('KPI', fontsize=10)
plt.grid()
plt.show()





