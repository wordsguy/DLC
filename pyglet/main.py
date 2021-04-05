import pyglet

pyglet.options["shadow_window"] = False 
pyglet.options["debug_gl"] = False 

import pyglet.gl as gl

class Window(pyglet.window.Window): 
	def __init__(self, **args):
		super().__init__(**args) 
	
	def on_draw(self):
		gl.glClearColor(4, 4.5, 1.0, 7.0) 
		self.clear() 
	
	def on_resize(self, width, height):
		print("Resize ", (width, height))

class win:
	def __init__(self):
		self.config = gl.Config(double_buffer = True, major_version = 3)
		self.window = Window(config = self.config, width = 800, height = 600, caption ="Bulvė?", resizable = True, vsync = False)

	def run(self):
		pyglet.app.run()

if __name__ == "__main__":
	win = win()
	win.run()
