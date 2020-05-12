from typing import Iterable,Tuple,Sequence             #import Iterable Item
from math import fsum,sqrt                  #more accurate sum
from pprint import pprint               #preety print for easy visualization
from functools import partial
from collections import defaultdict
from random import sample


''' Algorithm in English
Pick arbituary point as guesses for the center of each group
Assign all the data points to the closest maching group
within each group, average the points to get to a new guess
for the center of the group
Repeat multiple times: assign data and average the points '''

#a cleaner way to assign datatype of tuple is by creating your own object
Point = Tuple[int, ...]
Centroid = Point


def mean(data: Iterable[float]):
    'Accurate arithmetic mean using fsum'
    data = list(data)
    return fsum(data)/len(data)

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip):
    return sqrt(sum([(x-y)**2 for x,y in zip(p,q)]))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]):
    'Assign each data point to closest centroid'
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist,point))
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]):
    'Compute the centroid of each group of points in a list'
    return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data: Iterable[Point], num_centroids:int=2, iterations:int=50):
    'Cluster data into random n centroids'
    data = list(data)
    centroids = sample(data,num_centroids)
    for i in range(iterations):
        labeled_dict = assign_data(centroids, data)
        centroids = compute_centroids(labeled_dict.values())
    return centroids

if __name__ == '__main__':
    'Testing current module'

    points = [
    (10,41,23),
    (22,30,29),
    (11,42,5),
    (20,32,4),
    (12,40,12),
    (21,36,23)
    ]

    centroids = k_means(points, num_centroids=2)
    dictionary = assign_data(centroids, points)
    pprint(dictionary)