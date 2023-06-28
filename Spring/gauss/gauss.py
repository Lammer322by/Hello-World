import numpy


def gauss(a, b):
    a = a.copy()
    b = b.copy()
    N = len(b)

    def forward():
        for i in range(N):             # номер строки которую мы модифицируем
            if a[i, i] == 0.0:            # если на главной диагонали стоит нулевой коэффициент, меняем местами
                for t in range(i, N):  #  i-ю и первую строку с ненулевым коэффициентом в i-м столбце
                    if a[t,i] != 0.0:
                        a[i] = a[i] + a[t]
                        a[t] = a[i] - a[t]
                        a[i] = a[i] - a[t]
            if a[i, i] == 0.0:
                continue
            else:
                #a[i] = a[i] / a[i,i]
                for j in range(i+1, N):  #модифицируем строки, лежащие ниже текущей
                    b[j] = b[j] - ((b[i] * a[j, i]) / a[i, i])
                    a[j] = a[j] - ((a[i] * a[j, i]) / a[i, i])


    def backward():
        x = numpy.zeros(len(b), dtype=float)

        for i in range(N-1, -1, -1):
            if a[i, i] == 0.0:   #в этом случае у нас весь столбец нулевой и система от него не зависит существенно
                x[i] = 0.0      #тогда для удобства положим x[i] = 0
            else:
                x[i] = b[i]     #находим оставшиеся переменные
                for j in range(i+1, N):
                    x[i] = x[i] - (a[i, j] * x[j])
                x[i] = x[i] / a[i, i]
                #x[i] = round(x[i], 4)
        return x

    forward()
    x = backward()
    return x
