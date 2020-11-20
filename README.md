# HopfFibration

Download Blender 2.9 (or later) for free here: 
https://www.blender.org/download/

## Description
### Overview of the Hopf Fibration
The Hopf Fibration is the fibre bundle created by projecting the four-dimenstional sphere **S3** onto the three-dimentional sphere **S2**, every point on **S2** has a corresponding fibre in three-dimensional space **R3** which is a perfect two-dimensional sphere (or circle) **S1** . This structure is written as **S1 -> S3 -> S2**, which can be read as; "The fibre space **S1** is embedded in the full-space **S3** which is projected to the base-space **S2** . 

This fibre bundle is space-filling in **R3**, every fibre links with every other fibre and no two fibres ever intersect. Lines of constant elevation (&epsilon;) on **S2** are seen as tori in the fibre space, lines of constant azimuth (&alpha;) appear has Hopf bands. There are two edge cases at the poles of **S2** (&alpha = {0,&pi;}); at the south pole ($alpha; = 0) the fibres converge to a circle lying flat in the X-Y plane, at the north pole (&alpha; = &pi;) the fibre is a circle through infinity (here visualised as the straight line lying on the Z-axis).

### This project
The file *fibration.py* is a visualisation tool which uses the Python Blender API. 
This includes the function `makeFibre(elevation,azimuth)` which creates the fibre corresponding to the point on the sphere **S2** at the coordinate (&epsilon;,&alpha;). 
Fibres are visualised as tori in order to be visible, the cross-sectional diameter can be adjusted with the optional argument `sectionRad`. Also included is a function to convert (&epsilon;,&alpha;) into RGB colours for visualisation.

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
