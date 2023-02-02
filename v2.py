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

def display_grid(canvas, grid, seen):
    canvas.delete("all")
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) not in seen:
                color = "black"
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
seen = set()
canvas = tk.Canvas(root, width=len(grid[0])*40, height=len(grid)*40)
canvas.pack()
for i, line in enumerate(lines):
    bx, by, bc = re.match(r"x: (\d+), y: (\d+), C: (.)", line).groups()
    bx, by = int(bx), int(by)
    seen.add((bx, by))
    if i%5==0 or i==len(lines)-1:
        display_grid(canvas, grid, seen)
        # sleep(0.03)
        root.update()


root.mainloop()

