print()
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random 


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    
    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,scene_width,scene_height)
    draw_stars(canvas, scene_height, scene_width, 0.10, 1000)
    draw_clouds(canvas, 1, 10, 47) 
    draw_clouds(canvas, 1, 200, 47) 
    draw_clouds(canvas, 1, 500, 47)
    draw_clouds(canvas, 1, 700, 47)  
    draw_ground(canvas,scene_width, scene_height)
    draw_pine_tree(canvas, 7)
    draw_grid(canvas, scene_width, scene_height, 50)
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_pine_tree(canvas, num_trees):
    # Draw the tunk of the tree
    for i in range (num_trees):
        height = random.randint(100, 230)
        center_x = random.randint(0, 750) + 2
        trunk_width = height / 10
        trunk_height = height / 8
        left_trunk = center_x - trunk_width / 2
        bottom_trunk = random.randint(0, 160)
        right_trunk = center_x + trunk_width /2
        trunk_top = bottom_trunk + trunk_height
        draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, 
        trunk_top, fill="tan4")

        # Draw the skirt of the tree
        skirt_width = height / 2
        skirt_left = center_x - skirt_width / 2
        skirt_bottom = trunk_top
        peak_x = center_x
        peak_y = bottom_trunk + height
        skirt_right = center_x + skirt_width / 2
        draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, 
        peak_y, skirt_right, skirt_bottom, fill="darkGreen")

def draw_grid(canvas, width, height, interval):
    # Draw vertical lines
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    
    # Draw horizontal lines
    label_x = 15
    for y in range (interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="navyBlue")

def draw_clouds(canvas, num_clouds, b, diameter):
    for i in range (num_clouds):
        x = b 
        y = 300
        draw_oval (canvas, x,  y, x + diameter, y + diameter, fill='white', outline='white')
        x = b + 21
        y = y + 30
        draw_oval (canvas, x,  y, x + diameter, y + diameter, fill='white', outline='white')
        x = b + 45
        y = 320
        draw_oval (canvas, x,  y, x + diameter, y + diameter, fill='white', outline='white')
        x = b + 40 
        y = 300
        draw_oval (canvas, x,  y, x + diameter, y + diameter, fill='white', outline='white')
        x = b + 70 
        y = 315
        draw_oval (canvas, x,  y, x + diameter, y + diameter, fill='white', outline='white')
    
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="saddleBrown")

def draw_stars (canvas, scene_height, scene_width, star_size, num_stars):
    for i in range(num_stars):
        x = random.randint(0, scene_width)
        y = random.randint(int(scene_height / 3), scene_height)
        draw_oval(canvas, x, y, x+star_size, y+star_size, outline="gray85", fill ="gray85") 
   
# Call the main function so that
# this program will start executing.
main()