from pyglet import gl
"""
hack for retina displays because pyglet fails
see https://github.com/los-cocos/cocos/issues/303
and https://bitbucket.org/pyglet/pyglet/issues/45/retina-display-scaling-on-os-x
"""


def native_width(window):
    view = window.context._nscontext.view()
    bounds = view.convertRectToBacking_(view.bounds()).size
    return int(bounds.width), int(bounds.height)


def set_projection3D(self):
    """Sets a 3D projection mantaining the aspect ratio of the original window size"""
    # virtual (desired) view size
    vw, vh = self.get_window_size()

    nw, nh = native_width(self.window)
    gl.glViewport(self._offset_x, self._offset_y, nw, nh)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.gluPerspective(60, nw / float(nh), 0.1, 3000.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

    gl.glLoadIdentity()
    gl.gluLookAt(vw / 2.0, vh / 2.0, vh / 1.1566,   # eye
              vw / 2.0, vh / 2.0, 0,             # center
              0.0, 1.0, 0.0                      # up vector
              )


def set_projection2D(self):
    """Sets a 2D projection (ortho) covering all the window"""
    # called only for the side effect of setting matrices in pyglet
    nw, nh = native_width(self.window)
    self.window.on_resize(nw , nw)


def exec():
    from cocos.director import director, Director

    Director.set_projection2D = set_projection2D
    Director.set_projection3D = set_projection3D