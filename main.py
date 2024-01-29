from progam_ui import create_game
from image_processing import image_processor
from image_processing import make_graph
from image_processing import image_processor_multiple
from PIL import Image
from PIL import ImageDraw
import pygame
from PIL import ImageFont

#This is the main file for the program, using other functions it makes a dictionary of the color of every pixel, then creates a graph of that information 


#This dictionary tracks the colors of pixels through many images, once processed the keys hold the total number of times each colored pixel appears
#Using this dictionary instead of a list saves a lot of memory and causes the program to preform much better
color_dict = {
        'red':0,
        'green':0,
        'blue':0,
        'grey':0,
        'white':0,
        'black':0,
        'yellow':0,
        'magenta':0,
        'cyan':0,
    }

#This calls the create game function (located within the program_ui.py file), which makes the first visual part of the progam, allowing the user  to choose program specifications
#The function returns a tuple containing (str(the file destination), bool(if the function should be a percent), bool(if the function should create a pie chart), bool(if the function should be one image) )
image_string = create_game()

#This if statement means if no image is given, instead of crashing the program just closes
if image_string != None:

    #This if statement, checks if one image or multiple are being inputted, if the bool is true the program runs expecting one thing, if false the else hands mutliple
    if image_string[3]:

        #This function (located within image_processing.py) goes through the image and gets a string discribing the color for each pixel, 
        #then reuturn a list of all those pixels.
        #As well this function displays a visual copy of the inputed image, but with each pixel being replaced by the more vague color this program works with.
        color_list = image_processor(image_string[0][0])
    
        #This for loop goes over each color in the list, and then adds to the respective dictionary key. 
        for color in color_list[0]:
            if color == "red":
                color_dict['red'] = color_dict['red'] + 1
            if color == "green":
                color_dict['green'] = color_dict['green'] + 1
            if color == "blue":
                color_dict['blue'] = color_dict['blue'] + 1
            if color == "grey":
                color_dict['grey'] = color_dict['grey'] + 1
            if color == "white":
                color_dict['white'] = color_dict['white'] + 1
            if color == "black":
                color_dict['black'] = color_dict['black'] + 1
            if color == "yellow":
                color_dict['yellow'] = color_dict['yellow'] + 1
            if color == "magenta":
                color_dict['magenta'] = color_dict['magenta'] + 1
            if color == "cyan":
                color_dict['cyan'] = color_dict['cyan'] + 1

        #This function (located within program_ui.py), takes in the dictionary and graph information
        #then creates and displays that graph.
        make_graph(color_dict, image_string[1], image_string[2])

    else:
        #This varible lets the program know if a new window has been made, as it becomes True when a window is made       
        has_happened = False

        #This for loop iterates over mutlipe image file paths, and adds to the color dictionary for each of them.
        for image in image_string[0]:
            
            #This function (located within image_processing.py) goes through the image and gets a string discribing the color for each pixel, 
            #then reuturn a list of all those pixels.
            color_list_input = image_processor_multiple(image)

            #This for loop goes over each color in the list, and then adds to the respective dictionary key. 
            for color in color_list_input:
                if color == "red":
                    color_dict['red'] = color_dict['red'] + 1
                if color == "green":
                    color_dict['green'] = color_dict['green'] + 1
                if color == "blue":
                    color_dict['blue'] = color_dict['blue'] + 1
                if color == "grey":
                    color_dict['grey'] = color_dict['grey'] + 1
                if color == "white":
                    color_dict['white'] = color_dict['white'] + 1
                if color == "black":
                    color_dict['black'] = color_dict['black'] + 1
                if color == "yellow":
                    color_dict['yellow'] = color_dict['yellow'] + 1
                if color == "magenta":
                    color_dict['magenta'] = color_dict['magenta'] + 1
                if color == "cyan":
                    color_dict['cyan'] = color_dict['cyan'] + 1
            
            #This if statement makes it so whenever a new iteration occurs the winodw displaying that an iteration has accured closes.
            if has_happened:
                pygame.quit()
            
            #The five lines below this open a window displaying the words "One Image Has Loaded!", this window is disigned to pop up everytime a single image has loaded,
            #letting the user know the program is working.
            pygame.init()
            scrn = pygame.display.set_mode((800, 600))
            imp = pygame.image.load("C:\\Users\\Ben\\Color-Makeup-Machine\\images\\Loaded_Image.png").convert()

            scrn.blit(imp, (0, 0))
            pygame.display.update()

            #Lets the program know that a window has been opened
            has_happened = True
        pygame.quit()

        #This function (located within program_ui.py), takes in the dictionary and graph information
        #then creates and displays that graph.
        make_graph(color_dict, image_string[1], image_string[2])
