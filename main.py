# See https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html

import pyglet
import pyglet.window.key as key


# window shape
windowWidth = 600
windowHeight = 720

moveDistance = 20

window = pyglet.window.Window(windowHeight, windowWidth)

circle = pyglet.shapes.Circle(x = 100, y = 100, radius= 100, color=(255, 134, 20))
rectangle = pyglet.shapes.Rectangle(x=400, y=400, width=100, height=50)
rectangle.anchor_x = 50
rectangle.anchor_y = 25


# The rectangle is then rotated around its anchor point:
rectangle.rotation = 45

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed - {}'.format(chr(symbol)))
    if symbol == key.RIGHT:
        circle.x += moveDistance
    elif symbol == key.LEFT:
        circle.x -= moveDistance
    elif symbol == key.UP:
        circle.y += moveDistance
    elif symbol == key.DOWN:
        circle.y -= moveDistance


@window.event
def on_draw():
    window.clear()
    circle.draw()

pyglet.app.run()