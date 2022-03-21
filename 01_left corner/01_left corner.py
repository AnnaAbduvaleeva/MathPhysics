import numpy as np

M = 100
lst_x = np.linspace(0, 1, M+1)
lst_u = np.array([1 if 0.1 < i <= 0.2 else 0 for i in lst_x])
lst_new = np.zeros(101)


def calc_left_corner(lst_u, lst_new, i):
    h = 0.01
    t = 1
    lst_new[i] = t * 0.01 / h * (lst_u[i-1] - lst_u[i]) + lst_u[i]
    return lst_new[i]


for time in range(1, 50):
    for i in range(1, 100):
        lst_new[i] = calc_left_corner(lst_u, lst_new, i)

lst_new[0] = 0
lst_new[100] = 0

print(lst_x)
print(lst_new)
f = open("text.txt", "w")
f.write()
f.close()