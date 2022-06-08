# Author: Samantha Murray Tuesta
# Date: May 25, 2020
# Description: Implement a program to plot data from a chart on a map to
# show earthquake trends using turtle

import turtle

# teleport t to the latitude and longitude
def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and up/down state is the
        same as before.
    """
    # save the current pen state
    pen_was_down = t.isdown()
    
    # pick up pen, move to coordinates
    t.up()
    t.goto(x, y)
    
    # restore pen state
    if pen_was_down:
        t.down()

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle; return a turtle object in hidden
        state. The canvas has size canv_width by canv_height, with a
        coordinate system where (0,0) is in the center, and automatic
        re-drawing of the canvas is disabled. Set the background image to
        earth.png.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    turtle.bgpic('earth.png') # set the background image
    turtle.update()
    return t

def parse_row(line):
    """ Parse a line of the csv file, returning a dict with keys
    for latitude, longitude, timestamp, and magnitude.
    Pre: line is an unprocessed string representing a line of the file.
    Post: the returned dict has the following keys with values according
          to the data in the given line of the file:
            "latitude" -> (float)
            "longitude" -> (float)
            "timestamp" -> (str)
            "magnitude" -> (float)
    """
    # the line has all the data separated by commas, so
    # split the line into its constituent numbers
    # to make it easy to access the latitude, longitude, timestamp, and magnitude values
    split = line.split(",")
    
    # create a dictionary
    dict = {}
    #Populate the dictionary with the keys and values for latitude, longitude, timestamp, magnitude
    
    lat = split[0]
    long = split[1]
    time = split[2]
    mag = split[3]
    
    dict['latitude'] = float(lat)
    dict['longitude'] = float(long)
    dict['timestamp'] = str(time)
    dict['magnitude'] = float(mag)
    
    # return the resulting dictionary
    return(dict)

def main():
    """ Main function: plot a circle on a map for each earthquake """
    # we'll scale coordinates and canvas to be 720x360, double
    # the size of the range of lat/lon coordinates
    scale = 2.0
    
    # call turtle_setup to set up the canvas and get a turtle
    t = turtle_setup(scale * 360, scale * 180)
    
    # open earthquakes.csv for reading
    eq_file = open('earthquakes.csv', 'r')
    
    # make a list to store the earthquate dictionaries
    eq_dict = []
    
    # parse each line of the file using parse_row and add each returned
    # dictionary into the list (skip the headers on the first line!)
    for line in eq_file.readlines()[1:]:
        dict = parse_row(line)
        eq_dict.append(dict)

    # for each earthquake dictionary in the list:
    for dict in eq_dict:
        lat = dict['latitude']
        long = dict['longitude']
        time = dict['timestamp']
        mag = dict['magnitude']
        # if the magnitude is larger than 1.0:
        if mag > 1.0:
            # draw a circle with radius equal to the magnitude
            # at (longitude * scale, latitude * scale).
            teleport(t, long*scale, lat*scale)
            t.circle(mag)
        # if the magnitude is less than 1.0 circle radius is one to see
        # earthquake
        else:
            t.circle(1)
            
        # (challenge) by date.
        # Looking at the data, you may notice that the
        # earthquakes in our dataset all happened in 2016.
        #if the earthquake happened in july
        if time[5:7] == '07':
            #if before the 29th skyblue
            if int(time[8:10]) <= 29: 
                t.color('skyblue')
            #if after the 29th violet
            elif int(time[8:10]) > 29:
                t.color('violet')
        #if august earthquake
        elif time[5:7] == '08':
            #if before the 9th pink
            if int(time[8:10]) <= 9: 
                t.color('pink')
            #if before the 19th red
            elif int(time[8:10]) <= 19:
                t.color('red')
            #if before the 31st white
            elif int(time[8:10]) <= 31:
                t.color('white')

    # update the screen so all the circles are drawn on the canvas
    turtle.update()
    
if __name__ == "__main__":
    main()


