from tkinter import *
from ttkbootstrap import *
from PIL import Image

import tkinter.filedialog

BODY = [1, 0, 5, 5]
BODYMASK = [7, 0, 11, 5]
HAND = [12, 0, 14, 2]
HANDMASK = [14, 0, 16, 2]
FEET = [12, 2, 16, 4]
FEETMASK = [12, 4, 16, 6]
EMOS = [4, 6, 16, 8]

def draw_rounded_rectangle (canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2 - radius,
        x1, y1 + radius
    ]
    canvas. create_polygon (points, smooth = True, **kwargs)

root = Window(
        title = 'Teeworlds Editor Skin',      
        themename = "solar",    
        size = (1066, 600),      
        position = (100, 100),   
        minsize = (0, 0),     
        maxsize = (1920, 1080),    
        resizable = None,         
        alpha = 1.0,            
)

cav = Canvas (root, width = 2000, height = 1000)

def FileOpen():
    return tkinter. filedialog. askopenfilename (
        title = 'Teeworlds Editor Skin',
        filetypes = [('All files', '*')]
    )
    
teePath = ".\\测试Tee-Manga.png"
tee = Image. open (".\\测试Tee-Manga.png"). resize ((256, 128))

def showImage (img, x, y, scale = 1):
    photo = ImageTk. PhotoImage (img. resize ((int (img. size [0] * scale), int (img. size [1] * scale))))
    cav. create_image (x, y, image = photo)

    return photo

def DoOffest (i, size):
    return (
        i [0] * size [0] / 16,  
        i [1] * size [1] / 8, 
        i [2] * size [0] / 16, 
        i [3] * size [1] / 8, 
    )

tees = []

def showTee (img, x, y):
    global tees

    tees. clear ()

    feetOffest1 = [32, -64]

    tees. append (
        showImage (
            img. crop (
                DoOffest (FEET, img. size)
            ),
            x - feetOffest1 [0], 
            y - feetOffest1 [1],
            1.5
        )
    )

    tees. append (showImage (img. crop (DoOffest (BODYMASK, img. size)), x, y))
    tees. append (showImage (img. crop (DoOffest (BODY, img. size)), x, y))

    feetOffest2 = [-32, -64]

    tees. append (
        showImage (
            img. crop (
                DoOffest (FEET, img. size)
            ),
            x - feetOffest2 [0], 
            y - feetOffest2 [1],
            1.5
        )
    )

def open_tee ():
    global teePath, tee

    teePath = FileOpen ()

    print ("Open file = ", teePath)

    tee = Image. open (teePath). resize ((512, 256))
    
    showTee (tee, tee. size [0] / 2, tee. size [1] / 2)

def round_rectangle(x1, y1, x2, y2, radius = 25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return cav. create_polygon (points, **kwargs, smooth = True)

round_rectangle (16, 16, 512, 256, 25, fill = "#163637", outline = "#163637", width = 2)

round_rectangle (600, 16, 950, 500, 25, fill = "#163637", outline = "#163637", width = 2)

Button (root, text = "读取皮肤文件", command = open_tee). place (x = 0, y = 0)

cav. place (x = 32, y = 32)

root. mainloop ()
