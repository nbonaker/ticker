import numpy as np
import shutil
import os

base_keys = np.array(list('abcdefghijklmnopqrstuvwxyz.,?_$#'))
num_words = 17
words = np.array(np.arange(num_words))
grid = np.append(base_keys, words)

num_keys = grid.size
closest_sq = int(np.round(np.sqrt(num_keys)-0.51, 0))+1
grid.resize(closest_sq**2)
grid = grid.reshape(closest_sq, closest_sq)

num_cols = closest_sq
row_scan = ''
for key in grid[0]:
    row_scan += key
    if key != grid[0][-1]:
        row_scan += '-'

col_scans = []
for i in range(num_cols):
    col_scan = ''
    for key in grid.T[i]:
        col_scan += key
        if key != grid.T[i][-1]:
            col_scan += '-'
    if col_scan[-1] == '-':
        col_scan = col_scan[:-1]
    col_scans += [col_scan]

print grid
print row_scan
print col_scans

path = "grid_config/config/row_scan"
shutil.rmtree(path)

os.mkdir(path)
path += "/channels1"
os.mkdir(path)

stereo_file = open(path+"/stereo_pos.txt", 'w')
stereo_file.write("0")
stereo_file.close()

alpha_file = open(path+"/alphabet.txt", 'w')
alpha_file.write(row_scan)
alpha_file.close()

for col_num in range(1,num_cols+1):

    path = "grid_config/config/col_scan_" + str(col_num)
    shutil.rmtree(path)

    os.mkdir(path)
    path += "/channels1"
    os.mkdir(path)

    stereo_file = open(path+"/stereo_pos.txt", 'w')
    stereo_file.write("0")
    stereo_file.close()

    alpha_file = open(path+"/alphabet.txt", 'w')
    alpha_file.write(col_scans[col_num-1])
    alpha_file.close()

