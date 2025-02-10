import turtle
from turtle import *

# Set up the window and title
turtle.title("rainbow spiral")  # Sets the title of the turtle graphics window
speed(15)  # Sets the turtle speed to 15 (fastest speed)
bgcolor("black")  # Sets the background color of the window to black

# Initialize RGB values (Red, Green, Blue)
r, g, b = 255, 0, 0  # Start with red (255), green (0), and blue (0)

# Main loop that runs 510 times
for i in range(255 * 2):  # Loop will run from 0 to 509 (510 iterations)
    colormode(255)  # Sets color mode to 255, which uses RGB values in the range 0-255
    
    # Gradually modify the RGB values to create a rainbow effect
    if i < 255 // 3:  # For the first third of the loop
        g += 3  # Increase green gradually
    elif i < 255 * 2 // 3:  # For the second third of the loop
        r -= 3  # Decrease red gradually
    elif i < 255:  # When i is less than 255 (approximately the third point)
        b += 3  # Increase blue gradually
    elif i < 255 * 4 // 3:  # As the loop progresses further (starting after 255)
        g -= 3  # Decrease green gradually
    elif i < 255 * 5 // 3:  # Another stage of the loop
        r += 3  # Increase red gradually
    else:  # In the final stage of the loop (i > 255*5//3)
        b -= 3  # Decrease blue gradually
    
    fd(50 + i)  # Move the turtle forward by (50 + i) units, which increases as i increases
    rt(91)  # Turn the turtle right by 91 degrees (causing a spiral effect)
    pencolor(r, g, b)  # Set the pen color based on the current RGB values

done()  # Finish the drawing and keep the window open
