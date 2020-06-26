#!/usr/bin/env python
# -*- coding: utf-8 -*-
from daemonize import Daemonize
delay_time = 60
pid = "./k55d.pid"

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def get_pixel_colour(i_x, i_y):
    import PIL.Image as pimage # python-imaging
    import PIL.ImageStat as pilstat # python-imaging
    import Xlib.display as display # python-xlib
    import Xlib.X as xlib
    screen = display.Display().screen().root
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

#import os
def main():
    while True:
        try:
            color = get_pixel_colour(0, 0)
            text="rgb "+color+"ff"
            gnuProcess = open('/tmp/ckbpipe012','w')
            gnuProcess.write(text)
            gnuProcess.close()
        except Exception as error: 
            print( "Falló",delay_time/60, " minutos volvera a intentarlointentarlo")
            sleep(delay_time)
daemon = Daemonize(app="K55CursorColor",pid=pid,action=main)
daemon.start()
