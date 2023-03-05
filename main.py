def U_0_t(t):
    return 1 / (alfa * t + 1)

def U_1_t(t):
    return 1 / (alfa * t + 2)

# alpha(x)
def U_x_0(x):
    return 1 / (1 + x)

# alpha''(x)
def d2_U_x_0(x):
    return 2 / (x + 1)**3

# betta(x)
def U_x_0_t1(x):
    return -alfa / ((1 + x) ** 2)

def f_x_t(x, t):
    return 2 * (alfa ** 2 - 1) / ((x + alfa * t + 1) ** 3)

N = 14
alfa = 0.5 + 0.1 * N
l = 1
T = 1
n = 10
m = 10
h = l / n
tau = T / m

x = [i * h for i in range(n + 1)]
t = [i * tau for i in range(m + 1)]
u = [[0 for i in range(n + 1)] for j in range(n + 1)]

#граничные условия
for i in range(m + 1):
    u[0][i] = U_0_t(t[i])
    u[n][i] = U_1_t(t[i])

"Подставив это значение в (9), найдем"
for i in range(1, n + 1):
    u[i][0] = U_x_0(x[i])  # alpha(x)
              # alpha(x)              betta(x)
    u[i][1] = U_x_0(x[i]) + tau * U_x_0_t1(x[i]) + ((tau ** 2) / 2) * (d2_U_x_0(x[i]) + f_x_t(x[i], 0))

"Решение   выражается явным образом через значения на предыдущих слоях "
s = (tau ** 2) / (h ** 2)
for j in range(1, m):
    for i in range(1, n):
        u[i][j + 1] = s * u[i + 1][j] + 2 * (1 - s) * u[i][j] + s * u[i - 1][j] - u[i][j - 1] + tau ** 2 * f_x_t(x[i],t[j])

print("Значения на временных слоях:")
n = len(u)
k = len(u[0])
print("      x = |       0         0.1        0.2        0.3        0.4        0.5        0.6        0.7        0.8        0.9         1")
print("-----------------------------------------------------------------------------------------------------------------------------------")
for Col in range(k - 1, -1, -1):
    print('t = ', Col / 10, end="  |")
    for Row in range(n):
        print("{0:10.4f}".format(u[Row][Col]), end=" ")
    print()
print()

