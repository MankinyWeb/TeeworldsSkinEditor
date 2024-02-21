from tkinter import *
from ttkbootstrap import *
from PIL import Image

import tkinter.filedialog

PARTS = {}

PARTS ["BODY"] = [0, 0, 6, 6]
PARTS ["BODYMASK"] = [6, 0, 12, 6]
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

SHOWPOS = {}

SHOWPOS ["BODY"] = [1, 0, 64]
SHOWPOS ["BODYMASK"] = [1, 0, 64]
SHOWPOS ["FEET"] = [1.5, 32, 64]
SHOWPOS ["FEET2"] = [1.5, -32, 64]
SHOWPOS ["FEETMASK"] = [1.5, 32, 64]
SHOWPOS ["FEETMASK2"] = [1.5, -32, 64]
SHOWPOS ["EMO"] = [1.1, -16, 8, -24]

nowemo = "EMO1"

root = Window(
        title = 'Teeworlds Editor Skin',      
        themename = "solar",    
        size = (1920, 1080),      
        position = (0, 0),   
        minsize = (0, 0),     
        maxsize = (1920, 1080),    
        resizable = None,         
        alpha = 1.0,            
)

show = Canvas ()
cav = Canvas (root, width = 512, height = 1080)
show = Canvas (root, width = 1024, height = 512)
show. configure (bg = "#163637")

def FileOpen():
    return tkinter. filedialog. askopenfilename (
        title = 'Teeworlds Editor Skin',
        filetypes = [('All files', '*')]
    )

def round_rectangle(cv, x1, y1, x2, y2, radius = 25, **kwargs):
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

    return cv. create_polygon (points, **kwargs, smooth = True)

teePath = ".\\测试Tee-Tsumugi.png"
tee = Image. open (".\\测试Tee-Tsumugi.png"). resize ((512, 256))

partImg = tee

def showImage (img, x, y, scale = 1, c = cav, alpha = 1):
    newimg = img. resize ((int (img. size [0] * scale), int (img. size [1] * scale)))

    img = img.convert('RGBA')

    w, h = newimg. size
    
    for i in range(w):
        for k in range(h):
            color = newimg.getpixel((i, k))

            r, g, b, a = color

            if (a == 0):
                continue

            color = (r, g, b, int (alpha * 255))
            newimg. putpixel((i, k), color)
    
    photo = ImageTk. PhotoImage (newimg)

    c. create_image (x, y, image = photo)

    return photo

def DoOffest (i, size):
    return (
        i [0] * size [0] / 16,  
        i [1] * size [1] / 8, 
        i [2] * size [0] / 16, 
        i [3] * size [1] / 8, 
    )

tees = []

def showTee (img, x, y, alpha = 1, c = cav, scale = 1, nowchoose = "", emo = 1):
    global tees

    if ("EMO" in nowchoose):
        nowchoose = "EMO"

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["FEETMASK"], img. size)
            ),
            x + SHOWPOS ["FEETMASK2"] [1] * scale, 
            y + SHOWPOS ["FEETMASK2"] [2] * scale,
            SHOWPOS ["FEETMASK2"] [0] * scale,
            alpha = 1 if nowchoose == "FEETMASK" else alpha,
            c = c
        )
    )

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["FEET"], img. size)
            ),
            x + SHOWPOS ["FEET2"] [1] * scale, 
            y + SHOWPOS ["FEET2"] [2] * scale,
            SHOWPOS ["FEET2"] [0] * scale,
            alpha = 1 if nowchoose == "FEET" else alpha,
            c = c
        )
    )

    tees. append (showImage (img. crop (DoOffest (PARTS ["BODYMASK"], img. size)), x, y + 16, alpha = 1 if nowchoose == "BODYMASK" else alpha, c = c, scale = scale))
    tees. append (showImage (img. crop (DoOffest (PARTS ["BODY"], img. size)), x, y + 16, alpha = 1 if nowchoose == "BODY" else alpha, c = c, scale = scale))

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["FEETMASK"], img. size)
            ),
            x + SHOWPOS ["FEETMASK"] [1] * scale, 
            y + SHOWPOS ["FEETMASK"] [2] * scale,
            SHOWPOS ["FEETMASK"] [0] * scale,
            alpha = 1 if nowchoose == "FEETMASK" else alpha,
            c = c
        )
    )

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["FEET"], img. size)
            ),
            x + SHOWPOS ["FEET"] [1] * scale, 
            y + SHOWPOS ["FEET"] [2] * scale,
            SHOWPOS ["FEET"] [0] * scale,
            alpha = 1 if nowchoose == "FEET" else alpha,
            c = c
        )
    )

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["EMO" + str (emo)], img. size)
            ). transpose (Image.FLIP_LEFT_RIGHT),
            x + SHOWPOS ["EMO"] [1] * scale, 
            y + SHOWPOS ["EMO"] [2] * scale,
            SHOWPOS ["EMO"] [0] * scale,
            alpha = 1 if nowchoose == "EMO" else alpha,
            c = c
        )
    )

    tees. append (
        showImage (
            img. crop (
                DoOffest (PARTS ["EMO" + str (emo)], img. size)
            ),
            x + (SHOWPOS ["EMO"] [1] + SHOWPOS ["EMO"] [3]) * scale, 
            y + (SHOWPOS ["EMO"] [2]) * scale,
            SHOWPOS ["EMO"] [0] * scale,
            alpha = 1 if nowchoose == "EMO" else alpha,
            c = c
        )
    )

