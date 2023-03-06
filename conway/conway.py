"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import date

ON = 255
OFF = 0
vals = [ON, OFF]

# Creates grid and fills it with zeros
def createGrid(N, M):
    return np.zeros((N, M))

# Grabs all neighbors from a cell into a list and counts all alive ones
def neighbors(grid, i, j, n, N, M):
    neigh = grid[max(0,i-n):min(i+n+1, N), max(0, j-n):min(j+n+1, M)].flatten()
    return np.count_nonzero(neigh == 255)

# Grabs all necesary cells that a certain lifeform could exist and checks if it does
def checkLifeform(grid, i, j, n, m, lifeform):
    neigh = grid[i:i+n+1, j:j+m+1].flatten()
    return np.array_equal(neigh, lifeform)

# updates the animation of Game of Life
def update(frameNum, img, grid, N, M, lifeforms, result):
    # Makes sure the animation does not run the frame 1 twice
    global aux
    if aux:
        aux = False
        return
    
    # counts of lifeforms
    blockCount = 0
    beehiveCount = 0
    loafCount = 0
    boatCount = 0
    tubCount = 0
    blinkerCount = 0
    toadCount = 0
    beaconCount = 0
    gliderCount = 0
    LWSCount = 0
    
    # copy grid to make a new frame
    newGrid = grid.copy()
    # copy grid and add zeros around the grid to check all corners correctly
    auxGrid = grid.copy()
    auxGrid = np.pad(auxGrid, 1, mode="constant")
    for i in range(0, N):
        for j in range(0, M):
            aliveNeigh = neighbors(grid, i, j, 1, N, M)
            
            # rules of game
            if grid[i, j] == 255:
                aliveNeigh -= 1
                if not aliveNeigh == 2 and not aliveNeigh == 3:
                    newGrid[i, j] = 0
            else:
                if aliveNeigh == 3:
                    newGrid[i, j] = 255      
           
            # check for any lifeform living 
            if checkLifeform(auxGrid, i-1, j-1, 3, 3, lifeforms["block"]):
                blockCount += 1  
            elif checkLifeform(auxGrid, i-1, j-1, 4, 5, lifeforms["beehive"]):
                beehiveCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 5, lifeforms["loaf"]):
                loafCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["boat"]):
                boatCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["tub"]):
                tubCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 2, lifeforms["blinker1"]):
                blinkerCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 2, 4, lifeforms["blinker2"]):
                blinkerCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 5, lifeforms["toad1"]):
                toadCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 3, 5, lifeforms["toad2"]):
                toadCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 5, lifeforms["beacon1"]):
                beaconCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 5, lifeforms["beacon2"]):
                beaconCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["glider1"]):
                gliderCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["glider2"]):
                gliderCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["glider3"]):
                gliderCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 4, 4, lifeforms["glider4"]):
                gliderCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 6, lifeforms["LWS1"]):
                LWSCount += 1          
            elif checkLifeform(auxGrid, i-1, j-1, 5, 6, lifeforms["LWS2"]):
                LWSCount += 1        
            elif checkLifeform(auxGrid, i-1, j-1, 5, 6, lifeforms["LWS3"]):
                LWSCount += 1     
            elif checkLifeform(auxGrid, i-1, j-1, 5, 6, lifeforms["LWS4"]):
                LWSCount += 1     
    
    # write each iteration in output.txt 
    countLifeforms = sum([blockCount, beehiveCount, loafCount, boatCount, tubCount, blinkerCount, toadCount, beaconCount, gliderCount, LWSCount])
    aux2 = False
    if countLifeforms == 0:
        aux2 = True
        countLifeforms = 1
    f = open(result, "a")
    f.write("============= ITERATION {} =============\n".format(frameNum+1))
    f.write("   Lifeform   |   Count   |   Percent   \n")
    f.write("   block      |     {}     |     {}   \n".format(blockCount, int(blockCount / countLifeforms * 100)))
    f.write("   beehives   |     {}     |     {}   \n".format(beehiveCount, int(beehiveCount / countLifeforms * 100)))
    f.write("   loafs      |     {}     |     {}   \n".format(loafCount, int(loafCount / countLifeforms * 100)))
    f.write("   boats      |     {}     |     {}   \n".format(boatCount, int(boatCount / countLifeforms * 100)))
    f.write("   tubs       |     {}     |     {}   \n".format(tubCount, int(tubCount / countLifeforms * 100)))
    f.write("   blinkers   |     {}     |     {}   \n".format(blinkerCount, int(blinkerCount / countLifeforms * 100)))
    f.write("   toads      |     {}     |     {}   \n".format(toadCount, int(toadCount / countLifeforms * 100)))
    f.write("   beacons    |     {}     |     {}   \n".format(beaconCount, int(beaconCount / countLifeforms * 100)))
    f.write("   gliders    |     {}     |     {}   \n".format(gliderCount, int(gliderCount / countLifeforms * 100)))
    f.write("   LWS ships  |     {}     |     {}   \n".format(LWSCount, int(LWSCount / countLifeforms * 100)))
    f.write("--------------------------------------\n")
    if aux2:
        countLifeforms -= 1
    f.write("   total      |     {}     |\n".format(countLifeforms))
    f.write("\n\n".format(countLifeforms))

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    ####===== CHOOSE INPUT AND OUTPUT FILE =====####
    query = "input.txt"
    result = "output.txt"

    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    
    # generate starting universe and add existing alive cells
    f = open(query, "r")
    N, M = list(map(int, f.readline().split()))
    gen = int(f.readline())
    grid = np.array([])
    grid = createGrid(N, M)
    while True:
        cell = list(map(int, f.readline().split()))
        if not cell:
            break
        grid[cell[0], cell[1]] = 255
    f.close()

    # set animation update interval
    updateInterval = 50
    
    # create dictionary of lifeforms
    lifeforms = dict()
    lifeforms["block"] = np.array([0, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0])
    lifeforms["beehive"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["loaf"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 255, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["boat"] = np.array([0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["tub"] = np.array([0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["blinker1"] = np.array([0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0])
    lifeforms["blinker2"] = np.array([0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0])
    lifeforms["toad1"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["toad2"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["beacon1"] = np.array([0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["beacon2"] = np.array([0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["glider1"] = np.array([0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0])
    lifeforms["glider2"] = np.array([0, 0, 0, 0, 0, 0, 255, 0, 255, 0, 0, 0, 255, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["glider3"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 255, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0])
    lifeforms["glider4"] = np.array([0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["LWS1"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["LWS2"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 255, 255, 0, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["LWS3"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeforms["LWS4"] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 255, 255, 0, 255, 255, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # start writing the output with date runned and size of universe   
    f = open(result, "w")
    f.write("Simulation at {}\n".format(date.today()))
    f.write("Universe size {} x {}\n".format(N, M))
    f.write("\n")
    f.close()

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M, lifeforms, result),
                                  frames = gen,
                                  interval=updateInterval,
                                  save_count=gen, 
                                  repeat = False)    
    plt.show()

# call main
if __name__ == '__main__':
    aux = True
    main()