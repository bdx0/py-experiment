'''
Created on May 22, 2015

@author: CPU10157-local
'''
'''
http://steveasleep.com/pyglettutorial.html#intro
'''

from collections import namedtuple


Vec3 = namedtuple('Vec3', 'x y z')
Color = namedtuple('Color', 'r g b a')
 
class Shape(object):
 
    def __init__(self, vertices, faces, face_colors):
        # list of Vec3s
        self.vertices = vertices
 
        # list of faces, each face is a list of indices into 'vertices'
        self.faces = faces
 
        # List of colors, one per face
        self.face_colors = face_colors
