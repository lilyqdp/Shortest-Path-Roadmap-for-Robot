import sys
import numpy as np
import math
from collections import defaultdict
'''
Report reflexive vertices
'''



def findReflexiveVertices(polygons):
    vertices=[]
    
    # Your code goes here 
    for poly in polygons:
        n = len(poly)
        for i in range(n):
            x_prev, y_prev = poly[(i-1)%n]
            x, y = poly[i]
            x_next, y_next = poly[(i + 1) % n]
    # vertices = [[x1,y1],[x2,y2],...]
            v1x, v1y = x_next - x, y_next - y 
            v2x, v2y = x_prev - x, y_prev - y 

    # You should return a list of (x,y) values as lists, i.e.
            cross = v1x*v2y-v1y*v2x
    
            if cross > 0:
                vertices.append([x,y])
    return vertices

'''
Compute the roadmap graph
'''
def computeSPRoadmap(polygons, reflexVertices):
    vertexMap = dict()
    adjacencyListMap = defaultdict(list)
    
    # Your code goes here
    # You should check for each pair of vertices whether the
    # edge between them should belong to the shortest path
    # roadmap. 
    for index in range(len(reflexVertices)):
        vertexMap[index+1]= reflexVertices[index]

    def can_see_eachother(p1, p2):
        for poly in polygons:
            n = len(poly)
            for i in range(n):
                edge_start = poly[i]
                edge_end = poly[(i+1)%n]

                if p1 in (edge_start, edge_end) or p2 in (edge_start, edge_end):
                    continue
                if lines_intersect(p1, p2, edge_start, edge_end):
                    return False
        return True
    
    def lines_intersect(A,B,C,D):
        def ccw(X,Y,Z): #counter-clock-wise
            return (Z[1] - X[1]) * (Y[0] - X[0]) > (Y[1] - X[1]) * (Z[0] - X[0])
        return ccw(A,B,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    
    def dist(p1,p2):
        return math.hypot(p1[0]- p2[0], p1[1]- p2[1])

    # Your vertexMap should look like
    # {1: [5.2,6.7], 2: [9.2,2.3], ... }
    #
    # and your adjacencyListMap should look like
    # {1: [[2, 5.95], [3, 4.72]], 2: [[1, 5.95], [5,3.52]], ... }
    #
    # The vertex labels used here should start from 1
    
    for i in range(1, len(vertexMap)+1):
        for j in range(1, len(vertexMap)+1):
            if i ==j:
                continue
            point_a = vertexMap[i]
            point_b = vertexMap[j]

            if can_see_eachother(point_a, point_b):
                distance = dist(point_a, point_b)
                adjacencyListMap[i].append([j, distance])
    return vertexMap, adjacencyListMap

'''
Perform uniform cost search 
'''
def uniformCostSearch(adjListMap, start, goal):
    path = []
    pathLength = 0
    
    # Your code goes here. As the result, the function should
    # return a list of vertex labels, e.g.
    #
    # path = [23, 15, 9, ..., 37]
    #
    # in which 23 would be the label for the start and 37 the
    # label for the goal.
    
    return path, pathLength

'''
Agument roadmap to include start and goal
'''
def updateRoadmap(polygons, vertexMap, adjListMap, x1, y1, x2, y2):
    updatedALMap = dict()
    startLabel = 0
    goalLabel = -1

    # Your code goes here. Note that for convenience, we 
    # let start and goal have vertex labels 0 and -1,
    # respectively. Make sure you use these as your labels
    # for the start and goal vertices in the shortest path
    # roadmap. Note that what you do here is similar to
    # when you construct the roadmap. 
    
    return startLabel, goalLabel, updatedALMap

if __name__ == "__main__":
    
    # Retrive file name for input data
    if(len(sys.argv) < 6):
        print("Five arguments required: python spr.py [env-file] [x1] [y1] [x2] [y2]")
        exit()
    
    filename = sys.argv[1]
    x1 = float(sys.argv[2])
    y1 = float(sys.argv[3])
    x2 = float(sys.argv[4])
    y2 = float(sys.argv[5])

    # Read data and parse polygons
    lines = [line.rstrip('\n') for line in open(filename)]
    polygons = []
    for line in range(0, len(lines)):
        xys = lines[line].split(';')
        polygon = []
        for p in range(0, len(xys)):
            polygon.append(list(map(float, xys[p].split(','))))
        polygons.append(polygon)

    # Print out the data
    print ("Pologonal obstacles:")
    for p in range(0, len(polygons)):
        print (str(polygons[p]))
    print ("")

    # Compute reflex vertices
    reflexVertices = findReflexiveVertices(polygons)
    print ("Reflexive vertices:")
    print (str(reflexVertices))
    print ("")

    # Compute the roadmap 
    vertexMap, adjListMap = computeSPRoadmap(polygons, reflexVertices)
    print ("Vertex map:")
    print (str(vertexMap))
    print ("")
    print ("Base roadmap:")
    print (str(adjListMap))
    print ("")

    # Update roadmap
    start, goal, updatedALMap = updateRoadmap(polygons, vertexMap, adjListMap, x1, y1, x2, y2)
    print ("Updated roadmap:")
    print (str(updatedALMap))
    print ("")

    # Search for a solution     
    path, length = uniformCostSearch(updatedALMap, start, goal)
    print ("Final path:")
    print (str(path))
    print ("Final path length:" + str(length))
    

    # Extra visualization elements goes here
