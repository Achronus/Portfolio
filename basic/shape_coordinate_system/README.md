# Shape Coordinate System

This project involves creation of a two-dimensional virtual coordinate system, allowing you to store basic geometric shapes coordinate positions.

Firstly, you will be brought to a main menu screen like the below:

```Psuedocode
-------------------------------------------------------------------------------------------------------
Main command menu
-------------------------------------------------------------------------------------------------------
- add - Create a new shape
- shift - Move or scale an existing shape
- menu - Displays the list of user commands
- display - Displays a list of shapes created
- exit - Exits the program
-------------------------------------------------------------------------------------------------------
Enter the command:
```

Upon inputting the 'add' command, you will be brought to a new menu. Here you can select which shape/s to add.

```Psuedocode
-------------------------------------------------------------------------------------------------------
Input the command for the shape you would like to create
-------------------------------------------------------------------------------------------------------
- rectangle [x_coordinate] [y_coordinate] [height] [width] - Creates a rectangle
- square [x_coordinate] [y_coordinate] [edge_length] - Creates a square
- circle [x_coordinate] [y_coordinate] [radius] - Creates a circle
-------------------------------------------------------------------------------------------------------
Enter the command:
```

Adding a shape is similar to the below.

```Psuedocode
Enter the command: rectangle 10 10 4 3
Rectangle[h=4,w=3]
Points[(10, 10), (13, 10), (13, 14), (10, 14)]
Area=12.00 Perimeter=14.00

Input the command 'menu' for the list of commands.
```

From here you can now go back to the main menu, input the 'shift' command and manipulate a shape with either move or scale. The shift menu looks like the following:

```Psuedocode
-------------------------------------------------------------------------------------------------------
Input the command to change a shape
-------------------------------------------------------------------------------------------------------
- move [shape_index] [x_coordinate] [y_coordinate] - Moves a created shape
- scale [shape_index] [x_scale_amount] [y_scale_amount] - Scales a created shape
-------------------------------------------------------------------------------------------------------
------------------------------
Shape Number: 1
------------------------------
Rectangle[h=4,w=3]
Points[(10, 10), (13, 10), (13, 14), (10, 14)]
Area=12.00 Perimeter=14.00
```
