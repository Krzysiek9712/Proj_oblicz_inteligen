from sklearn.cluster import KMeans
from scipy.stats import norm
from csv import reader

import matplotlib.pyplot as plt
import numpy as np
import pyransac3d

# mns = [(5, 3), (15, 4), (10, 8)]
# scales = [(2, 1), (1, 1), (1, 2)]
#
# params = zip(mns, scales)
#
# clusters = []
#
# for parset in params:
#     dist_x = norm(loc=parset[0][0], scale=parset[1][0])
#     dist_y = norm(loc=parset[0][1], scale=parset[1][1])
#     cluster_x = dist_x.rvs(size=100)
#     cluster_y = dist_y.rvs(size=100)
#     cluster = zip(cluster_x, cluster_y)
#     clusters.extend(cluster)
#
# x, y = zip(*clusters)
# plt.figure()
# plt.scatter(x, y)
# plt.title('Punkty w 2D', fontsize=12)
# plt.tight_layout
# plt.xlabel('Os_X')
# plt.ylabel('Os Y')


def read_csv(name, nl="\n", dl=","):
    cloud = []
    with open(name, newline=nl) as csvfile:
        csvreader = reader(csvfile, delimiter=dl)
        for xx,yy,zz in csvreader:
            cloud.append([float(xx),float(yy),float(zz)])
    return cloud


cloud_points = read_csv("cloud_points.xyz")

clusterer = KMeans(n_clusters=3)

X = np.array(cloud_points)
y_pred = clusterer.fit_predict(X)

red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

plt.figure()
plt.scatter(X[red, 0], X[red, 1], c="red")
plt.scatter(X[blue, 0], X[blue, 1], c="blue")
plt.scatter(X[cyan, 0], X[cyan, 1], c="cyan")
plt.show()

if __name__=='__main__':
    cloud_points_read = np.array(read_csv("cloud_points.xyz"))

    plane = pyransac3d.Plane()
    best_eq, best_inliers = plane.fit(cloud_points_read, thresh = 0.01, minPoints=100, maxIteration=1000)

    print(f'best equation Ax+By+Cz+D:{best_eq}')
    print(f'best inliers:{best_inliers}')