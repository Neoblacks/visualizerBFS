#CONTENT: 1.0

# import tkinter as tk
# from time import sleep
# import re

# def display_grid(canvas, grid, seen):
#     canvas.delete("all") # On efface tout ce qui est dessiné sur le canvas
#     for y, row in enumerate(grid):
#         for x, cell in enumerate(row):
#             if (x, y) not in seen:
#                 color = "black"
#             elif grid[y][x] == "1":
#                 color = "red"
#             elif grid[y][x] == '0':
#                 color = "blue"
#             else:
#                 color = "green"
#             canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill=color)
#             canvas.create_text(x*40+20, y*40+20, text=cell, font="Arial 20 bold", fill="white" if color=="black" else "black")

# root = tk.Tk()
# grid = [list(line) for line in open("map.ber").read().strip().split("\n")]
# lines = open("pos.txt").read().strip().split("\n")
# seen = set()
# canvas = tk.Canvas(root, width=len(grid[0])*40, height=len(grid)*40)
# canvas.pack()
# for i, line in enumerate(lines):
#     bx, by, bc = re.match(r"x: (\d+), y: (\d+), C: (.)", line).groups()
#     bx, by = int(bx), int(by)
#     seen.add((bx, by))
#     if i%5==0 or i==len(lines)-1:
#         display_grid(canvas, grid, seen)
#         root.update()
#         sleep(0.03)


# root.mainloop()


import tkinter as tk
from time import sleep
import re

def close_window():
    # destroy label and canvas
    label.destroy()
    canvas.destroy()

    root.destroy()

def display_grid(canvas, grid, seen):
    canvas.delete("all")
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) not in seen:
                color = "black"
            elif seen[(x, y)] % 2 == 0:
                color = 'black'
            elif grid[y][x] == "1":
                color = "indianred"
            elif grid[y][x] == '0':
                color = "royalblue"
            elif grid[y][x] == 'C':
                color = "goldenrod"
            else:
                color = "forestgreen"
            canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill=color)
            canvas.create_text(x*40+20, y*40+20, text=cell, font="Arial 20 bold", fill= "white" if color=="black" else "black")
root = tk.Tk()
root.title("BFS Visualizer")
grid = [list(line) for line in open("map.ber").read().strip().split("\n")]
lines = open("pos.txt").read().strip().split("\n")
seen = {}
canvas = tk.Canvas(root, width=len(grid[0])*40, height=len(grid)*40 + 100)
canvas.pack()
label = tk.Label(root, text = "Number of steps: ", font = "Arial 20 bold", fg = "black", bg = "lightgrey")
label_collec = tk.Label(root, text = "Number of Collect found: ", font = "Arial 20 bold", fg = "black", bg = "lightgrey")
label.place(x = 0, y = len(grid)*40 + 5)
label_collec.place(x = 300, y = len(grid)*40 + 5)
for i, line in enumerate(lines):
    label.config(text = "Number of steps: " + str(i), font = "Arial 20 bold", fg = "black", bg = "lightgrey")
    # display number of collectibles found and increment it when C is found
    # label_collec.config(text = "Number of Collectibles found: " + str(line.count('C')), font = "Arial 20 bold", fg = "black", bg = "lightgrey")
    label.update()
    bx, by, bc = re.match(r"x: (\d+), y: (\d+), C: (.)", line).groups()
    bx, by = int(bx), int(by)
    if (bx, by) in seen:
        seen[(bx, by)] += 1
    else:
        seen[(bx, by)] = 1
    if i%5==0 or i==len(lines)-1:
        # sleep(0.03)
        root.update()
        display_grid(canvas, grid, seen)
# display_grid(canvas, grid, seen)

root.bind('<Escape>', lambda e: close_window())
root.mainloop()