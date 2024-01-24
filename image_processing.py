
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

#this function takes in a list of file paths as an input, and returns a list of color data
def image_processor(image_string):
    total_list_for_one_image = []
    #image_position_tracker = {}
    
    image_pixel_info = []
    im = Image.open(image_string)
    px = im.load()
    total_height = im.size[1] 
    # print("y" + str(total_height))
    # print("x" + str(im.size[0]))

    # print(im.size[0])
    # print(im.size[1])
    # f = open('all_things_read.txt', 'w')
    for height in range(im.size[1]):
        for width in range(im.size[0]):   
            #have to minus it from total as this program starts reading from top left corner
            # print("x,y:" +str(width) + "," + str(height))
            #print(width)
            #print(height)
            pixel_touple = px[width, height]
            # f.write('x: '+str(width) +'y: '+str(height) +'= '+str(px[width,height]) + '\n')
            if width==17 and height==203:
                print("it happens," + str(pixel_touple))
         
            # print("x,y:" +str(width) + "," + str(height) + 'color' + str(pixel_touple))
            # pixel_touple = px[width,total_height - height]
            #image_position_tracker[(height,width)] = (int(pixel_touple[0]), int(pixel_touple[1]), int(pixel_touple[2]))
            # print(pixel_touple)
            image_pixel_info.append((int(pixel_touple[0]), int(pixel_touple[1]), int(pixel_touple[2])))
    total_list_for_one_image.append(image_pixel_info)
    
    #print(total_list_for_one_image)
    print(im.size[0])
    print(im.size[1])
    return (total_list_for_one_image, im.size[0], im.size[1])

def color_processor(list_of_lists, width, height):
    color_list = []
    mut_height= height
    mut_width= width
    image_position_tracker = {}
    # f = open('entire_things made.txt', 'w')
    count = 0
    for total_list in list_of_lists:
        picture_iter = 0
        pixel_num = 0
        #for color_tuple in total_list:
        print(width)
        print(height)
       
        for mut_height in range(height):    
            for mut_width in range(width):
                # print(count)
                # count = count +1 
               

                color_tuple = total_list[pixel_num]
                # print(color_tuple)
                pixel_num = pixel_num + 1
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
                    image_position_tracker[mut_width, mut_height]  = "yellow"
                elif color_tuple[0] >150 and color_tuple[1] <120 and color_tuple[2] >150:
                    color_list.append("magenta")
                    image_position_tracker[mut_width, mut_height]  = "magenta"
                elif color_tuple[0] <120 and color_tuple[1] >150 and color_tuple[2] >150:
                    color_list.append("cyan")
                    image_position_tracker[mut_width, mut_height]  = "cyan"
                elif percent_diffrence < 20:
                    if color_tuple[0]>150 and color_tuple[0]<230:
                        color_list.append("grey")
                        image_position_tracker[mut_width, mut_height]  = "grey"

                    elif color_tuple[0]>=230:
                        color_list.append("white")
                        image_position_tracker[mut_width, mut_height]  = "white"

                    elif color_tuple[0] < 150:
                        color_list.append("black")
                        image_position_tracker[mut_width, mut_height]  = "black"
                elif largest_color == 0:
                    color_list.append("red")
                    image_position_tracker[mut_width, mut_height]  = "red"
                elif largest_color == 1:
                    color_list.append("green")
                    image_position_tracker[mut_width, mut_height] = "yellow"
                elif largest_color == 2:
                    color_list.append("blue")
                    image_position_tracker[mut_width, mut_height] = "blue"
                else:
                    color_list.append("pink")
                    image_position_tracker[mut_width, mut_height] = "pink"
            
                # f.write('x: '+str(mut_width) +'y: '+str(mut_height) +'= '+str(image_position_tracker[mut_width, mut_height]) + '\n')
            # if mut_width != width:
            #     mut_width = mut_width +1
            # else: 
            #     print( mut_width, mut_height)
            #     mut_width = 0
            #     mut_height = mut_height +1    
        picture_iter = picture_iter +1

    #print(image_position_tracker)
    #print(image_position_tracker)
    # f.close()
    return color_list, image_position_tracker
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
    im = Image.new('RGBA', (width, height), (25, 25, 25, 0))
    draw = ImageDraw.Draw(im) 
    # pixel_num=0
    #print(color_list)
    # print(width)
    # print(height)
    # f = open('entire_data_Base.txt', 'w')
    for l in range(height):
        for i in range(width):
            # print("x,y:" +str(i) + "," + str(l), image_position_tracker[i,l])
            # print(image_position_tracker[i,l])
            # if image_position_tracker[i,l] != None:
        
            # f.write('x: '+str(i) +'y: '+str(l) +'= '+str(image_position_tracker[i,l]) + '\n')
            draw.point((i, l), image_position_tracker[i, l])
        
            # else:

            # draw.point((i,l), "pink" )
            # pixel_num = pixel_num+1
    im.show()
    # f.close()
    #im.save("ImageDraw.png")
    
    

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

