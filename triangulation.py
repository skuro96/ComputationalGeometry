import numpy as np
import matplotlib.pyplot as plt

def dist(a, b): return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) 

# 6角形のサンプル
p = [
    [1, 8],
    [4, 8],
    [7, 7],
    [7, 3],
    [3, 0],
    [0, 3]
]

"""
# 7角形のサンプル
p = [
    [1, 11], 
    [2, 4], 
    [16, 3], 
    [21, 13], 
    [18, 22], 
    [9, 23], 
    [3, 19]
]
"""

n = len(p)
t = np.zeros((n, n+1))
t_pt = [[[] for j in range(n+1)] for i in range(n)]

for s in range(4, n+1):
    for i in range(n):
        min = np.inf
        for j in range(i+1, i+s-1):
            if j == i+1:
                tmp = dist(p[j % n], p[(i+s-1) % n]) + t[(i+1) % n][(s-1) % n]
                tmp_pt = [[j % n, (i+s-1) % n]]
                tmp_pt.extend(t_pt[(i+1) % n][(s-1) % n])
            elif j == i+s-2:
                tmp = dist(p[i % n], p[j % n]) + t[i % n][(s-1) % n]
                tmp_pt = [[i % n, j % n]]
                tmp_pt.extend(t_pt[i % n][(s-1) % n])
            else:
                tmp = dist(p[i % n], p[j % n]) + dist(p[j % n], p[(i+s-1) % n]) + t[i % n][(j-i+1) % n] + t[j % n][(s-j+i) % n]
                tmp_pt = [[i % n, j % n], [j % n, (i+s-1) % n]]
                tmp_pt.extend(t_pt[i % n][(j-i+1) % n])
                tmp_pt.extend(t_pt[j % n][(s-j+i) % n])
            
            if tmp < min:
                min = tmp
                min_pt = tmp_pt

        t[i][s] = min
        t_pt[i][s] = min_pt
        if s == n and i == 0:
            break

ans = t[0][n]
ans_pt = t_pt[0][n]
print("辺長和の最小値:", ans)
print("内部の辺:", ans_pt)

p.append(p[0])
x, y = zip(*p)
plt.axes().set_aspect('equal')
plt.scatter(x, y, color='k')
for i in range(len(p)-1):
    plt.plot([p[i][0], p[i+1][0]], [p[i][1], p[i+1][1]], color='r')
for i in range(len(ans_pt)):
    plt.plot([p[ans_pt[i][0]][0], p[ans_pt[i][1]][0]], [p[ans_pt[i][0]][1], p[ans_pt[i][1]][1]], color='r')
plt.show()
