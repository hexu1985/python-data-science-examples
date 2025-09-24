
from vectors import *
from draw2d import *

octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

def vertices(faces):
    return list(set([vertex for face in faces for vertex in face]))

def component(v,direction):
    return (dot(v,direction) / length(direction))

def vector_to_2d(v):
    return (component(v,(1,0,0)), component(v,(0,1,0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

blues = matplotlib.colormaps.get_cmap('Blues')

def unit(v):
    return scale(1./length(v), v)

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

def render(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        unit_normal = unit(normal(face)) #1
        if unit_normal[2] > 0: #2
            c = color_map(1 - dot(unit(normal(face)), unit(light))) #3
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines) #4
            polygons.append(p)
    draw2d(*polygons,axes=False, origin=False, grid=None)

render(octahedron, color_map=matplotlib.cm.get_cmap('Blues'), lines=black)
