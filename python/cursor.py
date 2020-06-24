def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def get_pixel_colour(i_x, i_y):
    import PIL.Image as pimage # python-imaging
    import PIL.ImageStat as pilstat # python-imaging
    import Xlib.display as display # python-xlib
    import Xlib.X as xlib
    screen = display.Display().screen().root
#    o_x_root = Xlib.display.Display().create_resource_object('window',0x277075e).get_wm_class()
#    print(o_x_root)
    cursor = screen.query_pointer()._data
    x = cursor["root_x"]
    y = cursor["root_y"]
    image = screen.get_image(x, y, 1, 1, xlib.ZPixmap, 0xffffffff)
    image_rgb = pimage.frombytes("RGB", (1, 1), image.data, "raw", "BGRX")
    lf_colour = pilstat.Stat(image_rgb).mean
    r= int(lf_colour[0])
    g= int(lf_colour[1])
    b= int(lf_colour[2])
    return rgb2hex(r,g,b)

import subprocess
import sys
#gnuProcess = subprocess.Popen('/tmp/ckbpipe012', stdin=subprocess.PIPE)
color = get_pixel_colour(0, 0)
text="rgb 1:"+color+"ff"
print(text)
 #   gnuProcess.stdin.write(text)
 #   gnuProcess.stdin.flush()
