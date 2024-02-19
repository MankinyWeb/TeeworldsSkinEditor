from tkinter import *
from ttkbootstrap import *
from PIL import Image

import tkinter.filedialog

PARTS = {}

PARTS ["BODY"] = [1, 0, 5, 5]
PARTS ["BODYMASK"] = [7, 0, 11, 5]
PARTS ["HAND"] = [12, 0, 14, 2]
PARTS ["HANDMASK"] = [14, 0, 16, 2]
PARTS ["FEET"] = [12, 2, 16, 4]
PARTS ["FEETMASK"] = [12, 4, 16, 6]
PARTS ["EMO1"] = [4, 6, 6, 8]
PARTS ["EMO2"] = [6, 6, 8, 8]
PARTS ["EMO3"] = [8, 6, 10, 8]
PARTS ["EMO4"] = [10, 6, 12, 8]
PARTS ["EMO5"] = [12, 6, 14, 8]
PARTS ["EMO6"] = [14, 6, 16, 8]

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
    
teePath = ".\\测试Tee-Tsumugi.png"
tee = Image. open (".\\测试Tee-Tsumugi.png"). resize ((512, 256))

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
                DoOffest (PARTS ["FEET"], img. size)
            ),
            x - feetOffest1 [0], 
            y - feetOffest1 [1],
            1.5
        )
    )

    tees. append (showImage (img. crop (DoOffest (PARTS ["BODYMASK"], img. size)), x, y))
    tees. append (showImage (img. crop (DoOffest (PARTS ["BODY"], img. size)), x, y))

    feetOffest2 = [-32, -64]

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["FEET"], img. size)
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

chooses = ["BODY", "BODYMASK", "FEET", "FEETMASK", "EMO1", "EMO2", "EMO3", "EMO4", "EMO5", "EMO6", "HAND", "HANDMASK"]

nowChoose = ""
lastChoose = ""

choosePart = ttk. Combobox(
    master = root,
    values = chooses,
    textvariable = nowChoose
)

partImg = tee

def changePart (x):
    global partImg, lastChoose, nowChoose

    nowChoose = choosePart. get ()

    if (PARTS. get (lastChoose, -1) != -1):
        tee. paste (partImg, (int (DoOffest (PARTS [lastChoose], tee. size) [0]), int(DoOffest (PARTS [lastChoose], tee. size) [1])))

    partImg = tee. crop (DoOffest (PARTS [nowChoose], tee. size))  

    lastChoose = nowChoose

    showTee (tee, tee. size [0] / 2, tee. size [1] / 2)

    showPart (775, 230)

choosePart. bind ('<<ComboboxSelected>>', changePart)

choosePart. place (x = 337, y = 300)

def showPart (x, y):
    global partImg

    tees. append (showImage (partImg, x, y))

cav. place (x = 32, y = 32)

root. mainloop ()
