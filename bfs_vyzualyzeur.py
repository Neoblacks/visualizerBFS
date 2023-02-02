from time import sleep
from colorama import Fore
import os
import re

def display_grid(grid, seen):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = Fore.WHITE if (x, y) not in seen else Fore.RED if grid[y][x] == "1" else Fore.BLUE if grid[y][x] == '0' else Fore.GREEN
            print(color + cell, end="")
        print()

grid = [list(line) for line in open("map.ber").read().strip().split("\n")]
lines = open("pos.txt").read().strip().split("\n")
seen = set()
for i, line in enumerate(lines):
    bx, by, bc = re.fullmatch(r"x: (\d+), y: (\d+), C: (.)", line).groups()
    bx, by = int(bx), int(by)
    seen.add((bx, by))
    if i%5==0 or i==len(lines)-1:
        os.system("clear")
        display_grid(grid, seen)
        sleep(0.03)
