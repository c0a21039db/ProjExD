import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(): #こうかとんの移動
    global cx, cy, mx, my, canvas, kiretori
    # cx, cy = mx*100 + 50, my*100 + 50 #こうかとんの初期位置
    # canvas.coords("kokaton", cx, cy)
    # root.after(100, main_proc) #移動速度
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    canvas.lower("kirekokaton") #壁にぶつかって怒るこうかとん(以下)
    canvas.lower("kire")
    if maze_lst[mx][my] == 1: #移動先が壁ならば
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
        # canvas = tk.Canvas(root, width=1500, height=900, bg="black"
        canvas.create_rectangle(cx-50, cy-50, cx+50, cy+50, fill = "white", tag = "kire")
        kiretori = tk.PhotoImage(file = "fig/7.png")
        canvas.create_image(cx, cy, image=kiretori, tag="kirekokaton")
        canvas.lift("kirekokaton")

    cx, cy = mx*100 + 50, my*100 + 50 #こうかとんの初期位置
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc) #移動速度


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 + 50 #こうかとんの初期位置
    tori = tk.PhotoImage(file = "fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag = "kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()


    root.mainloop()

