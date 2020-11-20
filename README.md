# HopfFibration

Download Blender 2.9 (or later) for free here: 
https://www.blender.org/download/

Includes the function `makeFibre(elevation,azimuth)` which creates the fibre corresponding to the point on the projective sphere at the coordinate (&epsilon;,&alpha;). 
Also included is a function to convert (&epsilon;,&alpha;) into RGB colours for visualisation.

## Example renders

![Hopf fibration example 1](https://github.com/For-The-Wolf/HopfFibration/blob/main/Example%20Renders/hopf_fibration_1.JPG?raw=true)
![Hopf fibration example 2](https://github.com/For-The-Wolf/HopfFibration/blob/main/Example%20Renders/hopf_fibration_3.JPG?raw=true)
![Hopf fibration example 3](https://github.com/For-The-Wolf/HopfFibration/blob/main/Example%20Renders/hopf_fibration_4.JPG?raw=true)

## Directions

Simply make a new Blender file or download the provided example(*fibration.blend*), create a Text Editor pane, open the *fibration.py* file and use the keyboard shortcut `Alt+P` to run the script. 
This will run an example visualisation which generates fibres constructing six tori and the two edge cases at &epsilon; = {0,pi/2} (a flat cricle and a circle through infinity respectively).

![Hopf fibration visualisation in blender](https://github.com/For-The-Wolf/HopfFibration/blob/main/Example%20Renders/hopf_fibration_SS.JPG?raw=true)

## To do
- [ ] Improve the automatic colouring of fibres
- [ ] Add functionality for easy animation creation 
