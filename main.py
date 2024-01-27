from progam_ui import create_game
from image_processing import image_processor
from image_processing import make_graph
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
    # x= 0
    for image in image_string[0]:
        # x=x+1
        #print("image "+str(x)+" done processing")
        color_list_input = image_processor(image)
        # color_list = color_processor(color_list_input[0],  color_list_input[1], color_list_input[2])
        #if make_image == True:
        #draw_the_info(color_list_input[1], color_list_input[2], color_list_input[3])

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
