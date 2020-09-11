import matplotlib.pyplot as plt
import random
import time
import sys

def signed_area(a, b, c):
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) / 2.0

def merge_sort_argument(data, x_min):
    l = len(data)
    if l >= 2:
        left = merge_sort_argument(data[:(l//2)], x_min)
        right = merge_sort_argument(data[(l//2):], x_min)

        ans = []
        while len(left) != 0 and len(right) != 0:
            if signed_area(x_min, left[0], right[0]) > 0:
                ans.append(left.pop(0))
            else:
                ans.append(right.pop(0))
        if len(left) != 0:
            ans.extend(left)
        elif len(right) != 0:
            ans.extend(right)
        return ans
    else:
        return data

"""
data = [
    [6, 12],
    [14, 8],
    [1, 11],
    [2, 4],
    [18, 22],
    [8, 5],
    [11, 10],
    [3, 19],
    [9, 23],
    [16, 3],
    [21, 13],
    [10, 18]
]
"""

N = int(input('input n:'))
data = [[random.randint(0, N**2), random.randint(0, N**2)] for i in range(N)]

if N == 0:
    sys.exit()

#start = time.time()

n = len(data)
min_i = 0
min_x = data[0][0]
for i in range(n):
    if data[i][0] < min_x:
        min_x = data[i][0]
        min_i = i

d = list(data)
x_min = d.pop(min_i)
q = merge_sort_argument(d, x_min)
q.insert(0, x_min)
q.append(q[0])

v = [q[0], q[1], q[2]]

for i in range(3, n+1):
    print(v)
    k = len(v) - 1
    while signed_area(v[k-1], v[k], q[i]) < 0:
        v.pop(k)
        k -= 1
        print(v)
    v.append(q[i])
print(v)

#end = time.time()
#print(end - start , 'sec.')

x, y = zip(*data)
plt.scatter(x, y, color="k")
for i in range(len(v)-1):
    plt.plot([v[i][0], v[i+1][0]], [v[i][1], v[i+1][1]], color="r")
plt.show()
