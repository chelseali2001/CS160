import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from wire_plotter import Wire_Plotter

"""
Wrapper class to simplify using the plotting functions
"""
class Wire_Plotter:   
    def __init__(self, length, divisions, temp_min = 0, temp_max = 100, verbose = False):
        self.length         = length
        self.divisions      = divisions
        self.temp_min       = temp_min
        self.temp_max       = temp_max
        self.wire           = []
        self.verbose        = verbose

    def add_interval(self, wire):
        self.wire.append(list.copy(wire))
        self.out("INFO", "Added wire of length %d to plotter." % len(wire))

    def animate(self):
        if self.validate():
            self.out("INFO", "Starting diffusion animation.")
            animate1D(self.wire, self.length, self.divisions, self.temp_min, self.temp_max, smooth=True)
        else:
            self.out("ERROR", "Cannot animate, wire is not valid")

    def draw_interval(self, interval):
        self.validate()
        self.out("INFO", "Drawing wire at time interval %d" % interval)
        draw1D(self.wire[interval], self.length, self.divisions, self.temp_min, self.temp_max, smooth=True)
    
    def draw_last(self):
        self.validate() # Dont need to stop, but should show error
        self.draw_interval(-1)
    
    def validate(self):
        if len(self.wire) < 1:
            self.out("WARN","No intervals to show")
            return False

        size = len(self.wire[0])
        if not all(len(arr) == size for arr in self.wire):
            self.out("WARN","Not all intervals are the same size")
            return False
        return True

    def out(self, state, msg):
        if self.verbose:
            print("PLT-LIB::%-5s|| %s" % (state, msg))
"""
draw 1D

Purpose: Draws heat transfer over wire (1D Array)
Parameters:
    values: 1D array of temperature values
    wire_length: The length of the wire
    wire_divisions: How many segments exist in the wire
    temp_min: minimum temperature of wire. 0 Default
    temp_max: maximum temperature of the wire. 100 Default

    Kwargs: Smooth -> Boolean. True for smooth, otherwise blocky display
"""
def draw1D(values, wire_length, wire_divisions, temp_min = 0, temp_max = 100, **kwargs):

    smooth = 'none'
    if "smooth" in kwargs and kwargs['smooth'] == True:
            smooth = 'bilinear'

    plt.rcParams["figure.figsize"]  = 10, 4
    x = np.linspace(0,wire_length, wire_divisions)
    y = np.asarray(values)

    fig, (ax,ax2) = plt.subplots(nrows=2, sharex=True)

    imgCoords = [
        x[0]-(x[1]-x[0])/2.,    # Left
        x[-1]+(x[1]-x[0])/2.,   # Right
        0,                      # Bottom
        1]                      # Top
    
    ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent =imgCoords, interpolation = smooth, vmin = temp_min, vmax = temp_max)
    ax.set_yticks([])
    ax.set_xlim(imgCoords[0], imgCoords[1])
    

    ax2.plot(x,y)
    plt.tight_layout()
    plt.show()



"""
Animate 1D

Purpose: Animates heat transfer over wire (1D Array)
Parameters:
    allValues: 2D array of temperature values, where second dimension is time
    wire_length: The length of the wire
    wire_divisions: How many segments exist in the wire
    temp_min: minimum temperature of wire. 0 Default
    temp_max: maximum temperature of the wire. 100 Default

    Kwargs: Smooth -> Boolean. True for smooth, otherwise blocky display
"""
def animate1D(all_values, wire_length, wire_divisions, temp_min = 0, temp_max = 100, timeModifier = 5, **kwargs):
    smooth = 'none'
    if "smooth" in kwargs and kwargs['smooth']:
            smooth = 'bilinear'

    plt.rcParams["figure.figsize"] = 10, 4
    x = np.linspace(0, wire_length, wire_divisions)
    y = np.asarray(all_values[0])

    fig, (ax,ax2) = plt.subplots(nrows=2, sharex=True)

    imgCoords = [
        x[0]-(x[1]-x[0])/2.,    # Left
        x[-1]+(x[1]-x[0])/2.,   # Right
        0,                      # Bottom
        1]                      # Top
    
    image = ax.imshow(y[np.newaxis,:], cmap="plasma", aspect="auto", extent = imgCoords, interpolation = smooth, vmin = temp_min, vmax = temp_max)
    ax.set_yticks([])
    ax.set_xlim(imgCoords[0], imgCoords[1])
    
    linePlot, = ax2.plot(x,y)
    
    def animate(i):
        y = np.asarray(all_values[i])
        
        image.set_array(y[np.newaxis,:])
        linePlot.set_ydata(y)
        return [image]
    
    ani = FuncAnimation(fig, animate, np.arange(0, len(all_values)), interval = 100, blit = False, repeat=False)

    plt.tight_layout()
    plt.show()
    del ani
    plt.close()

def main(wireLen, wireDiv, tempLeft, tempRight):
    wire_len = wireLen
    wire_div = wireDiv
    temp_left = tempLeft
    temp_right = tempRight

    # setting up the plotter
    plotter = Wire_Plotter(wire_len, wire_div, temp_left, temp_right, True)

    f = open("wire_temps.csv", "r")
    lines = f.readlines()
    for line in lines:
        # reading in a line from the file and separating it on spaces
        wire_temps = line.split(",")
        # converting all elements of the list to be floats
        for i in range(len(wire_temps)):
           wire_temps[i]=float(wire_temps[i])
        print(wire_temps)
        # this is where you would pass in your array of wire temperatures
        plotter.add_interval(wire_temps)
    # call this once you have added all the lines and it will animate
    plotter.animate()

# Inputs
var = input("Enter the thermal conductivity, density, and specific heat: ").split()
conditions = input("Enter the initial temperature and boundary conditions: ").split()
wire = input("Enter the wire length and sections: ").split()
time = input("Enter the time intervals and change in time: ").split()

deltaX = float(wire[0]) / float(wire[1])
const = (float(var[0]) * float(time[1])) / (deltaX ** 2 * float(var[2]) * float(var[1]))

uOld = [float(conditions[0])] * int(wire[1])
uOld[0] = float(conditions[1])
uOld[int(wire[1]) - 1] = float(conditions[2])

uNew = [float(conditions[0])] * int(wire[1])
uNew[0] = float(conditions[1])
uNew[int(wire[1]) - 1] = float(conditions[2])

timeX = 0

if abs((float(var[0]) * float(time[1])) / ((float(conditions[2]) - float(conditions[1])) ** 2 * float(var[2]) * float(var[1]))) < 0.5:
    for x in range(int(time[0])):
        for i in range(1, int(wire[1]) - 1):
            uNew[i] = const*(uOld[i+1]-2*uOld[i]+uOld[i-1])+uOld[i]

        print(x + 1)
        print(uNew)    
        uOld = uNew[:]
else:
    print("Error: invalid inputs")

main(float(wire[0]), int(wire[1]), float(conditions[1]), float(conditions[2]))