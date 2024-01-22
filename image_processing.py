
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

#this function takes in a list of file paths as an input, and returns a list of color data
def image_processor(image_string):
    total_list_for_one_image = []
    #image_position_tracker = {}
    
    image_pixel_info = []
    im = Image.open(image_string)
    px = im.load()
    
    for height in range(im.size[0]-1):
        for width in range(im.size[1]-1):
            pixel_touple = px[height,width]
            #image_position_tracker[(height,width)] = (int(pixel_touple[0]), int(pixel_touple[1]), int(pixel_touple[2]))
            #print("x,y:" +str(height) + "," + str(width) + 'color' + str(pixel_touple))
            # print(pixel_touple)
            image_pixel_info.append((int(pixel_touple[0]), int(pixel_touple[1]), int(pixel_touple[2])))
    total_list_for_one_image.append(image_pixel_info)
    
    #print(total_list_for_one_image)
    return (total_list_for_one_image, width, height, )

def color_processor(list_of_lists, width, height):
    color_list = []
    mut_height= 0
    mut_width= 0
    image_position_tracker2 = {}
    for total_list in list_of_lists:
       
        for color_tuple in total_list:
            
    
            
            #print(str(mut_height), str(mut_width))
    
            largest_color = 4
            smallest_color = 4

            #print(color_tuple)
            if color_tuple[0] > color_tuple[1] and color_tuple[0] >color_tuple[2]:
                largest_color = 0
            elif color_tuple[1] > color_tuple[0] and color_tuple[1] > color_tuple[2]:
                largest_color =1
            else:
                largest_color =2
            
            if color_tuple[0] < color_tuple[1] and color_tuple[0] <color_tuple[2]:
                smallest_color = 0
            elif color_tuple[1] < color_tuple[0] and color_tuple[1] < color_tuple[2]:
                smallest_color =1
            else:
                smallest_color =2
            
            
            percent_diffrence = ((color_tuple[largest_color] - color_tuple[smallest_color]) / (color_tuple[smallest_color]+1)) * 100
            #print(percent_diffrence)

            if color_tuple[0] >150 and color_tuple[1] >150 and color_tuple[2] <120:
                color_list.append("yellow")
                image_position_tracker2[mut_height, mut_width]  = "yellow"
            elif color_tuple[0] >150 and color_tuple[1] <120 and color_tuple[2] >150:
                color_list.append("magenta")
                image_position_tracker2[mut_height, mut_width]  = "magenta"

            elif color_tuple[0] <120 and color_tuple[1] >150 and color_tuple[2] >150:
                color_list.append("cyan")
                image_position_tracker2[mut_height, mut_width]  = "cyan"

            elif percent_diffrence < 20:
                if color_tuple[0]>150 and color_tuple[0]<230:
                    color_list.append("grey")
                    image_position_tracker2[mut_height, mut_width]  = "grey"

                elif color_tuple[0]>=230:
                    color_list.append("white")
                    image_position_tracker2[mut_height, mut_width]  = "white"

                elif color_tuple[0] < 150:
                    color_list.append("black")
                    image_position_tracker2[mut_height, mut_width]  = "black"

            elif largest_color == 0:
                color_list.append("red")
                image_position_tracker2[mut_height, mut_width]  = "red"
                
            elif largest_color == 1:
                color_list.append("green")
                image_position_tracker2[mut_height, mut_width] = "yellow"

            elif largest_color == 2:
                color_list.append("blue")
                image_position_tracker2[mut_height, mut_width] = "blue"
            
            
            if mut_width != width+1:
                mut_width = mut_width +1
            else: 
                mut_width = 0
                mut_height = mut_height +1    
                    
    #print(image_position_tracker2)
    print(image_position_tracker2)
    return color_list, image_position_tracker2
            #print(color_list.pop)
    #print(color_list)
       
    #make_graph(color_list)
        
def make_graph(color_dict, is_percent, is_pie):
    colors = 'red', 'green', 'blue', 'grey', 'white', 'black', 'yellow', 'magenta','cyan' 
    colors_list = ['red', 'green', 'blue', 'grey', 'white', 'black', 'yellow', 'magenta','cyan'] 
    #print(color_dict)
    color_dict2 = color_dict
    if is_percent:
        total = color_dict['red'] + color_dict['green'] + color_dict['blue'] + color_dict['grey'] + color_dict['white'] + color_dict['black'] +color_dict['yellow'] + color_dict['magenta'] + color_dict['cyan']
        Runs = [(color_dict['red']/total)*100, (color_dict['green']/total)*100, (color_dict['blue']/total)*100, (color_dict['grey']/total)*100, (color_dict['white']/total)*100, (color_dict['black']/total)*100, (color_dict['yellow']/total)*100, (color_dict['magenta']/total)*100, (color_dict['cyan']/total)*100]
    else:
        Runs = [color_dict['red'], color_dict['green'], color_dict['blue'], color_dict['grey'], color_dict['white'], color_dict['black'], color_dict['yellow'], color_dict['magenta'], color_dict['cyan']]

#bar graph
    if is_pie:
        count =0
        #print(Runs)
        for percents  in Runs[:]:
            print('what happens' + str(percents))
            if percents < 1.0:
                Runs.remove(percents)
                for entries in colors_list:
                    #print(color_dict2[entries])
                    #print(colors_list)
                    if (color_dict2[entries]/total)*100 == percents:
                        colors_list.remove(entries)

            else:
                count = count + 1
        
        explode = []    
        colors = tuple(colors_list)
        # print(colors)
        # print(Runs)
        for i in range(count):
            explode.append(0)
         # it "explode" the 1st slice
        # print(Runs)
        # print(colors_list)
        # print(explode)     
        fig1, ax1 = plt.subplots()    
        ax1.pie(Runs, explode=explode, labels=colors, autopct='%1.1f%%',    
                shadow=True, startangle=90)    
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
        plt.show()    

    else:
        
        #print(Runs)
        plt.bar(colors,Runs,color = 'black')    
        plt.title('Result')    
        plt.xlabel('Colors')    
        plt.ylabel('Pixels of that color')    
        plt.show()    


def draw_the_info(image_position_tracker, width, height):
    im = Image.new('RGBA', ( height, width), (25, 25, 25, 0))
    draw = ImageDraw.Draw(im) 
    pixel_num=0
    #print(color_list)
    for i in range(height-1):
        for l in range(width-1):
            #print("x,y:" +str(height-i) + "," + str(width-l))
            draw.point((height- i, width - l), image_position_tracker[height - i, width - l])
            pixel_num = pixel_num+1
    im.show()
    #im.save("ImageDraw.png")
    
    

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

