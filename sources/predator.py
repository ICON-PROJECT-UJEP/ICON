import numpy as np
from random import randint

def first_member(xs, min, max):
    for x in xs:
        if min <= x <= max:
            return x

def sqeel(t0, dt, s_points, h_points):
    if (any(t0 <= sp <= t0+dt for sp in s_points)
            and (t0 <= hp <= t0 + dt for hp in h_points)):
        return (t0 + dt - first_member(s_points, t0, t0 + dt)) / dt
    else:
        return 0.0

def get_indexes(imin, imax, n):
    assert imax - imin + 1 > n, "Not enough points in interval"
    indexes = []
    dx = (imax - imin) / (n-1)
    for i in range(n-1):
        indexes.append(round(i * dx - 0.5) + imin)
    indexes.append(imax-1)
    return indexes

def get_data(nsamples, di, n):
    sources = [
        ("/home/fiser/IKON/ICON/mereni/26_02_2020_11_38/1hp.txt",
         "/home/fiser/IKON/ICON/anotace/1hp.a.csv"),
        ("/home/fiser/IKON/ICON/mereni/26_02_2020_11_38/1hp2.txt",
         "/home/fiser/IKON/ICON/anotace/1hp2.a.csv")
    ]
    rsamples = []
    rlabels = []

    for data, annot in sources:
        fs = 250
        d = np.loadtxt(data)
        a = np.loadtxt(annot, delimiter=",", converters={1: lambda c: float(b"SHF".index(c))})
        s_points = a[a[:,1] == 0.0, 0]
        h_points = a[a[:, 1] == 1.0, 0]
        for _ in range(nsamples):
            i = randint(0, len(d) - di - 2)
            rsamples.append(d[get_indexes(i, i + di, n)])
            rlabels.append(sqeel(i/fs, di/fs, s_points, h_points))
    return rsamples, rlabels

inputs, labels = get_data(100, 75, 5)
print(inputs)
print(labels)