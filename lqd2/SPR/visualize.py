import sys

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

''' 
Set up matplotlib to create a plot with an empty square
'''
def setupPlot():
    fig = plt.figure(num=None, figsize=(5, 5), dpi=120, facecolor='w', edgecolor='k')
    plt.autoscale(False)
    plt.axis('off')
    ax = fig.add_subplot(1,1,1)
    ax.set_axis_off()
    ax.add_patch(patches.Rectangle(
        (0,0),   # (x,y)
        1,          # width
        1,          # height
        fill=False
        ))
    return fig, ax

'''
Make a patch for a single pology 
'''
def createPolygonPatch(polygon):
    verts = []
    codes= []
    for v in range(0, len(polygon)):
        xy = polygon[v]
        verts.append((xy[0]/10., xy[1]/10.))
        if v == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)
    verts.append(verts[0])
    codes.append(Path.CLOSEPOLY)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='gray', lw=1)

    return patch
    
'''
Make a patch for the robot
'''
def createPolygonPatchForRobot(polygon):
    verts = []
    codes= []
    for v in range(0, len(polygon)):
        xy = polygon[v]
        verts.append((xy[0]/10., xy[1]/10.))
        if v == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)
    verts.append(verts[0])
    codes.append(Path.CLOSEPOLY)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='gray', lw=1)

    return patch
    

'''
Render polygon obstacles  
'''
def drawPolygons(polygons):
    fig, ax = setupPlot()
    for p in range(0, len(polygons)):
        patch = createPolygonPatch(polygons[p])
        ax.add_patch(patch)    
    plt.show()

def drawRoadmap(ax, vertexMap, adjListMap):
    for v, edges in adjListMap.items():
        for nbr, _ in edges:
            if v in vertexMap and nbr in vertexMap:
                x1, y1 = vertexMap[v][0] / 10.0, vertexMap[v][1] / 10.0
                x2, y2 = vertexMap[nbr][0] / 10.0, vertexMap[nbr][1] / 10.0
                ax.plot([x1, x2], [y1, y2], color='green', linewidth=1)

def drawFinalPath(ax, path, vertexMap, startPt, goalPt):
    points = []
    for node in path:
        if node == 0: 
            points.append(startPt)
        elif node == -1: 
            points.append(goalPt)
        else:
            points.append(vertexMap[node])

    xs = [p[0] / 10.0 for p in points]
    ys = [p[1] / 10.0 for p in points]

    ax.plot(xs, ys, color='red', linewidth=2)
    
def visualizeAll(polygons, vertexMap, adjListMap, path, startPt, goalPt):
    fig, ax = setupPlot()

    # Draw obstacles
    for poly in polygons:
        patch = createPolygonPatch(poly)
        ax.add_patch(patch)

    # Draw roadmap (green)
    drawRoadmap(ax, vertexMap, adjListMap)

    # Draw shortest path (red)
    drawFinalPath(ax, path, vertexMap, startPt, goalPt)

    # Draw start + goal
    ax.scatter(startPt[0]/10.0, startPt[1]/10.0, color='blue', s=40)
    ax.scatter(goalPt[0]/10.0, goalPt[1]/10.0, color='orange', s=40)

    plt.show()


if __name__ == "__main__":
    
    # Retrive file name for input data
    if(len(sys.argv) < 2):
        print("Please provide input file: python visualize.py [env-file]")
        exit()
    
    filename = sys.argv[1]

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
    for p in range(0, len(polygons)):
        print(str(polygons[p]))

    # Draw the polygons
    drawPolygons(polygons)

    
