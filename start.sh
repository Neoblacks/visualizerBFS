#!/bin/bash

# Start the first process

#Get repo on 1st arg

cd ~/Documents/slg/map_gen

./a.out

cd ../

./so_long map/map_gen.ber > ~/Documents/pythonBFS/pos.txt
cp map/map_gen.ber ~/Documents/pythonBFS/map.ber

cd ~/Documents/pythonBFS
python bfs_vyzualyzeur.py
