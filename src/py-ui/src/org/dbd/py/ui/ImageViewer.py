'''
Created on May 22, 2015

@author: CPU10157-local
'''
'''
http://images.wookmark.com/253022_bad_girl_by_lestat96.jpg
'''

from cStringIO import StringIO
import urllib

from pyglet.gl import *


def get_image():
    print 'get image'
    return StringIO(urllib.urlopen('http://images.all-free-download.com/images/graphiclarge/sexy_beautiful_hd_pictures_168156.jpg').read())

# imageobj = get_image()
# image = pyglet.image.load('', file=imageobj)
window = pyglet.window.Window()

vertices = [
    0, 0,
    window.width, 0,
    window.width, window.height]
vertices_gl = (GLfloat * len(vertices))(*vertices)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(2, GL_FLOAT, 0, vertices_gl)


@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(gl.GL_MODELVIEW)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 2)


pyglet.app.run()
