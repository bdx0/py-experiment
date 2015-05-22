'''
Created on May 22, 2015

@author: CPU10157-local
'''
import pyglet


window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')
context = window.context
config = context.config

@window.event
def on_draw():
    window.clear()
    label.draw() 

pyglet.app.run()
