"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    distance = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    year_distance = GRAPH_MARGIN_SIZE + distance*year_index

    return year_distance

def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    #canvas.create_line(15, 25, 200, 25)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       fill='black')
    distance = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE*2) / len(YEARS)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + i * distance, 0,
                           GRAPH_MARGIN_SIZE + i * distance, CANVAS_HEIGHT)
        x_label = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_text(x_label + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

    #tkinter.mainloop()

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # print(name_data)
    # exit()
    distance = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    color_order = 0
    for name in lookup_names:
        rank_list = []
        for x in YEARS:
            year = str(x)
            if year in name_data[name]:
                rank_list.append(name_data[name][year])
            else:
                rank_list.append('580')
        print(rank_list)
        initial = GRAPH_MARGIN_SIZE
        for x in range(len(rank_list)-1):
            if int(rank_list[x]) >= 580:
                rank_list[x] = 580
            else:
                pass
            if int(rank_list[x+1]) >= 580:
                rank_list[x+1] = 580
            else:
                pass
            canvas.create_line(initial, rank_list[x], initial+distance, rank_list[x+1], fill =COLORS[color_order])
            for i in range(len(YEARS)):
                if int(rank_list[x]) >= 580:
                    canvas.create_text(initial + TEXT_DX, rank_list[x], text=name + str('*'),
                                       anchor=tkinter.SW, fill=COLORS[color_order])
                else:
                    canvas.create_text(initial + TEXT_DX, rank_list[x], text=name + str(rank_list[x]),
                                   anchor=tkinter.SW,fill =COLORS[color_order])
            initial += distance
        color_order += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
