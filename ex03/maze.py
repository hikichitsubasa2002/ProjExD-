
import tkinter as tk
import maze_maker as mm
def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key=""

def main_proc(): #こうかとんの移動
    global cx, cy,my,mx
    delta = {"":[0,0],"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}
    
    # cx,cy = cx+delta[key][0], cy+delta[key][1]

    if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
        my,mx = my+delta[key][1],mx+delta[key][0]
    cx,cy = mx*100+50,my*100+50
    cabvas.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    cabvas = tk.Canvas(root,width=1500,height=900,bg="brown" )
    cabvas.pack()
    maze_bg = mm.make_maze(15,9)#
    mm.show_maze(cabvas,maze_bg)#
    mx,my = 1,1
    cx,cy = mx*150,my*150
    tori = tk.PhotoImage(file="fig/1.png")
    cabvas.create_image(cx,cy, image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()