def open_tee ():
    global teePath, tee, partImg, nowChoose, lastChoose

    teePath = FileOpen ()

    print ("Open file = ", teePath)

    tee = Image. open (teePath). resize ((512, 256))

    partImg = tee

    nowChoose = -1
    lastChoose = -1
    
    showTee (tee, tee. size [0] / 2, tee. size [1] / 2)

round_rectangle (cav, 16, 16, 512, 256, 25, fill = "#163637", outline = "#163637", width = 2)

menu = Menu (root)

menu. add_command (label = "读取", command = open_tee)

menu. config (background = "#163637")

root. config (menu = menu)

chooses = ["BODY", "BODYMASK", "FEET", "FEETMASK", "EMO1", "EMO2", "EMO3", "EMO4", "EMO5", "EMO6", "HAND", "HANDMASK"]

nowChoose = ""
lastChoose = ""

choosePart = Combobox (
    master = cav,
    values = chooses,
    textvariable = nowChoose
)

emos = ["EMO1", "EMO2", "EMO3", "EMO4", "EMO5", "EMO6"]

chooseEMO = Combobox (
    master = root,
    values = emos,
    textvariable = nowemo
)

def changePart (x = 0):
    global partImg, lastChoose, nowChoose, tees , nowemo

    tees. clear ()

    nowChoose = choosePart. get ()
    nowemo = chooseEMO. get ()

    if ("EMO" in nowChoose):
        nowemo = nowChoose
        chooseEMO. set (nowemo)

    if (PARTS. get (lastChoose, -1) != -1):
        tee. paste (partImg, (int (DoOffest (PARTS [lastChoose], tee. size) [0]), int(DoOffest (PARTS [lastChoose], tee. size) [1])))

    partImg = tee. crop (DoOffest (PARTS [nowChoose], tee. size))  

    lastChoose = nowChoose

    showTee (tee, tee. size [0] / 2, tee. size [1] / 2)

    showPart (512, 200)


choosePart. bind ('<<ComboboxSelected>>', changePart)

choosePart. place (x = 16, y = 300)

chooseEMO. bind ('<<ComboboxSelected>>', changePart)

chooseEMO. place (x = 48 + 230, y = 300 + 32)

s = 2
apf = 0.5
    
def showPart (x, y):
    global partImg

    s = '%.2f'% scl. get ()
    apf = '%.2f'% afs. get ()

    scltext ["text"] = "展示大小 {1.00 ~ 2.00} " + str (s)
    afstext ["text"] = "其他部分透明度 {0.00 ~ 1.00} " + str (apf)

    s = float (s)
    apf = float (apf)

    showTee (tee, x, y, alpha = apf, c = show, scale = s, nowchoose = nowChoose, emo = int (nowemo [3]))

    x += SHOWPOS [nowChoose] [1] * s
    y += SHOWPOS [nowChoose] [2] * s

    showTee (tee, tee. size [0] / 2, tee. size [1] / 2, nowchoose = nowChoose, emo = int (nowemo [3]))

cav. place (x = 32, y = 32)

show. place (x = 600, y = 48)

scl = Scale (root, orient = HORIZONTAL,
                length = 200,
                from_ = 1.0, to = 2.0,
                variable = s,
                command = changePart
)

scl. set (1)

scl. place (x = 600, y = 48 + 512 + 16 + 48)
scltext = Label (text = "展示大小 {1.00 ~ 2.00} 1.00", font = ("Fira Code", 16))
scltext. place (x = 832, y = 48 + 512 + 8 + 48)

afs = Scale (root, orient = HORIZONTAL,
                length = 200,
                from_ = 0.0, to = 1.0,
                variable = apf,
                command = changePart
)

afs. set (0.5)

afs.place (x = 600, y = 48 + 512 + 16 + 100)
afstext = Label (text = "其他部分透明度 {0.00 ~ 1.00} 0.50", font = ("Fira Code", 16))
afstext. place (x = 832, y = 48 + 512 + 8 + 100)

root. mainloop ()
