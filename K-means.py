# Implementation of K-means clustering
# This code was developed to solve a specific homework so some variables are hardcoded, it can be generalized in
# the future
import math


def euclidean_distance(x, cs):
    total = 0
    result = []  # holds the distance between the records values and the centroid's values
    for i in range(len(x)):
        for j in range(len(x[i])):
            total += ((x[i][j] - cs[j]) ** 2)
        total = math.sqrt(total)
        result.append(total)
        total = 0
    return result


def cluster(x, y, z):
    cluster_list = []  # stores cluster value for each record in the data
    for i in range(len(x)):
        mini = min(x[i], y[i], z[i])
        if x[i] == mini:
            cluster_list.append(0)
        elif y[i] == mini:
            cluster_list.append(1)
        else:
            cluster_list.append(2)
    return cluster_list


def centroids_generator(data0, cl):
    global n_clusters
    res = []  # 2d list stores every cluster's elements in a separate list [[],[]...]
    centroid1 = [0, 0, 0]
    centroid2 = [0, 0, 0]
    centroid3 = [0, 0, 0]
    for i in range(n_clusters):  # finding the index values for each cluster number
        res.append([key for key, val in enumerate(cl)
                    if val == i])
    for i in range(len(res)):
        for j in range(len(res[i])):
            for k in range(len(data0[0])):
                vars()['centroid{}'.format(i + 1)][k] += data0[res[i][j]][k] / len(res[i])

    return centroid1, centroid2, centroid3, res


data2 = [[81218, 47, 3281],
         [74386, 5210, 7503],
         [60653, 5797, 819],
         [934, 107, 4],
         [906, 112, 14],
         [900, 133, 2],
         [64, 4, 1],
         [59, 9, 0],
         [57, 9, 1]
         ]
data = [[31096531, 61836, 564134],
        [12664058, 86704, 317936],
        [12148487, 53158, 162502],
        [4585385, 30702, 95337],
        [989492, 5008, 23107],
        [976598, 4880, 22926],
        [946647, 6204, 23409],
        [872936, 2179, 22921],
        [775, 0, 1],
        [712, 0, 13],
        [661, 0, 1]
        ]
n_clusters = 3
centroids = [[12664058, 86704, 317936], [976598, 4880, 22926], [775, 0, 1]]
iteration = 0
while 1:
    prevCentroids = centroids[0:3]
    distance_x = euclidean_distance(data, centroids[0])
    distance_y = euclidean_distance(data, centroids[1])
    distance_z = euclidean_distance(data, centroids[2])
    c = cluster(distance_x, distance_y, distance_z)
    centroids = centroids_generator(data, c)
    print("Distance from centroid 1:\n", distance_x)
    print("Distance from centroid 2:\n", distance_y)
    print("Distance from centroid 3:\n", distance_z)
    print("Elements in cluster1: ", centroids[3][0])
    print("Elements in cluster2: ", centroids[3][1])
    print("Elements in cluster3: ", centroids[3][2])
    print("The new centroids are: ", centroids[0:3])
    print('\n\n----------------------------------------------\n')
    if centroids[0:3] == prevCentroids:
        print("The new centroids have not changed, K-means has found the optimal solution after",
              iteration, "iteration(s)")
        exit(0)
    iteration += 1
