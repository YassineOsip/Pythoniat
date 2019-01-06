import pyglet
window  = pyglet.window.Window()
label = pyglet.text.Label('Hello world ',font_name ='Arial', font_size=28,x =window.width//2 ,y = window.width //2, anchor_x="center" , anchor_y="center" )

@window.event()
def on_Draw():
    window.draw_mouse_cursor()
    label.draw()
pyglet.app.run()

