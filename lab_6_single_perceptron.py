#single layer perceptron
T = [
    [0.1, 0.1, -1, 1],
    [0.2, 0.1, -1, 1],
    [0.5, 0.1, -1, 2],
    [0.6, 0.1, -1, 2],
    [0.3, 0.3, -1, 3],
    [0.4, 0.3, -1, 3]
]
w = [
    [-0.1, 0.15, 0.2],
    [-0.2, 0.11, 0.17],
    [0.17, 0.16, 0.11]
]
d = [
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
]

def sgn(net):
    if net > 0:
        return 1
    else:
        return -1

error = 1
counter = 0

while error != 0:
    e = [0, 0, 0]

    for k in range(6):
        o = [0, 0, 0]
        for i in range(3):
            summation = 0
            for j in range(3):
                net = T[k][j] * w[i][j]
                summation += net
            o[i] = sgn(summation)

        for l in range(3):
            s = T[k][3] - 1
            for m in range(3):
                w[l][m] = w[l][m] + 0.5 * (d[s][l] - o[l]) * T[k][m]
            e[l] = 0.5 * (d[s][l] - o[l]) ** 2

        print("error at epoch " + str(counter) + ": " + str(e))
        counter += 1

    error = sum(e)

print(f"Converged after {counter} epochs.")
print(f"Updated weights:\n{w}")
