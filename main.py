from progam_ui import create_game
from image_processing import image_processor
from image_processing import make_graph
from image_processing import image_processor_multiple
from PIL import Image
from PIL import ImageDraw
import pygame
from PIL import ImageFont

# from image_processing import color_processor
# from image_processing import draw_the_info

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

image_string = create_game()
if image_string != None:

    if image_string[3]:

        color_list_input = image_processor(image_string[0][0])
    

        for color in color_list_input[0]:
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


        make_graph(color_dict, image_string[1], image_string[2])

    else:
        
        # mf = ImageFont.truetype('font.ttf', 25)
        # Add Text to an image
        count = 0
        has_happened = False

        # Display edited image on which we have added the text

        for image in image_string[0]:
            
            color_list_input = image_processor_multiple(image)
            count = count + 1

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
            if has_happened:
                pygame.quit()
            
            pygame.init()
            scrn = pygame.display.set_mode((800, 600))
            imp = pygame.image.load("C:\\Users\\Ben\Color-Makeup-Machine\images\Loaded_Image.png").convert()
            scrn.blit(imp, (0, 0))
            pygame.display.update()

            #i = Image.open('C:\\Users\\Ben\Color-Makeup-Machine\images\Background.png')
            #Im = ImageDraw.Draw(imp)
            # imp.text((0,0), "Images processed: "+ str(count), (25,190, 60))
            # imp.show()
            has_happened = True
        pygame.quit()
                    # Im.text((15,15), "Lady watching movie with her dog", (255,0,0), font=mf)
            #scrn.fill('black')
            # scrn.
        
        make_graph(color_dict, image_string[1], image_string[2])
