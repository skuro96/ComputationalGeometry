def cross(lines, i, j):
    return (lines[j][1] - lines[i][1]) / (lines[i][0] - lines[j][0])


def f(L, lines, x0):
    maxi = []
    max = -float('inf')
    for i in range(len(L)):
        tmp = lines[L[i]][0]*x0 + lines[L[i]][1]
        if abs(max - tmp) < 1e-7:
            maxi.append(L[i])
        elif max < tmp:
            max = tmp
            maxi = [L[i]]
    return maxi


def remove_line(L, lines, cross_x, pairs, i):
    L.remove(i)
    cross_x.clear()
    pairs.clear()
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            cross_x.append(cross(lines, L[i], L[j]))
            pairs.append([L[i], L[j]])


lines = [[-1/2, 8], [1, -3], [1/2, 1], [-1/4, 5], [2/3, -3], [-3/2, 9]]
#lines = [[-3, 15], [-2, 16], [-4/5, 13], [-1/5, 13], [-3/5, 15], [2, -5], [1, 4], [1/2, 5]]

L = [i for i in range(len(lines))]
n = len(lines)

cross_x = []
pairs = []
for i in range(n):
    for j in range(i+1, n):
        cross_x.append(cross(lines, i, j))
        pairs.append([i, j])


while len(L) > 2:
    print(L)
    n = len(L)

    x = [cross(lines, L[i], L[i+int(n/2)]) for i in range(int(n/2))]
    x.sort()
    x0 = x[int((len(x)-1)/2)]
    I = f(L, lines, x0)

    idx = [i for i in I]
    ai = [lines[i][0] for i in I]
    a_max = max(ai)
    a_min = min(ai)

    if a_min < 0 and 0 < a_max:
        break

    elif a_min < 0: 
        while len(I) > 1:
            ai = [lines[i][0] for i in I]
            a_mini = I[0]
            a_min = lines[a_mini][0]
            for i in range(len(I)):
                if a_min > ai[i]:
                    a_min = ai[i]
                    a_mini = I[i]
            remove_line(L, lines, cross_x, pairs, a_mini)
            I.remove(a_mini)
        
        remove_list = []
        for i in range(len(cross_x)):
            if cross_x[i] < x0:
                tmp_1 = pairs[i][0]
                tmp_2 = pairs[i][1]
                if lines[tmp_1][0] < lines[tmp_2][0]:
                    remove_list.append(tmp_1)
                else:
                    remove_list.append(tmp_2)
        rmv = list(set(remove_list))

    elif 0 < a_max:
        while len(I) > 1:
            ai = [lines[i][0] for i in I]
            a_maxi = I[0]
            a_max = lines[a_mini][0]
            for i in range(len(I)):
                if a_max < ai[i]:
                    a_max = ai[i]
                    a_maxi = I[i]
            remove_line(L, lines, cross_x, pairs, a_maxi)
            I.remove(a_maxi)
        
        remove_list = []
        for i in range(len(cross_x)):
            if cross_x[i] > x0:
                tmp_1 = pairs[i][0]
                tmp_2 = pairs[i][1]
                if lines[tmp_1][0] > lines[tmp_2][0]:
                    remove_list.append(tmp_1)
                else:
                    remove_list.append(tmp_2)
        rmv = list(set(remove_list))

    for i in rmv:
        remove_line(L, lines, cross_x, pairs, i)

print(L)
print('最適解の座標は (', cross_x[0], ', ', lines[L[0]][0]*cross_x[0]+lines[L[0]][1], ')', sep='')

'''
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3]
[0, 1, 2]
[0, 2]
最適解の座標は (7.0, 4.5)
'''

'''
[0, 1, 2, 3, 4, 5, 6, 7]
[3, 5, 6]
[3, 6]
最適解の座標は (7.5, 11.5)
'''