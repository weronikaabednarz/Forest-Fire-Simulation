# Forest Fire Simulation
 
The project is a simulation of a forest fire using the 2D cellular automat method, and includes:
- dropping a bomb in random posiotions using "space", extinguishing the fire with belts using the keys from 1 to 0,
- cell states:  "water" - blue, "tree" - green, "burning tree" - red, "burnt tree" - black, "earth" brown,
- transition rules: 
tree -> burning tree with probability p if it has a burning tree as a neighbour, with analogously calculated probability: burning tree -> burnt tree, burnt tree -> ground, ground -> regrown trees,
- visualisation of simulation results.

Technologies used in the project: **Python** with libraries:
- numpy - a library for scientific calculations, operations on multidimensional arrays and matrices,
- pygame - a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library,
- random - a built-in module that you can use to make random numbers,
- matplotlib - a module for creating graphs,
- PIL - a module for image handling.

Start picture:
  
![1](https://github.com/weronikaabednarz/Forest-Fire-Simulation/blob/main/images/mapa.jpg)

Action picture:

![2](https://github.com/weronikaabednarz/Forest-Fire-Simulation/blob/main/images/image1.jpg)

Action continued:

![3](https://github.com/weronikaabednarz/Forest-Fire-Simulation/blob/main/images/image2.png)
