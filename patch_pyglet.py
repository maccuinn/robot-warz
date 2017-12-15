from pyglet.window import Window
from pyglet import gl

def on_resize(self, width, height):
    '''
    Patch the on_resize to handle retina displays on mac.
    see https://github.com/los-cocos/cocos/issues/303
    and https://bitbucket.org/pyglet/pyglet/issues/45/retina-display-scaling-on-os-x
    '''
    view = self.context._nscontext.view()
    bounds = view.convertRectToBacking_(view.bounds()).size
    back_width, back_height = (int(bounds.width), int(bounds.height))

    gl.glViewport(0, 0, back_width, back_height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(0, width, 0, height, -1, 1)

Window.on_resize = on_resize